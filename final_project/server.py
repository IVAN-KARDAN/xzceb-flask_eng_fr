from machinetranslation import translator
from flask import Flask

app = Flask("web_app")

@app.route("/")
def root():
    input = 'input.html'
    with open(input.html, 'r+') as readfile1:
        print(readfile1.read())
        readfile1.close()

@app.route("/englishToFrench")


@app.route("/frenchToEnglish")