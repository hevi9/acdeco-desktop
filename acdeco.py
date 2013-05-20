#!/usr/bin/env python2.7
## -*- coding: utf-8 -*-
## Copyright (C) 2013 Petri Heinilä, License LGPL 2.1
"""
acdeco desktop part control
===========================
"""

import logging
log = logging.getLogger(__name__)
D = log.debug
import bluetooth as bt
import subprocess as sp

SERVICE = "ACDECO"
UUID = "350da82e-c15a-11e2-949e-001e4fbfb714"
#UUID = "00001101-0000-1000-8000-00805F9B34FB"


class DesktopControl(object):
  
  def __init__(self):
    pass

class Proto(object):
  
  def __init__(self, socket):
    self._socket = socket
    self._control = DesktopControl()

  def communicate_to_end(self):
    self._socket.send("H")
    try:
      while True:
        D("Receiving data ..")
        data = self._socket.recv(1) # BLOCK
        if len(data) == 0:
          D("Connection close")
          break
        D("DATA: %d" % ord(data[0]))
    except IOError, ex:
      D("Exception %s" % str(ex))

class BTServer(object):
  """
  Initial active.
  Looping.
  """
  
  def __init__(self):
    self._server_socket = s = bt.BluetoothSocket(bt.RFCOMM)
    s.bind(("",bt.PORT_ANY))
    s.listen(5)
    self._port = s.getsockname()[1]
    D("Advertising service %s" % SERVICE)
    bt.advertise_service(s,SERVICE,
      service_id = UUID,
      service_classes = [UUID, bt.SERIAL_PORT_CLASS],
      profiles = [bt.SERIAL_PORT_PROFILE]
      )
  
  def serve_forever(self):
    while True:
      D("Waiting new RFCOMM connection on channel %d" % self._port)
      conn_sock, conn_info = self._server_socket.accept() # BLOCK
      D("New connction from %s" % conn_info[0])
      proto = Proto(conn_sock)
      proto.communicate_to_end() # BLOCK

def main():
  logging.basicConfig(level=logging.DEBUG)
  server = BTServer()
  server.serve_forever()

if __name__ == "__main__": main()