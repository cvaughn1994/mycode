#!/usr/bin/python3

from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import render_template

app = Flask(__name__)

groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

@app.route("/")
def showgroups():
    return render_template("flashchallenge1.html", groups = groups)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
