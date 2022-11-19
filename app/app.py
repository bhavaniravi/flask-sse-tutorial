from flask import Flask, render_template, Response
from flask_sse import sse
import time
import redis

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://127.0.0.1:6379"
app.register_blueprint(sse, url_prefix="/stream")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello/<message>")
def publish_hello(message):
    sse.publish({"message": message}, type="greeting")
    return "Message sent!"
