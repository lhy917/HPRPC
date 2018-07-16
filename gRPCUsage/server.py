# coding: utf8
# server.py

import math
import grpc
import time
from concurrent import futures

from gRPCUsage import pi_pb2
from gRPCUsage import pi_pb2_grpc

class PiCalcilatorServicer(pi_pb2_grpc.PiCalculatorServicer):

    def Calc(self, request, context):
        s = 0.0
        for i in range(request.n):
            s += 1.0 / (2 * i + 1) / (2 * i + 1)
        return pi_pb2.PiResponse(value=math.sqrt(8 * s))

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    servicer = PiCalcilatorServicer()
    pi_pb2_grpc.add_PiCalculatorServicer_to_server(servicer, server)
    server.add_insecure_port('127.0.0.1:8080')
    server.start()
    try:
        time.sleep(1000)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    main()