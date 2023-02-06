from app import auth_pb2
from app import auth_pb2_grpc


class Authentication(auth_pb2_grpc.AuthServicer):

    def SayHello(self, request, context):
        return auth_pb2.HelloReply(message="Opa opa opa-pa")
