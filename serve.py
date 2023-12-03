# serve.py

from waitress import serve
from lab.wsgi import application

if __name__ == "__main__":
    print('Сервер запущено через Waitress!')
    serve(application, host='0.0.0.0', port=8000)
