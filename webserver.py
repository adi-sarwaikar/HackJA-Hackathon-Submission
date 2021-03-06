from flask import Flask, render_template, request
from sourceFinder import main_function

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        query = request.form["query"]
        sourcesList = main_function(query)
        sourceString =""
        for source in sourcesList:
            sourceString = sourceString + source +"\n"
        return "<!DOCTYPE html> <head> <title>Source Search - Easy Way To Find Sources</title> <style> * { margin: 0; padding: 0; box-sizing: border-box; } body { font-family: \"Roboto\", Helvetica, Arial, sans-serif; font-weight: 100; font-size: 12px; line-height: 30px; color: #777; background-image: url(background.jpg); } .container { max-width: 400px; width: 100%; margin: 0 auto; position: relative; } #query input[type=\"text\"], #query button[type=\"submit\"] { font: 400 12px/16px \"Roboto\", Helvetica, Arial, sans-serif; } #query { background: #F9F9F9; padding: 25px; margin: 150px 0; box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24); } #query h3 { display: block; font-size: 30px; font-weight: 300; margin-bottom: 10px; } #query h4 { margin: 5px 0 15px; display: block; font-size: 13px; font-weight: 400; } fieldset { border: medium none !important; margin: 0 0 10px; min-width: 100%; padding: 0; width: 100%; } #query input[type=\"text\"]{ width: 100%; border: 1px solid #ccc; background: #FFF; margin: 0 0 5px; padding: 10px; } #query input[type=\"text\"]:hover{ -webkit-transition: border-color 0.3s ease-in-out; -moz-transition: border-color 0.3s ease-in-out; transition: border-color 0.3s ease-in-out; border: 1px solid #aaa; } #query button[type=\"submit\"] { cursor: pointer; width: 100%; border: none; background: #4995c2; color: #FFF; margin: 0 0 5px; padding: 10px; font-size: 15px; } #query button[type=\"submit\"]:hover { background: #4CAF50; -webkit-transition: background 0.3s ease-in-out; -moz-transition: background 0.3s ease-in-out; transition: background-color 0.3s ease-in-out; } #query button[type=\"submit\"]:active { box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.5); } #query input:focus{ outline: 0; border: 1px solid #aaa; } ::-webkit-input-placeholder { color: #888; } :-moz-placeholder { color: #888; } ::-moz-placeholder { color: #888; } :-ms-input-placeholder { color: #888; } </style> </head> <body translate=\"no\" data-new-gr-c-s-check-loaded=\"14.991.0\" data-gr-ext-installed=\"\"> <div class=\"container\"> <form id=\"query\" action=\"#\" method=\"post\"> <h3>Source Search</h3> <p>"+sourceString+"</p> </form> </div>"
    else:
        return render_template('main.html')

if __name__ == '__main__':
    app.run()