from flask import Flask, render_template, request

app = Flask(__name__)
PORT = 8080


@app.route('/')
@app.route('/index')
def index():
    return f"<a href=http://127.0.0.1:{PORT}/promotion_image>Перейти к рекламе</a>" \
           f"<br><a href=http://127.0.0.1:{PORT}/astronaut_selection>Перейти к анкете</a>" \
           f"<br><a href=http://127.0.0.1:{PORT}/choice/Марс>Перейти к выбору планеты (по умолчанию Марс)</a>"


@app.route("/promotion_image")
def promotion_image():
    return render_template("base.html")


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template("astro_form.html")
    elif request.method == 'POST':
        print(request.form['lname'])
        print(request.form['fname'])
        print(request.form['educ'])
        print(request.form.getlist('profession'))
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        print(request.form['accept'])
        return "Форма отправлена"


@app.route("/choice/<planet_name>")
def planet_page(planet_name):
    return render_template("planet.html", planet_name=planet_name)


if __name__ == '__main__':
    app.run(port=PORT, host='127.0.0.1')
