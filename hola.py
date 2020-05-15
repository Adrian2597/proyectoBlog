from flask import Flask #Primero se importa la clase principal
from flask import render_template #Tambien se importa la carpeta que maneja los templates o plantillas, esta clase
#buscara el template deseado mediante su nombre en la carpeta templates

app = Flask(__name__) #Instancia de la clase Flask, el primer argumento es el nombre del modulo o paquete de la aplicacon

@app.route("/curriculum/Adrian")
def url_principal():
	return render_template("template.html",nombre="Adrián Sánchez Hernández")

if __name__ == "__main__":
	app.run(debug=True)