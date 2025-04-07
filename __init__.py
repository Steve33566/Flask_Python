from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''
    for j in range(1):
        for i in range(1+j):   
        for k in range(j+1):
            etoiles += '1'
        etoiles += '<br>'
    return etoiles
if __name__ == "__main__":
  app.run(debug=True)
      
   
