from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

# In-memory storage for to-do items
todo_list = []

# Routes
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", todos=todo_list)

@app.route("/add", methods=["POST"])
def add_todo():
    task = request.form.get("task")
    if task:
        new_task = {"id": len(todo_list) + 1, "task": task}
        todo_list.append(new_task)
    return redirect("/")

@app.route("/delete/<int:todo_id>", methods=["GET"])
def delete_todo(todo_id):
    global todo_list
    todo_list = [todo for todo in todo_list if todo["id"] != todo_id]
    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)
