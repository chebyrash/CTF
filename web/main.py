import json
import os
from flask import Flask, render_template, request

template_dir = os.path.abspath("./static/")
app = Flask(__name__, template_folder=template_dir)

file = open("states.json", "r+")
states = json.loads(file.read())


@app.after_request
def save(resp):
    file.seek(0)
    file.write(json.dumps(states))
    file.truncate()

    return resp


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/state")
def get_state():
    user = states.get(request.remote_addr, None)
    if not user:
        print("New user", request.remote_addr)
        states[request.remote_addr] = [False for _ in range(5)]
    else:
        print("Existing user")

    return json.dumps(states[request.remote_addr])


@app.route("/ch0")
def ch0():
    flag = request.args.get("FLAG")

    if flag:
        if flag.strip() == "CTF{Welcome_to_Microsoft_Windows}":
            states[request.remote_addr][0] = True

    return json.dumps(states[request.remote_addr])


@app.route("/ch1")
def ch1():
    flag = request.args.get("FLAG")

    if flag:
        if flag.strip() == "CTF{Photoshop_is_for_quitters}":
            states[request.remote_addr][1] = True

    return json.dumps(states[request.remote_addr])


@app.route("/ch2")
def ch2():
    flag = request.args.get("FLAG")

    if flag:
        if flag.strip() == "CTF{Mouse_Right_Click_to_flag}":
            states[request.remote_addr][2] = True

    return json.dumps(states[request.remote_addr])


@app.route("/ch3")
def ch3():
    flag = request.args.get("FLAG")

    if flag:
        if flag.strip() == "CTF{Clippy_Office_Assistant}":
            states[request.remote_addr][3] = True

    return json.dumps(states[request.remote_addr])


@app.route("/ch4")
def ch4():
    flag = request.args.get("FLAG")

    if flag:
        if flag.strip() == "CTF{First_MP3_Player_For_DOS}":
            states[request.remote_addr][4] = True

    return json.dumps(states[request.remote_addr])


app.run("0.0.0.0", 5000, True)
