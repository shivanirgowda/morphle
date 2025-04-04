from flask import Flask
import os
import datetime
import subprocess

app = Flask(_name_)

@app.route('/htop')
def htop():
    # Get system username
    username = os.getenv("USER") or os.getenv("USERNAME")

    # Get current time in IST
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    
    # Get top output
    top_output = subprocess.getoutput("top -b -n 1 | head -10")

    # HTML Output
    return f"""
    <html>
        <head><title>System Info</title></head>
        <body>
            <h2>Name: Your Full Name</h2>
            <h3>Username: {username}</h3>
            <h3>Server Time (IST): {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</h3>
            <pre>{top_output}</pre>
        </body>
    </html>
    """

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
