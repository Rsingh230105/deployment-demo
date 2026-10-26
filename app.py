from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            response = {
                "status": "healthy",
                "application": "deployment-demo"
            }
            self.send_response(200)
        else:
            response = {
                "message": "Python application is running"
            }
            self.send_response(200)

        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())


server = HTTPServer(("0.0.0.0", 8000), AppHandler)

print("Application running on port 8000", flush=True)
server.serve_forever()
