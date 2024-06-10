from flask import Flask

app = Flask(__name__)

@app.route('/flask')
def home():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)