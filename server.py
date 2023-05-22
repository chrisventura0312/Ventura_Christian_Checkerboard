from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", rows=8, columns=8)

@app.route('/<int:x>/<int:y>')
def checkerboard(x, y):
    return render_template("index.html", rows=x, columns=y)

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def checkerboard_colors(x, y, color1, color2):
    return render_template("index.html", rows=x, columns=y, color1=color1, color2=color2)

if __name__ == "__main__":
    app.run(debug=True)
