import http.server
import socketserver
import webbrowser
import os

# 设置端口
PORT = 11451

# 获取当前目录
current_dir = os.getcwd()

# 创建一个简单的HTTP服务器
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print(f"服务器启动在 http://localhost:{PORT}")
print(f"在浏览器中打开 http://localhost:{PORT}/index.html")
print("按 Ctrl+C 停止服务器")

# 自动在浏览器中打开
webbrowser.open(f"http://localhost:{PORT}/index.html")

# 启动服务器
httpd.serve_forever()