import MySQLdb
import MySQLdb.cursors
from flask import Flask, render_template, json

app = Flask(__name__)

database = MySQLdb.connect(host = "localhost", 
	user = "root2",
	passwd = "LPAdmin/", 
	db = "projeto", 
	cursorclass = MySQLdb.cursors.DictCursor)
cursor = database.cursor()

@app.route("/")
def main():
	cursor.execute("SELECT name, value FROM alunos ORDER BY value DESC LIMIT 5")
	data = cursor.fetchall()
	usuario = {
		"usuario": {
			"nome": "aluno",
			"sobrenome": "sobrenome",
			"data_nascimento": data,
			"email": "e-mail"
		}
	}
	return render_template("index.html", title = "Anychart Python template", chartData = json.dumps(usuario))

if __name__ == "__main__": 
	app.run()