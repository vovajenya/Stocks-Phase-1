#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, CGIHTTPRequestHandler
import cgitb; cgitb.enable()  ## This line enables CGI error reporting

server = BaseHTTPRequestHandler.HTTPServer
handler = CGIHTTPRequestHandler.CGIHTTPRequestHandler
server_address = ("", 8000)
handler.cgi_directories = ["/"]

httpd = server(server_address, handler)
httpd.serve_forever()
