from flask import Flask
import random

app = Flask(__name__)
cat_breeds = ["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"]

@app.route('/cats')
def get_random_cat_breed():
    random_breed = random.choice(cat_breeds)
    return f"Случайная порода кошки: {random_breed}"

if __name__ == '__main__':
    app.run(debug=True)
