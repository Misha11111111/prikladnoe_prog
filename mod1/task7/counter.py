from flask import Flask
counter = 0
app = Flask(__name__)

@app.route('/counter')
def count():
    global counter
    counter += 1
    return 'Количество посещений =%s' % str(counter)

if __name__=="__main__":
    app.run(debug=True, port=8888)