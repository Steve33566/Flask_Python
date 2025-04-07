from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/')
def formulaire():
    return '''
    <form action="/suite" method="get">
        Entrez un nombre : <input type="number" name="valeur" min="2" required>
        <input type="submit" value="Générer">
    </form>
    
if __name__ == "__main__":
  app.run(debug=True)
