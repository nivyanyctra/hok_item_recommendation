# app.py: Aplikasi Web Flask untuk Sistem Pakar HoK (Kompleks)

from flask import Flask, render_template, request
from inference_engine import forward_chaining
from knowledge_base import get_hero_list

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    hero_list = get_hero_list()
    if request.method == 'POST':
        my_hero = request.form['my_hero']
        enemy_heroes = [
            request.form.get('enemy1', ''),  # Allow empty for flexibility
            request.form.get('enemy2', ''),
            request.form.get('enemy3', ''),
            request.form.get('enemy4', ''),
            request.form.get('enemy5', '')
        ]
        result = forward_chaining(enemy_heroes, my_hero)
        return render_template('index.html', result=result, hero_list=hero_list)
    
    return render_template('index.html', result=None, hero_list=hero_list)

if __name__ == '__main__':
    app.run(debug=True)