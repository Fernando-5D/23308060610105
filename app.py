from flask import Flask, render_template, request, session
app = Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/clasificar-macro", methods=("GET", "POST"))
def clasificar():
    if request.method == "POST":
        nombre = request.form("nombre")
        grasas = request.form("grasas") * 9
        proteinas = request.form("proteinas") * 4
        carbohidratos = request.form("carbohidratos") * 4
        
        session["alimentos"]

if __name__ == "__main__":
    app.run(debug=True)
