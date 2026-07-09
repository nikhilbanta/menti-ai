#!/usr/bin/env python3
import http.server
import socketserver
import os

os.chdir('/mnt/d/mfapp/menti-ai')
PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

print(f"Starting server on http://0.0.0.0:{PORT}")
print(f"Access from mobile: http://172.24.234.241:{PORT}")

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print("Server running. Press Ctrl+C to stop.")
    httpd.serve_forever()
