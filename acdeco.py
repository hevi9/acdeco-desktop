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


class DesktopControl(object):
  
  def __init__(self):
    pass

class Proto(object):
  
  def __init__(self):
    pass

class BTServer(object):
  """
  Initial active.
  Looping.
  """
  
  def __init__(self):
    pass
  
  def serve_forever(self):
    pass

def main():
  server = BTServer()
  server.serve_forever()

if __name__ == "__main__": main()