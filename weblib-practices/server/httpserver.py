from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

port = 8888

class MyHttpRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        print(self.path)

        result = urlparse(self.path)
        print(result)

        if result.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset = utf-8')
            self.end_headers()
            self.wfile.write('<h1>Welcome to Main Page!</h1>'.encode('utf-8'))

        elif result.path == 'board':
            params = parse_qs(result.quesry)
            print(params)
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset = utf-8')
            self.end_headers()
            self.wfile.write('''
<!DOCTYPE html>
<html lang = "en"
<head>
    <meta charset = "UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>Hello World</h1>
</body>
</html>

'''.encode('utf-8'))


http = HTTPServer(('0.0.0.0', port), MyHttpRequestHandler)
print(f'Server Running on Port{port}')
http.serve_forever()
