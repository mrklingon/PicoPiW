# SPDX-FileCopyrightText: 2022 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
import os
import time
import ssl
import wifi
import random
import socketpool
import microcontroller
from adafruit_httpserver import HTTPServer, HTTPResponse
from kwords import *
from words import *
from mwords import *

def mcode():
    codew = ""

    for i in range(6):
        codew = codew + " " + mwords[random.randrange(len(mwords))]
    return (codew)

def dcode():
    codew = ""

    for i in range(6):
        codew = codew + " " + words[random.randrange(len(words))]
    return (codew)
def kcode():
    codew = ""

    for i in range(6):
        codew = codew + " " + kwords[random.randrange(len(kwords))]
    return ("\"" + codew + "\"")

#  connect to SSID
wifi.radio.connect(os.getenv('WIFI_SSID'), os.getenv('WIFI_PASSWORD'))

pool = socketpool.SocketPool(wifi.radio)

print(f"Listening on http://{wifi.radio.ipv4_address}:80")

pool = socketpool.SocketPool(wifi.radio)
server = HTTPServer(pool)


@server.route("/")
def base(request):  # pylint: disable=unused-argument
    """Default reponse is /index.html"""
#    return HTTPResponse(filename="/index.html")
    return HTTPResponse(body=kcode() +"\n"+mcode() +"\n" +dcode())

# Never returns
server.serve_forever(str(wifi.radio.ipv4_address))

