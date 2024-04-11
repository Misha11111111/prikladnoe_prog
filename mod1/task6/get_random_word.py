import random
from flask import Flask

app = Flask(__name__)

# Маршрут для вывода случайного слова из книги "Война и мир"
@app.route('/get_random_word')
def get_random_word():
    try:
        with open('war_and_peace.txt', 'r', encoding='utf-8') as file:
            words = file.read().split()
            random_word = random.choice(words)
            return f"Случайное слово из книги 'Война и мир': {random_word}"
    except FileNotFoundError:
        return "Файл 'Война и мир' не найден."
    except Exception as e:
        return f"Произошла ошибка: {e}"

if __name__ == '__main__':
    app.run(debug=True)
