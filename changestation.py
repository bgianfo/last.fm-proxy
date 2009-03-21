#!/usr/bin/python

import sys
import config
import httpclient

s = httpclient.httpclient("localhost", config.listenport)
s.req("/" + sys.argv[1])

