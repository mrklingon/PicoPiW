# SPDX-FileCopyrightText: 2022 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
import os
import time
import ssl
import wifi
import socketpool
import microcontroller
from adafruit_httpserver import HTTPServer, HTTPResponse


#  connect to SSID
wifi.radio.connect(os.getenv('WIFI_SSID'), os.getenv('WIFI_PASSWORD'))

pool = socketpool.SocketPool(wifi.radio)

print(f"Listening on http://{wifi.radio.ipv4_address}:80")

pool = socketpool.SocketPool(wifi.radio)
server = HTTPServer(pool)


@server.route("/")
def base(request):  # pylint: disable=unused-argument
    """Default reponse is /index.html"""
    return HTTPResponse(filename="/index.html")


# Never returns
server.serve_forever(str(wifi.radio.ipv4_address))
