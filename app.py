from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    # Obtener los datos del formulario
    distancia = request.form['distancia']
    tiempo = request.form['tiempo']
    velocidad_maxima = request.form['velocidad_maxima']
    
    if (distancia==""):
        return render_template('index.html', mensaje="Error: Debe ingresar una distancia")
    elif(tiempo==""):
        return render_template('index.html', mensaje="Error: Debe ingresar un tiempo")
    elif(velocidad_maxima==""):
        return render_template('index.html', mensaje="Error: Debe ingresar una velocidad maxima")
    
    distancia = float(distancia)
    tiempo = float(tiempo)
    velocidad_maxima = float(velocidad_maxima)

    # Validación básica
    if distancia <= 0 or tiempo <= 0:
        return "La distancia y el tiempo deben ser valores positivos."

    # Realizar el cálculo de la velocidad
    velocidad = float(distancia / 1000) / (tiempo/60)
    porcentaje1 = float(velocidad_maxima * (porcentaje/ 100))
    velocidad_con_porcentaje = velocidad_maxima+porcentaje1

    if (velocidad < velocidad_maxima):
        estado = "OK"
    elif(velocidad < (velocidad_con_porcentaje) ):
        estado = "MULTA"
    elif(velocidad >=(velocidad_con_porcentaje) ):
        estado = "MULTA Y CURSO DE SENSIBILIZACION"
    else:
        estado = "Error"

    # Renderizar la plantilla `about.html` con los resultados
    return render_template('about.html', 
                           distancia=distancia, 
                           tiempo=tiempo, 
                           velocidad_maxima=velocidad_maxima, 
                           resultado=velocidad,
                           estado=estado,
                           velocidad_con_porcentaje=velocidad_con_porcentaje)

if __name__ == '__main__':
    app.run(debug=True)
