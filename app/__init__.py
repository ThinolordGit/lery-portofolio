from flask import Flask
from flask_mail import Mail,Message
from flask_sqlalchemy import SQLAlchemy
from random import *
import os

appconfig = {}
# Configuration pour le dossier de téléversement
appconfig['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'static', 'img', 'pp')

# Assurez-vous que le dossier d'upload existe au démarrage de l'application
os.makedirs(appconfig['UPLOAD_FOLDER'], exist_ok=True)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# Configuration Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Remplacez par votre serveur SMTP
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'thinolord@gmail.com'  # Remplacez par votre email
app.config['MAIL_PASSWORD'] = 'uszgslxsbuyggees'  # Remplacez par le mot de passe de votre email
app.config['MAIL_DEFAULT_SENDER'] = 'leranciad@gmail.com'  # Remplacez par votre email

mail = Mail(app)

db = SQLAlchemy(app)

# Importez les modèles ici pour les enregistrer avec SQLAlchemy
from app.models import User

# Importez les routes ici
from app.routes import *
