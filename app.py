from flask import Flask, redirect, render_template, request
import checker
import os

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")



@app.route('/check', methods=['GET', 'POST'])
def check():
    if request.method == 'POST':
        code=request.form['code']
        # print(code)
        code1 = checker.Checker(code)
        symDub = code1.getSymbolDuplicates()
        charDub = code1.getCharachterDuplicates()
    return render_template("index.html", symbols=symDub, characters=charDub)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
