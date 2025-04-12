from flask import Flask, request

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def log_request(path):
    ip = request.remote_addr
    method = request.method
    print(f"[{method}] Anfrage von {ip} auf /{path}")
    return "Logged", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)
