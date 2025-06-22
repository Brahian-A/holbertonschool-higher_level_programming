#!/usr/bin/env python3

import json
import http.server
import socketserver

address_port = 8000


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    with socketserver.TCPServer(("", address_port), SimpleAPIHandler) as httpd:
        print("Serving at port", address_port)
        httpd.serve_forever()
