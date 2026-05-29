from flask import Flask, make_response, request
from uuid import uuid4
from datetime import datetime

app = Flask("TaskManager")

tasks_storage = {}

@app.route("/")
def list_tasks():
    tasks = tasks_storage
    completed_flag = request.args.get("completed", "")
    if completed_flag.lower() == "true":
        tasks = {
            task_id: task_info for task_id, task_info in tasks_storage.items() if task_info["is_completed"]
        }
    elif completed_flag.lower() == "false":
        tasks = {
            task_id: task_info for task_id, task_info in tasks_storage.items() if not task_info["is_completed"]
        }
        
    return make_response(tasks, 200)

@app.post("/")
def create_task():
    task_id = uuid4().hex
    task_info = {
        "title": request.json.get("title", "Missed Title"),
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "is_completed": False
    }
    tasks_storage[task_id] = task_info
    return make_response({"task_id": task_id}, 201)

@app.put("/<task_id>")
def mark_completed(task_id):
    if task_id not in tasks_storage:            
        return make_response({"error": "Task not found."}, 404)
    
    tasks_storage[task_id]["is_completed"] = True
    return make_response({"message": "Task marked as completed."}, 200)

@app.delete("/<task_id>")
def delete_task(task_id):
    if task_id not in tasks_storage:            
        return make_response({"error": "Task not found."}, 404)
    
    del tasks_storage[task_id]
    return make_response({"message": "Task deleted."}, 200)

if __name__ == "__main__":
    app.run(debug=True)