from flask import Flask #Primero se importa la clase principal
from flask import render_template #Tambien se importa la carpeta que maneja los templates o plantillas, esta clase
#buscara el template deseado mediante su nombre en la carpeta templates
from flask import send_file

app = Flask(__name__) #Instancia de la clase Flask, el primer argumento es el nombre del modulo o paquete de la aplicacon

@app.route("/")
def url_principal():
	inicial="proyecto1"
	imagenes=["proyecto2","proyecto3","proyecto4","proyecto5"]
	return render_template("template.html",imagenes=imagenes,nombre="Adrián Sánchez Hernández",inicial=inicial)

@app.route("/download")
def download_file():
	archivo="static/Document/CurriculumVitaeAdrian.pdf"
	return send_file(archivo,as_attachment=True)

if __name__ == "__main__":
	app.run(debug=True)