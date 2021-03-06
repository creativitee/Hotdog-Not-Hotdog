# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import hashing_pb2 as hashing__pb2


class ByteStreamHashingStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Hashing = channel.unary_unary(
        '/ByteStreamHashing/Hashing',
        request_serializer=hashing__pb2.HashRequest.SerializeToString,
        response_deserializer=hashing__pb2.HashReply.FromString,
        )


class ByteStreamHashingServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Hashing(self, request, context):
    """hash the byte stream of a photo file with sha256
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ByteStreamHashingServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Hashing': grpc.unary_unary_rpc_method_handler(
          servicer.Hashing,
          request_deserializer=hashing__pb2.HashRequest.FromString,
          response_serializer=hashing__pb2.HashReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ByteStreamHashing', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
