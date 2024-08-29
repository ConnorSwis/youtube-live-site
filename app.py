import os
from dotenv import load_dotenv
from http.server import SimpleHTTPRequestHandler, BaseHTTPRequestHandler
import socketserver


load_dotenv()

channel_id = os.getenv("YOUTUBE_CHANNEL_ID")
assert channel_id is not None, "Please set CHANNEL_ID in .env file"

html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Live Webcam Feed</title><style>body{{font-family:Arial,sans-serif;background-color:#f0f0f0;display:flex;justify-content:center;align-items:center;height:100vh;margin:0}}.card{{width:100%;max-width:768px;background-color:#fff;border-radius:8px;box-shadow:0 4px 8px rgba(0,0,0,.1);overflow:hidden;margin:0 auto}}.card-header{{padding:20px;border-bottom:1px solid #e0e0e0}}.card-title{{font-size:1.5rem;margin:0;color:#333}}.card-description{{font-size:1rem;color:#666}}.card-content{{padding:20px}}.video-wrapper{{position:relative;width:100%;padding-top:56.25%}}.video-wrapper iframe{{position:absolute;top:0;left:0;width:100%;height:100%;border:none;border-radius:6px}}</style></head><body><div class="card"><div class="card-content"><div class="video-wrapper"><iframe src="https://youtube.com/embed/live_stream?channel={channel_id}&autoplay=1&mute=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div></div></div></body></html>"""


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())


port = int(os.getenv("PORT", 8000))

with socketserver.TCPServer(("", port), SimpleHTTPRequestHandler) as httpd:
    print(f"Serving at port {port}")
    httpd.serve_forever()
