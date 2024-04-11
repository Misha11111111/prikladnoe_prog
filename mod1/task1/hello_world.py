from flask import Flask
app = Flask(__name__)

@app.route('/hello_world')
def pythonProject():
    return "Привет, мир!"

if __name__=="__main__":
    app.run(debug=True, port=8080)