from flask import Flask, render_template, request

app = Flask(__name__)
registros=[]
frutas=[]
@app.route('/', methods=["GET", "POST"])
def principal():
   # frutas = ["Morango","Uva","Laranja","Mamão","Maça"]
    
    if request.method == "POST":
        if request.form.get("fruta"):
            frutas.append(request.form.get("fruta"))
    return render_template("index.html",frutas=frutas)

@app.route('/sobre', methods=["GET","POST"])
def sobre():
   #notas = {"Deby":10.0,"Rafa":6.0,"Miguel":5.0,"Rita":9.0}
    if request.method == 'POST':
        if request.form.get("aluno") and request.form.get("nota"):
            registros.append({"aluno":request.form.get("aluno"),"nota": request.form.get("nota")})
    return render_template("sobre.html", registros=registros)

if __name__=="__main__":
    app.run(debug=True)