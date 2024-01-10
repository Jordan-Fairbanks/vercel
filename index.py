from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "home page route"

@app.route('/calendar')
def calendar():
    return 'calendar route'

@app.route("/events")
def events():
    return "events route"

if __name__ == "__main__":
    app.run(debug=True)