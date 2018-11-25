#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import logging

logging.basicConfig(level=logging.DEBUG)

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return
  # POST
  def do_POST(self):
        # Send response status code
        self.send_response(200)

        # read post data
        content_length = int(self.headers['Content-Length'])
        x = self.rfile.read(content_length)
        self.rfile.close()
        self.log_message("Post data: %r", x)

        # Send headers
        self.send_header('Content-type','text/xml; charset="utf-8"')
        self.end_headers()

        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return



def run():
  print('starting mock sonos ...')

  ip = get_ip()
  # Server settings
  # Choose port 1400, since that is what real sonoses answer to 
  port = 1400
  server_address = (ip, port)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running sonosd on {}:{}'.format(ip, port))
  httpd.serve_forever()


run()
