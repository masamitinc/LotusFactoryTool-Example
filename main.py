from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import datetime

TOOL_NAME="Lotus Factory Tool for TX"
TOOL_VERSION="00.00.01"

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon_48x48.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        dt = datetime.datetime.now()
        print("{}, VISLED:{}, IR:{}, BUTTON:{}, BarCode1:{}, BarCode2:{}".format(
            str(dt),
            request.form['result_visled'],
            request.form['result_irled'],
            request.form['result_button'],
            request.form['TextBarCode_1'],
            request.form['TextBarCode_2']))

    return render_template('index_tx.html')


if __name__ == '__main__':
    print(TOOL_NAME, "Ver:", TOOL_VERSION)
    #app.run(debug=True, host="0.0.0.0", port="80")
    app.run()
    print("Exit")