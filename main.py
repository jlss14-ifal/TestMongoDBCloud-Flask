from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
def hello_world():
    return "<p>Hello world</p>"


@app.route("/insert_Produto")
def salvarProduto():
    
    
    if __name__ == "__main__":
         app.run()