from flask import Flask, render_template, request, redirect
from operation import *

app = Flask(__name__)


@app.route("/update/<id>", methods=["GET", "POST"])
def update_taskid(id):
    if request.method == "POST":
        updated_task = request.form["taskal"]
        update_task(id, updated_task)
    return redirect("/")    

@app.route("/delete/<id>", methods=["GET", "POST"])
def delete(id):
    delete_task(id)
    return redirect("/")

@app.route("/done/<id>", methods=["GET", "POST"])
def update(id):
    mark_done(id)
    return redirect("/")

@app.route("/", methods=["GET", "POST"])
def render():
    if request.method=="POST":
        add_task(request.form["task"])
    data = read_json()
    return render_template("index.html", task_info=data["task"])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")