from app import create_app, db
import os

app = create_app(os.environ.get('FLASK_ENV') or 'default')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
