import datetime
from flask import Flask
app = Flask(__name__)

@app.route('/get_time/now')
def pythonProject():
    return 'Это тестовая страница, ответ сгененрирован в %s'% \
    datetime.datetime.now().utcnow()

if __name__=="__main__":
    app.run(debug=True,port=5555)