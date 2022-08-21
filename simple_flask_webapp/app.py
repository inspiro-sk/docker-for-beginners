import os
from flask import Flask, render_template
app = Flask(__name__)

bg_color= os.environ.get('APP_COLOR')

@app.route("/")
def main():
    print(bg_color)
    return render_template('index.html', bg_color=bg_color)


@app.route('/how_are_you')
def hello():
    return 'I am good, how about yourself?'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

