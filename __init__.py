from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(_name_)                                                                                                                  

@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''
    for j in range(valeur):
        for i in range(valeur-j):
            etoiles += '+'   
        for k in range(j+1):
            etoiles += '*'
        etoiles += '<br>'
    return etoiles
if _name_ == "_main_":
    app.run(debug=True)
