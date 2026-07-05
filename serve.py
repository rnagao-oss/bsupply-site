import os
os.chdir("/tmp/bsupply-cinema")
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
ThreadingHTTPServer(("0.0.0.0", 4523), SimpleHTTPRequestHandler).serve_forever()
