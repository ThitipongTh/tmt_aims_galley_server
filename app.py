from flask import Flask, jsonify, request

app = Flask(__name__)

_json = []

@app.route('/')
def index_welcom():
    return 'Welcome to AIMs Lab KMITL'

@app.route('/postorder', methods = ['POST', 'GET'])
def post_order():
    if request.method == 'POST':
        _jsonrequest = request.get_json(force=True)
        _seatNo = _jsonrequest['seatNo']
        _orders = _jsonrequest['orders']
        _json.append({'seatNo': _seatNo, 'orders': _orders, 'total_orders': len(_orders)})
        return 'finish_received_order'
    elif request.method == 'GET':
        return 'error_add_order'

@app.route('/getorder', methods = ['POST', 'GET'])
def get_order():
    if request.method == 'POST':
        return 'error_get_order'
    elif request.method == 'GET':
        return jsonify(Orders = _json, Total_orders = len(_json))
    
@app.route('/removeorder', methods = ['POST', 'GET'])
def remove_order():
    if request.method == 'POST':
        _removeOrder = request.get_json(force=True)
        _json.pop(_removeOrder["remove"])
        return 'already_remove_order'
    elif request.method == 'GET':
        return 'error_remove_order'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='7005', debug=True)