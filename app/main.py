import asyncio
from argparse import ArgumentParser
from concurrent import futures

import grpc

from app.compiled_pb import auth_pb2_grpc
from app.handlers import Authentication
from database import engine, Base

parser = ArgumentParser()

parser.add_argument("--host", type=str, default="0.0.0.0")

parser.add_argument("--port", type=int, default=8001)


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


def serve():
    args = parser.parse_args()
    # asyncio.run(init_models())
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    auth_pb2_grpc.add_AuthServicer_to_server(Authentication(), server)
    # server.add_insecure_port('0.0.0.0:50051')
    server.add_insecure_port(address=f"{args.host}:{args.port}")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
