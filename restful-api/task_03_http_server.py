import http.server
import socketserver
import json

class httpreq(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            massge = "Hello, this is a simple API!"
            self.wfile.write(massge.encode())
        elif self.path == "/data":
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            massge = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(massge).encode())
        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            massge = "OK"
            self.wfile.write(massge.encode())
        elif self.path == "/info":
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            massge = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(massge).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            massge = "Endpoint not found"
            self.wfile.write(massge.encode())

if __name__ == "__main__":
    PORT = 8000
    with socketserver.TCPServer(("", PORT), httpreq) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
