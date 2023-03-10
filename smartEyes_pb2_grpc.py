# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import smartEyes_pb2 as smartEyes__pb2


class SmartEyesRPCStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListRules = channel.unary_unary(
                '/smartEyes.SmartEyesRPC/ListRules',
                request_serializer=smartEyes__pb2.ListRulesRequest.SerializeToString,
                response_deserializer=smartEyes__pb2.RuleSet.FromString,
                )
        self.Flush = channel.unary_unary(
                '/smartEyes.SmartEyesRPC/Flush',
                request_serializer=smartEyes__pb2.Empty.SerializeToString,
                response_deserializer=smartEyes__pb2.StringResponse.FromString,
                )
        self.StartPacketHandler = channel.unary_unary(
                '/smartEyes.SmartEyesRPC/StartPacketHandler',
                request_serializer=smartEyes__pb2.Empty.SerializeToString,
                response_deserializer=smartEyes__pb2.StringResponse.FromString,
                )
        self.StopPacketHandler = channel.unary_unary(
                '/smartEyes.SmartEyesRPC/StopPacketHandler',
                request_serializer=smartEyes__pb2.Empty.SerializeToString,
                response_deserializer=smartEyes__pb2.StringResponse.FromString,
                )


class SmartEyesRPCServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListRules(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Flush(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartPacketHandler(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopPacketHandler(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SmartEyesRPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListRules': grpc.unary_unary_rpc_method_handler(
                    servicer.ListRules,
                    request_deserializer=smartEyes__pb2.ListRulesRequest.FromString,
                    response_serializer=smartEyes__pb2.RuleSet.SerializeToString,
            ),
            'Flush': grpc.unary_unary_rpc_method_handler(
                    servicer.Flush,
                    request_deserializer=smartEyes__pb2.Empty.FromString,
                    response_serializer=smartEyes__pb2.StringResponse.SerializeToString,
            ),
            'StartPacketHandler': grpc.unary_unary_rpc_method_handler(
                    servicer.StartPacketHandler,
                    request_deserializer=smartEyes__pb2.Empty.FromString,
                    response_serializer=smartEyes__pb2.StringResponse.SerializeToString,
            ),
            'StopPacketHandler': grpc.unary_unary_rpc_method_handler(
                    servicer.StopPacketHandler,
                    request_deserializer=smartEyes__pb2.Empty.FromString,
                    response_serializer=smartEyes__pb2.StringResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'smartEyes.SmartEyesRPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SmartEyesRPC(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListRules(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/smartEyes.SmartEyesRPC/ListRules',
            smartEyes__pb2.ListRulesRequest.SerializeToString,
            smartEyes__pb2.RuleSet.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Flush(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/smartEyes.SmartEyesRPC/Flush',
            smartEyes__pb2.Empty.SerializeToString,
            smartEyes__pb2.StringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartPacketHandler(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/smartEyes.SmartEyesRPC/StartPacketHandler',
            smartEyes__pb2.Empty.SerializeToString,
            smartEyes__pb2.StringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopPacketHandler(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/smartEyes.SmartEyesRPC/StopPacketHandler',
            smartEyes__pb2.Empty.SerializeToString,
            smartEyes__pb2.StringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
