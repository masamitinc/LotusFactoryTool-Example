from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import datetime
import json
import csv

# Opening JSON file
f = open('config.json')

# returns JSON object as
# a dictionary
configargs = json.load(f)

TOOL_NAME = configargs['stationtype']
TOOL_VERSION = configargs['version']

app = Flask(__name__)

dt = datetime.datetime.now()
OUTPUT_FILENAME=os.path.join(app.root_path, f'{dt.year:04}{dt.month:02}{dt.day:02}-{dt.hour:02}{dt.minute:02}{dt.second:02}'+".csv")
print("Output file:", OUTPUT_FILENAME)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon_48x48.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        csv_row = []
        for i in request.form:
            # print("{}: {}".format(i, request.form[i]))
            csv_row.append(request.form[i])
        csv_row.append(TOOL_NAME)
        csv_row.append(TOOL_VERSION)
        print(csv_row)

        # Append
        with open(OUTPUT_FILENAME, 'a', newline="") as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            csvwriter.writerow(csv_row)

    return render_template('index_tx.html', configargs=configargs)


if __name__ == '__main__':
    print(TOOL_NAME, "Ver:", TOOL_VERSION)
    #app.run(debug=True, host="0.0.0.0", port="80")
    app.run()
    print("Exit")
