from http.server import BaseHTTPRequestHandler
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Serve the index.html file
        try:
            # Get the path to index.html
            current_dir = os.path.dirname(os.path.abspath(__file__))
            index_path = os.path.join(os.path.dirname(current_dir), 'index.html')
            
            with open(index_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))
            
        except Exception as e:
            # Fallback response if index.html is not found
            fallback_html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Wallet Balance Checker Bot</title>
                <meta charset="UTF-8">
                <style>
                    body {{ font-family: Arial, sans-serif; text-align: center; padding: 50px; background: #f0f0f0; }}
                    .container {{ background: white; padding: 40px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); max-width: 600px; margin: 0 auto; }}
                    .status {{ color: #4ade80; font-weight: bold; margin: 20px 0; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>🤖 Wallet Balance Checker Bot</h1>
                    <div class="status">✅ Bot is Online</div>
                    <p>Telegram bot for checking Ethereum and Base network wallet balances.</p>
                    <p><strong>Features:</strong></p>
                    <ul style="text-align: left; display: inline-block;">
                        <li>🟦 Ethereum Mainnet support</li>
                        <li>🔵 Base Network support</li>
                        <li>🔍 Multiple address checking</li>
                        <li>⚡ No API keys required</li>
                    </ul>
                    <p><a href="https://t.me/BalanceCK_bot" target="_blank" style="background: #0088cc; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Open Bot in Telegram</a></p>
                    <hr style="margin: 30px 0;">
                    <p><strong>API Endpoint:</strong> {os.environ.get('VERCEL_URL', 'localhost')}/api/webhook</p>
                    <p><strong>Status:</strong> Online ✅</p>
                </div>
            </body>
            </html>
            """
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(fallback_html.encode('utf-8'))