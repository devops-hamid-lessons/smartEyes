import argparse
import sys
import os
import logging
import smartEyes_pb2
import smartEyes_pb2_grpc
import grpc
import autologging
from concurrent import futures
from libs.credentials import SERVER_CERTIFICATE, SERVER_CERTIFICATE_KEY
from PacketHandler import PacketHandler
from IPTable import IPTable
from Exceptions import NotFoundException
import time, datetime

_ONE_DAY = datetime.timedelta(days=1)


@autologging.traced
@autologging.logged
class SmartEyesRPCServicer(smartEyes_pb2_grpc.SmartEyesRPCServicer):

    def ListRules(self, request, context):
        rules = IPTable.ListRules(request.chain)
        return smartEyes_pb2.RuleSet(rules=rules)

    def Flush(self, request, context):
        try:
            IPTable.Flush()
            context.set_code(grpc.StatusCode.OK)
            return smartEyes_pb2.StringResponse(message="Success")
        except Exception as e:
            return smartEyes_pb2.StringResponse(message=str(e))

    def StartPacketHandler(self, request, context):
        try:
            PacketHandler.instance().start()
            context.set_code(grpc.StatusCode.OK)
            return smartEyes_pb2.StringResponse(message="Success")
        except Exception as e:
            context.set_code(grpc.StatusCode.ABORTED)
            return smartEyes_pb2.StringResponse(message=str(e))

    def StopPacketHandler(self, request, context):
        try:
            PacketHandler.instance().stop()
            context.set_code(grpc.StatusCode.OK)
            return smartEyes_pb2.StringResponse(message="Success")
        except Exception as e:
            return smartEyes_pb2.StringResponse(message=str(e))

def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    smartEyes_pb2_grpc.add_SmartEyesRPCServicer_to_server(
        SmartEyesRPCServicer(), server)

    # Loading credentials
    server_credentials = grpc.ssl_server_credentials([
        (SERVER_CERTIFICATE_KEY,
         SERVER_CERTIFICATE)
    ])

    server.add_secure_port('[::]:' + str(port), server_credentials)
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY.total_seconds())
    except KeyboardInterrupt:
        os.system('rm -f PortNum')
        server.stop(None)



if __name__ == "__main__":
    logging.basicConfig(level=autologging.TRACE, stream=sys.stderr,
                        format="%(levelname)s:%(filename)s,%(lineno)d:%(name)s.%(funcName)s:%(message)s")
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--port', type=int)
    args = parser.parse_args()
    print("[-] Starting the service on", args.port)
    serve(args.port)
