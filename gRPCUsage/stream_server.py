# coding: utf-8
# stream_server.py

import math
import grpc
import time
import random
from concurrent import futures

from gRPCUsage import streaming_pi_pb2
from gRPCUsage import streaming_pi_pb2_grpc

class PiCalculatorServicer(streaming_pi_pb2_grpc.PiCalculatorServicer):

    def Calc(self, request, context):
        for eachrequest in request:
            if random.randint(0, 1) == 1:
                continue
            s = 0.0
            for i in range(request.n):
                s += 1.0 / (2 * i + 1) / (2 * i + 1)
            yield streaming_pi_pb2.PiResponse(n = i, value = math.sqrt(8 * s))


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    servicer = PiCalculatorServicer()
    streaming_pi_pb2_grpc.add_PiCalculatorServicer_to_server(servicer, server)
    server.add_insecure_port('localhost:8080')
    server.start()
    try:
        time.sleep(1000)
    except KeyboardInterrupt:
        server.start(0)


if __name__ == '__main__':
    main()