from flask import Flask, render_template, request
from utils import get_clean_df
from predict_health import get_score
import pandas as pd
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def upload_predict():
    if request.method == "POST":
        df = get_clean_df(request.files["metaphlan2"])
        score = round(get_score(df), 2)
        return render_template("index.html", score=score)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=12000, debug=True)
