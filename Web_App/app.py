from flask import Flask, render_template, request, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = "secret_final_exam"
API_URL = "http://127.0.0.1:8000"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users")
def users():
    response = requests.get(f"{API_URL}/users/")
    users = response.json() if response.status_code == 200 else []
    return render_template("users.html", users=users)

@app.route("/objects")
def objects():
    response = requests.get(f"{API_URL}/objects/")
    objects = response.json() if response.status_code == 200 else []
    return render_template("objects.html", objects=objects)

@app.route("/policies")
def policies():
    response = requests.get(f"{API_URL}/policies/")
    policies = response.json() if response.status_code == 200 else []
    return render_template("policies.html", policies=policies)

@app.post("/create_user")
def create_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    username = request.form['username']
    email = request.form['email']
    user_data = {
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "email": email
    }

    response = requests.post(f"{API_URL}/users/", json=user_data)
    if response.status_code == 200:
        flash("User created successfully", "success")
    else:
        flash("Failed to create user", "fail")
    return redirect(url_for('users'))

@app.post("/delete_user/<int:user_id>")
def delete_user(user_id):
    response = requests.delete(f"{API_URL}/users/{user_id}")
    if response.status_code == 204:
        flash("User deleted successfully", "success")
    else:
        flash("Failed to delete user", "fail")
    return redirect(url_for('users'))

@app.post("/create_object")
def create_object():
    path = request.form['path']
    object_data = {
        "path": path
    }
    response = requests.post(f"{API_URL}/objects/", json=object_data)
    if response.status_code == 200:
        flash("Object created successfully", "success")
    else:
        flash("Failed to create object", "fail")
    return redirect(url_for("objects"))

@app.post("/delete_object/<int:object_id>")
def delete_object(object_id):
    response = requests.delete(f"{API_URL}/objects/{object_id}")
    if response.status_code == 204:
        flash("Object deleted successfully", "success")
    else:
        flash("Failed to delete object", "fail")
    return redirect(url_for("objects"))

@app.post("/create_policy")
def create_policy():
    user_id = request.form["user_id"]
    object_id = request.form["object_id"]
    policy_data = {
        "user_id": user_id,
        "object_id": object_id
    }
    response = requests.post(f"{API_URL}/policies/", json=policy_data)
    if response.status_code == 200:
        flash("Policy created successfully", "success")
    else:
        flash("Failed to create policy", "fail")
    return redirect(url_for("policies"))

@app.post("/delete_policy/<int:policy_id>")
def delete_policy(policy_id):
    response = requests.delete(f"{API_URL}/policies/{policy_id}")
    if response.status_code == 204:
        flash("Policy deleted successfully", "success")
    else:
        flash("Failed to delete policy", "fail")
    return redirect(url_for("policies"))

if __name__ == "__main__":
    app.run(debug=True)
