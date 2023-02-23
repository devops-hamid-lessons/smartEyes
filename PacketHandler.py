#!/usr/bin/python
from scapy.all import *
from scapy.layers.inet import TCP, UDP, IP, Ether, ICMP
from Decorators import Singleton



@Singleton
class PacketHandler:
    """
    This is a Singleton class to handle IP packets.
    """

    def __init__(self) -> None:
        print("Instance create.")

    def _listener(self):
        """
        listen and detect all *Incoming* packets.
        """
        source_mac = Ether().src
        if os.path.exists("./PortNum"):
            f = open('PortNum', 'r')
            gRPC_port = f.read()
            self._s = sniff(prn=self._handler, store=0,
                        filter=f"ether src not {source_mac} and port not 22 and port not {gRPC_port}",
                        stop_filter=lambda p: self._event.is_set())
        else:
            self._s = sniff(prn=self._handler, store=0,
                            filter=f"ether src not {source_mac} and port not 22",
                            stop_filter=lambda p: self._event.is_set())

    def stop(self):
        """
        Stops the process
        """
        try:
            self._event.set()
            print("process stopped.")
        except Exception as e:
            raise e

    def start(self):
        """
        Starts the process.
        """
        try:
            self._event = threading.Event()
            t = threading.Thread(target=self._listener())
            t.start()
            print("listener started.")
        except Exception as e:
            raise e

    def _handler(self, frame):
        """
        A packet handler that distinguishes packets of different protocols.
        A handler method for each protocol is available. You can fill each of them as you prefer.
        """
        try:
            if frame.haslayer(IP):
                pkt = frame[IP]
                if not pkt.src or pkt.src == '127.0.0.1':
                    return None
                src = pkt.src
                dst = pkt.dst
                # fill to handle Ip packets
            else:
                return None
            if pkt.haslayer(TCP):
                tcp = pkt[TCP]
                self.process_tcp(tcp)

            elif pkt.haslayer(UDP):
                udp = pkt[UDP]
                self.process_udp(udp)

            elif pkt.haslayer(ICMP):
                icmp = pkt[ICMP]
                self.process_icmp(icmp)

            else:
                print("unknown layer4")
        except:
            print("something is broken. Continuing")
            traceback.print_exc(file=sys.stdout)

    def process_tcp(self, t):
        """
        The TCP packets handler.
        """
        print("processing tcp")

    def process_udp(self, u):
        """
        The UDP packets handler.
        """
        print("processing udp")

    def process_icmp(self, i):
        """
        The ICMP packets handler.
        """
        print("processing icmp")
