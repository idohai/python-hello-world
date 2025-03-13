# from http.server import BaseHTTPRequestHandler

# class handler(BaseHTTPRequestHandler):

#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type','text/plain')
#         self.end_headers()
#         self.wfile.write(self.path.encode('utf-8'))
#         return
from sanic import Sanic
from sanic.response import json
app = Sanic()
 
 
@app.route('/')
@app.route('/<path:path>')
async def index(request, path=""):
    return json({'hello': path})
