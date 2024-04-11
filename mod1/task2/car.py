from flask import Flask
car =['Chevrolet', 'Renault', 'Ford', 'Lada','hhh']
app = Flask(__name__)

@app.route('/cars')
def pythonProject():
    return ', '.join(car)

if __name__=="__main__":
    app.run(debug=True, port=5050)