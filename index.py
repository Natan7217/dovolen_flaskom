from flask import Flask, render_template

app = Flask(__name__)
PORT = 8080


@app.route('/')
@app.route('/index')
def index():
    return f"<a href=http://127.0.0.1:{PORT}/promotion_image>Перейти к рекламе</a>"


@app.route("/promotion_image")
def promotion_image():
    return render_template("base.html", title="title", username=666)


if __name__ == '__main__':
    app.run(port=PORT, host='127.0.0.1')
