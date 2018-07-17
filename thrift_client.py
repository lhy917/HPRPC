# coding: utf-8
# thrift_client.py

import sys

from thrift.transport import TSocket, TTransport
from thrift.protocol import TCompactProtocol

from pi.PiService import Client
from pi.ttypes import PiRequest, IllegaArgument


if __name__ == '__main__':
    sock = TSocket.TSocket('127.0.0.1', 8888)
    transport = TTransport.TBufferedTransport(sock)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = Client(protocol)

    transport.open()
    for i in range(10):
        try:
           res = client.cal(PiRequest(n=i))
           print('pi(%d) = %f' % (i, res.value))
        except IllegaArgument as ia:
            print('pi(%d) %s' % (i, ia.message))
    transport.close()
