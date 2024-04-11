from flask import Flask
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/get_time/future')
def pythonProject():
    current_time = datetime.now()
    time_after_hour = current_time + timedelta(hours=1)
    return f"Точное время через час будет {time_after_hour.strftime('%H:%M:%S')}"

if __name__=="__main__":
    app.run(debug=True,port=5555)