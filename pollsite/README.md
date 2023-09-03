La tarea consiste en que usuarios se registren para realizar las encuestas 

## Instalación
Siga estos pasos para configurar y ejecutar GDYO en su entorno local:
1. Clone el repositorio:
```bash
git clone https://github.com/ivancast03/tarea
python -m venv venv
venv\Scripts\activate.bat
Instale las dependencias requeridas:
pip install -r requirements.txt
Realice las migraciones de la base de datos:
python manage.py makemigrations
python manage.py migrate
Inicie el servicio:
python manage.py runserver
El servicio estará disponible localmente en http://127.0.0.1:8000/  y listo podrá elegir entres sus encuestas
