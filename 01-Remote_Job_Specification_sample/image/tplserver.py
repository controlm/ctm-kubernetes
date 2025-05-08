# tplserver.py

from flask import Flask, request, render_template
import json

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def home():
    return "Job Spec template server is running!\n"

@app.route("/jobspec/<Specfile>")
def jobs(Specfile):
  context = request.args
  return render_template(Specfile, **context)


if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)

