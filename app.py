from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Your Full Name"  # Replace with your name
    username = os.getenv("USER")
    server_time = datetime.datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S')

    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')

    return f"""
    <h1>Name: Shivani TR</h1>
    <h2>User: shivanirgowda</h2>
    <h3>Server Time (IST): {server_time}</h3>
    <h4>TOP output:</h4>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
  
