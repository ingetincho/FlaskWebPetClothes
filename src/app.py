from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL

#instanciamos las clases

app = Flask(__name__)
mysql = MySQL()


if __name__ == "main":
    app.run(debug=True)   #Para correr flask


