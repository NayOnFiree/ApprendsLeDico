from flask import Flask, render_template, url_for
import random
from larousse_api import larousse

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    mot_a_trouver = random.choice(open('liste_francais.txt').readlines())
    mot_a_trouver = mot_a_trouver[:len(mot_a_trouver)-1]

    larousse_def = larousse.get_definitions(mot_a_trouver)
    if not larousse_def:
        larousse_def = ['aucune définition']

    return render_template('index.html', mot_a_trouver=mot_a_trouver, resultat=larousse_def)

if __name__ == '__main__':
    app.run(debug=True)
