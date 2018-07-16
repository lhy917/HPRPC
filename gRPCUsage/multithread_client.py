# coding: utf8
# multithread_client.py

import grpc

from gRPCUsage import pi_pb2
from gRPCUsage import pi_pb2_grpc

from concurrent import futures


def pi(client, k):
    return client.Calc(pi_pb2.PiRequest(n = k)).value

def main():
    channel = grpc.insecure_channel('localhost:8080')
    client = pi_pb2_grpc.PiCalculatorStub(channel)
    pool = futures.ThreadPoolExecutor(max_workers = 4)
    result = []
    for i in range(1, 1000):
        result.append((i, pool.submit(pi, client, i)))
    pool.shutdown()
    for i, future in result:
        print(i, future.result())


if __name__ == '__main__':
    main()