import json
import socket
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class ReportApiHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        responseData = {
            "message": "Hallo van report-api",
            "hostname": socket.gethostname(),
        }
        responseBody = json.dumps(responseData).encode()

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(responseBody)


ThreadingHTTPServer(("0.0.0.0", 8080), ReportApiHandler).serve_forever()