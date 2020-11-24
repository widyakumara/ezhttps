import sys
import http.server
import socketserver
from http import HTTPStatus

HOST = '127.0.0.1'
PORT = 8888
TEXT = 'Hello world, from Python {}.{}.{}'.format(*sys.version_info)

class Handler(http.server.SimpleHTTPRequestHandler):
  def do_GET(self):
    self.send_response(HTTPStatus.OK)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(TEXT.encode('utf-8'))

print('\nServer running on http://{}:{}'.format(HOST, PORT))
httpd = socketserver.TCPServer((HOST, PORT), Handler)
httpd.serve_forever()
