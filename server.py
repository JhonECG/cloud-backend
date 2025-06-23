from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/generate":
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            data = json.loads(body)

            response = {
                "message": "Diagrama generado correctamente",
                "type": data.get("type")
            }

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

if __name__ == "__main__":
    server = HTTPServer(('localhost', 8000), SimpleHandler)
    print("Backend corriendo en http://localhost:8000")
    server.serve_forever()