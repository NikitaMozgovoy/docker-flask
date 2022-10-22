from flask import Flask
import os
import socket

app = Flask(__name__)


@app.route('/')
def hello():
    name = os.getenv("NAME", 'world')
    hostname = socket.gethostname()

    html = f"""
    <h1>Hello, {name}!</h1> 
    <b>Hostname:</b> {hostname} <br>
    """
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    # app.run(host='127.0.0.1', port=80)
