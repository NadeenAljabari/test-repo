from flask import Flask

app = Flask(__name__)
#tete
@app.route('/')
def home():
    return "Hello, World!"

@app.route('/health')
def health_check():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969)
