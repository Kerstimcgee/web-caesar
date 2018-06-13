from flask import Flask, request, redirect
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>Rotate it!</title>
        <style> 
        form {
            background-color: #eee;
            padding: 20px;
            margin: 0 auto;
            width: 540px;
            font: 16px sans-serif;
            border-radius: 10px;
            }
        textarea {
            margin: 10px 0;
            width: 540px;
            height: 120px;
            }
        </style>
    </head>
    <body>
"""
add_form = """
    <form action="/rotate" method="post">
        <label>
            Rotate by:
            <input type="number" name="rot" value="0"/>
        </label>
        <br>
            <textarea name="some_text_to_rot" form="user_form">Enter text here</textarea> 
        <br>
            <input type="submit" value="Submit Query"/>  
    </body>
</html>
"""

@app.route("/")
def index():
    content = add_form + page_header
    return content
    
app.run()

#@app.route("/rotated")



