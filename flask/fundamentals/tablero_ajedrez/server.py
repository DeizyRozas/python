from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def tablero_default():
    return render_template("index.html", columnas=8, filas= 8)

@app.route('/<int:filas>')
def tablero(filas):
    return render_template("index.html", columnas=8, filas= filas)

@app.route('/<int:columnas>/<int:filas>')
def tablero_personalizado(columnas,filas):
    return render_template("index.html", columnas=columnas, filas= filas)


#COLORES ALTERNOS 
# @app.route('//')
# def tablero_alterno(color):
#     return render_template("index.html", columnas=8, filas= 8,color=1)




if __name__=="__main__":
    app.run(debug=True)