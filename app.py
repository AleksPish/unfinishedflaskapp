from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return '<h1>Here is some BOLD text that is changed.</h1>'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')