from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def index():
    num_list, personal_info = create_info()
    if request.method == "POST":
        update_nickname = request.form['nickname']
        update_age = request.form["age"]
        update_address = request.form["address"]
        personal_info['nickname'] = update_nickname
        personal_info['age'] = update_age
        personal_info['address'] = update_address

    return render_template("flaskQ.html", send_num_list=num_list, send_personal_info=personal_info)


def create_info():
    num_list = []
    personal_info = {}
    for i in range(10):
        num_list.append(int(i))

    personal_nickname = 'KnightHardt'
    personal_age = '18'
    personal_address = 'Shanghai, China'
    personal_info['nickname'] = personal_nickname
    personal_info['age'] = personal_age
    personal_info['address'] = personal_address
    return num_list, personal_info


if __name__ == "__main__":
    # app.run( debug=True)
    app.run(port =8000, debug=True)



