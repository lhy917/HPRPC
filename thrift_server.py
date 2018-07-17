# coding: utf-8
# server.py

import sys
import math

from thrift.transport import TSocket, TTransport
from thrift.protocol import TCompactProtocol
from thrift.server import TServer

from pi.ttypes import PiResponse, IllegaArgument
from pi.PiService import Iface, Processor


class PiHandler(Iface):

    def cal(self, req):
        if req.n <= 0:
            raise IllegaArgument(message='parameter must be positive')
        s = 0.0
        for i in range(req.n):
            s += 1.0 / (2 * i + 1) / (2 * i + 1)
        return PiResponse(value=math.sqrt(8 * s))


if __name__ == '__main__':
    handler = PiHandler()
    processor = Processor(handler)
    transport = TSocket.TServerSocket(host='127.0.0.1', port=8888)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TCompactProtocol.TCompactProtocolFactory()

    server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)
    server.setNumThreads(10)
    server.deamon = True
    server.serve()
