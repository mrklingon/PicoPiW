# Based on sample code from Adafruit

import os
import time
import ssl
import wifi
import random
import socketpool
import microcontroller
from adafruit_httpserver import HTTPServer, HTTPResponse
import starships  #build a SF story
import fstory     #build a Fantasy story


#  connect to SSID
wifi.radio.connect(os.getenv('WIFI_SSID'), os.getenv('WIFI_PASSWORD'))

pool = socketpool.SocketPool(wifi.radio)

print(f"Listening on http://{wifi.radio.ipv4_address}:80")

pool = socketpool.SocketPool(wifi.radio)
server = HTTPServer(pool)
print (str(wifi.radio.ipv4_address))

@server.route("/")
def base(request):  # pylint: disable=unused-argument
    """Default reponse is building stories"""
    return HTTPResponse(body=starships.story()+"\n-----\n"+fstory.story())

# Never returns
while True:
    try:
        server.serve_forever(str(wifi.radio.ipv4_address))

    except:
        print ("oops!")
