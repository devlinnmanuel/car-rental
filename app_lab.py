from flask import Flask,request

app = Flask(__name__)

@app.route('/hello')
def index():
    res = {'message': 'tes Hello, IBDA'}
    return res
    # return "Hello, IBDA"

@app.route('/say')
def say():
    name = request.args.get('name')
    age = request.args.get('age')
    res = {'message': f'tes Hello, {name} with {age} year(s)'}
    return res

@app.route('/say-hello/<string:name>')
def sayHello(name):
    # name = request.args.get('name')
    age = request.args.get('age')
    res = {'message': f'tes Hello, {name} with {age} year(s)'}
    return res

@app.route('/messages', methods=['POST'])
def createMessage():
    data = request.get_json()

    if data['id'] == 0:
        return {
            'status': 'ERROR',
            'message': 'Invalid ID Message'
        }

    result = {
        'status': 'OK',
        'data': data
    }

    return result


if __name__ == "__main__":
    app.run()