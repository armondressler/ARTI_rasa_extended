import http.server
import socketserver

PORT = 8080
DIRECTORY = "web"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.landing_page_path = "/chat.html"
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path != self.landing_page_path:
            self.send_response(302)
            self.send_header('Location', "/chat.html")
            self.end_headers()
        else:
            super().do_GET()


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving on port", PORT)
    httpd.serve_forever()