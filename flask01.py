from flask import Flask

app = Flask(__name__)

@app.route('/') # https://google.com.tw/
def home():
    return "Hello Python !"

app.run(port=5000)

# / = slash