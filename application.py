from http.server import BaseHTTPRequestHandler, HTTPServer


class DevOpsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        response = """Hello from DevOps Pipeline!
Version 2 of the application
"""

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(response.encode())

    def log_message(self, format, *args):
        return


server = HTTPServer(("0.0.0.0", 8080), DevOpsHandler)

print("DevOps Pipeline application listening on port 8080", flush=True)

server.serve_forever()
