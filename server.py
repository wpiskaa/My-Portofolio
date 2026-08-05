import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", 10000))

class PortfolioHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with socketserver.TCPServer(("", PORT), PortfolioHandler) as httpd:
        print(f"Server running on port {PORT}")
        httpd.serve_forever()
