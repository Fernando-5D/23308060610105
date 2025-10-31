from flask import Flask, render_template, request
app = Flask(__name__)

alimentos = []

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/clasificar-macro", methods=("GET", "POST"))
def clasificar():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        grasas = float(request.form.get("grasas"))
        proteinas = float(request.form.get("proteinas"))
        carbs = float(request.form.get("carbohidratos"))
        totalCal = (grasas * 9) + (proteinas * 4) + (carbs * 4)
        
        clasif = ""
        if grasas > proteinas:
            clasif = "Grasas"
        elif proteinas > carbs:
            clasif = "Proteínas"
        elif carbs > grasas:
            clasif = "Carbohidratos"
        
        predom = 0
        tmp = [grasas, proteinas, carbs]
        for m in tmp:
            if m > predom:
                predom = m
        predom = predom * 100 / totalCal
        
        alimentos.append({
            "nombre": nombre,
            "totalCal": totalCal,
            "clasif": clasif,
            "predom": predom,
            "grasas": grasas,
            "proteinas": proteinas,
            "carbs": carbs
        })
        
        return render_template("resultado.html", nombre=nombre, totalCal=totalCal, clasif=clasif, predom=predom, grasas=grasas, proteinas=proteinas, carbs=carbs)
        
@app.route("/listaAlimentos")
def lista():
    return render_template("lista.html")

if __name__ == "__main__":
    app.run(debug=True)
