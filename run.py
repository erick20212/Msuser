# run.py
from src.app import create_app

app = create_app()

if __name__ == '__main__':
    # Cambia el host a '0.0.0.0' para que Flask sea accesible fuera del contenedor
    app.run(debug=True, host='0.0.0.0', port=5000)