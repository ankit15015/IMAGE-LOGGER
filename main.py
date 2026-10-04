from http.server import BaseHTTPRequestHandler
from datetime import datetime, timezone
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        event = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "method": "GET",
            "path": self.path
        }

        # Visible in your Vercel function logs
        print(json.dumps(event))

        if self.path.startswith("/image.png"):
            # Tiny 1x1 transparent PNG
            image = bytes.fromhex(
                "89504E470D0A1A0A"
                "0000000D49484452000000010000000108060000001F15C489"
                "0000000D4944415408D763F8CFC0F01F00050001FF89993D1D"
                "0000000049454E44AE426082"
            )

            self.send_response(200)
            self.send_header("Content-Type", "image/png")
            self.send_header("Content-Length", str(len(image)))
            self.end_headers()
            self.wfile.write(image)
            return

        body = b"Image logger test endpoint"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
