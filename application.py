from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Hacer una solicitud HTTP para obtener los datos del seguro
    response = requests.get('https://dn8mlk7hdujby.cloudfront.net/interview/insurance/58')
    
    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        data = response.json()
        
        # Acceder a los datos del seguro
        name = data['insurance']['name']
        description = data['insurance']['description']
        price = data['insurance']['price']
        image = data['insurance']['image']
        
        # Renderizar la plantilla HTML con los datos
        return render_template('index.html', name=name, description=description, price=price, image=image)
    else:
        # Manejar el caso de error
        return "Error al obtener los datos del seguro"

if __name__ == '__main__':
    app.run(debug=True)