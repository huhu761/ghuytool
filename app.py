from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Tool ghuy đang chạy 24/24"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
