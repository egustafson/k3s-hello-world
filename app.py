## example:  python-flask
##

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '-- Hello K3s --'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
