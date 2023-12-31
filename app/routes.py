from flask import render_template, request, jsonify
from app import app, db, appconfig, os,randint, Message, mail
from app.models import *
import html

def generateUnique (length: int)->str:
    chains = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    uniqy = ""
    for i in range(length):
        uniqy += chains[randint(0,(len(chains)-1))]
    return uniqy
    
    
# Créez la table lors du lancement de l'application
with app.app_context():
    db.drop_all()
    db.create_all()


@app.route('/')
def index():
     # Récupérez tous les utilisateurs de la base de données
    users = User.query.all()
    posts = UserPost.query.all()
    # for dex,user in enumerate(users) :
    #     # Récupérer un utilisateur en fonction de son email
    #     user_infos = User.query.filter_by(email=user.email).first()
    return render_template('index.html', users=users, metaUser = User,metaPost = UserPost,posts = posts)


@app.route('/process_form', methods=['POST'])
def process_form():
    uname = html.escape(request.form.get('uname'))
    uprename = html.escape(request.form.get('uprename'))
    umail = html.escape(request.form.get('umail'))
    uctt = html.escape(request.form.get('ucontent'))
    filepp = ""
    print (request.files)
    if 'pp' in request.files:
        file = request.files['pp']
        

        if not file.filename == '':
            # Vous pouvez enregistrer le fichier ou effectuer d'autres traitements ici
            # par exemple, sauvegarder le fichier dans le dossier 'uploads'
            # Générez un nom de fichier unique à l'aide de votre fonction
            filename = generateUnique(20)  # Changez la longueur selon vos besoins

            # Ajoutez l'extension du fichier d'origine au nom généré
            _, file_extension = os.path.splitext(file.filename)
            filename_with_extension = f"{filename}{file_extension}"

            # Chemin complet du fichier
            filepath = os.path.join(appconfig['UPLOAD_FOLDER'],filename_with_extension)
            print(filepath)
            # Enregistrez le fichier avec le nouveau nom
            file.save(filepath)
            filepp = "/static/img/pp/"+filename_with_extension

    # Crée un nouvel utilisateur avec les données du formulaire
    new_user = User(username=uname, userprename=uprename,email=umail,pp = filepp)
    

    # Ajoute l'utilisateur à la session et commit dans la base de données
    try:
        db.session.add(new_user)
        db.session.commit()
        try:
            uid = new_user.id
            new_post = UserPost(uid = uid,username=uname, userprename=uprename,ucontent = uctt,email = umail,pp = filepp)
                
            db.session.add(new_post)
            db.session.commit()
            
            great_subject = 'Remerciement'
            great_body = 'Merci de nous avoir laisser votre avis!'
            
            u_subject = 'Nouvel Avis'

            msg = Message(great_subject, recipients=[umail])
            msg.sender = app.config['MAIL_DEFAULT_SENDER']
            msg.body = great_body
            
            u_msg = Message(u_subject, recipients=['leranciad@gmail.com'])
            u_msg.sender = umail
            u_msg.body = uctt
            
            mail.send(u_msg)
            mail.send(msg)
            return jsonify({'result': f'Vous avis : {uctt} vient d\'être posté'})
        except Exception as er:
            db.session.rollback()
            return jsonify({'error': f'Erreur lors de l\'ajout du post : {str(er)}'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Erreur lors de l\'ajout de l\'utilisateur : {str(e)}'})
