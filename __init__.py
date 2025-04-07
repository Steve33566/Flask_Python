from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''
    for j in range(1):
        for i in range(1+j):
            etoiles += '1'   
        for k in range(j+1):
             for h in range(k-j):
            etoiles += '+'
        etoiles += '<br>'
    return etoiles
if __name__ == "__main__":
  app.run(debug=True)
      
   
