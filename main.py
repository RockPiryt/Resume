from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/info')
def info_project():
    return render_template("info_project.html")

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port="5000")