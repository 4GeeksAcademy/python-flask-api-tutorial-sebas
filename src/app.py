from flask import Flask, jsonify, request   
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

# ESTO ES EL GET
@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

# ESTO ES EL POST
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)

    todos.append(request_body)
    return jsonify(todos)


# ESTO ES EL DELETE
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
# Asegúrate de que la posición sea válida
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Position out of range"}), 400
    
    # Eliminar el elemento
    del todos[position]
    
    # Retornar la lista actualizada
    return jsonify(todos)

# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)