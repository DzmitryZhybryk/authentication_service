from app.compiled_pb import auth_pb2
from app.compiled_pb import auth_pb2_grpc
from sqlalchemy.orm import Session

from app.database import engine
from app.models import User


class Authentication(auth_pb2_grpc.AuthServicer):

    def Login(self, request, context):
        # with Session(engine) as session:
            print(request.username, request.password)
            # new_user = User(username=request.username, password=request.password)
            # session.add(new_user)
            # session.commit()
            return auth_pb2.TokenReply(token="some", token_type="Bearer")
