from flask import render_template
from . import app
import requests
owm_key = "27a415b718cef5c8f54f87b42ad67c5d"
city = "Poltava"


@app.route("/")
@app.route("/index")
def index():
    response = requests.get(f"https://alerts.com.ua/api/states/12 -H X-API-Key: 34421337")
    print(response.json())

    return render_template("index.html")