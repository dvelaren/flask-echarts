from flask import Flask, render_template, request, url_for, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

# Create echarts time series mockup data
data = [
    ["2019-01-01", 10],
    ["2019-01-02", 20],
    ["2019-01-03", 30],
    ["2019-01-04", 40],
    ["2019-01-05", 50],
    ["2019-01-06", 60],
    ["2019-01-07", 70],
    ["2019-01-08", 80],
    ["2019-01-09", 90],
    ["2019-01-10", 100],
]


@app.route("/")
def home():
    return render_template("index.html", data=data)


@app.route("/data")
def get_data():
    global data
    new_date = datetime.strptime(data[-1][0], "%Y-%m-%d") + timedelta(days=1)
    data.append(
        [
            new_date.strftime("%Y-%m-%d"),
            data[-1][1] + 10,
        ]
    )
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
