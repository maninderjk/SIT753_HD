from flask import Flask, request, jsonify, abort
from models import Task
from storage import load_tasks, save_tasks
from utils import get_current_timestamp

app = Flask(__name__)
tasks = load_tasks()

@app.route('/')
def health_check():
    return "OK", 200

@app.route('/tasks', methods=['GET'])
def list_tasks():
    return jsonify([task.to_dict() for task in tasks]), 200

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Task 'name' is required"}), 400

    new_task = Task(name=data['name'])
    tasks.append(new_task)
    save_tasks(tasks)
    return jsonify(new_task.to_dict()), 201

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    for task in tasks:
        if task.id == task_id:
            return jsonify(task.to_dict()), 200
    return jsonify({"error": "Task not found"}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    save_tasks(tasks)
    return jsonify({"message": f"Task {task_id} deleted"}), 200

@app.route('/tasks/<int:task_id>', methods=['PATCH'])
def update_task_status(task_id):
    data = request.get_json()
    if not data or 'status' not in data:
        return jsonify({"error": "'status' field is required"}), 400

    for task in tasks:
        if task.id == task_id:
            task.status = data['status']
            task.updated_at = get_current_timestamp()
            save_tasks(tasks)
            return jsonify(task.to_dict()), 200
    return jsonify({"error": "Task not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

