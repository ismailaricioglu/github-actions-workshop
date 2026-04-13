from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage
todos = []


@app.route("/")
def home():
    return jsonify({"message": "Welcome to Todo API", "version": "1.0.0"})


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)


@app.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "title is required"}), 400

    todo = {
        "id": len(todos) + 1,
        "title": data["title"],
        "completed": False
    }
    todos.append(todo)
    return jsonify(todo), 201


@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify(todo)


@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404

    data = request.get_json()
    if "title" in data:
        todo["title"] = data["title"]
    if "completed" in data:
        todo["completed"] = data["completed"]
    return jsonify(todo)


@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    global todos
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404

    todos = [t for t in todos if t["id"] != todo_id]
    return jsonify({"message": "Todo deleted"})


@app.route("/math/add")
def math_add():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    if a is None or b is None:
        return jsonify({"error": "a and b are required"}), 400
    return jsonify({"result": a + b})


@app.route("/math/multiply")
def math_multiply():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    if a is None or b is None:
        return jsonify({"error": "a and b are required"}), 400
    return jsonify({"result": a * b})


def calculate_factorial(n):
    if n < 0:
        raise ValueError("Negative numbers not allowed")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


@app.route("/utils/factorial/<int:n>")
def factorial(n):
    try:
        result = calculate_factorial(n)
        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route("/utils/palindrome")
def palindrome():
    text = request.args.get("text", "")
    if not text:
        return jsonify({"error": "text is required"}), 400
    return jsonify({"text": text, "is_palindrome": is_palindrome(text)})


if __name__ == "__main__":
    app.run(debug=True)
