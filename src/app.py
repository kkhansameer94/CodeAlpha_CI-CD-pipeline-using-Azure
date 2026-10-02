from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {
            "status": "success",
            "message": "CodeAlpha Azure CI/CD Pipeline Running",
            "deployed_via": "Azure App Service",
            "container_registry": "Azure Container Registry (ACR)"
        }
        self.wfile.write(json.dumps(response).encode('utf-8'))

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), SimpleHandler)
    print("Server running on port 8080...")
    server.serve_forever()
