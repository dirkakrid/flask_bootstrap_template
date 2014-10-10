from flask.ext.mail import Message, Mail

def get_mail(app):
    mail = Mail()

    #app.secret_key = 'development key'

    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_PORT'] = 465
    app.config["MAIL_USERNAME"] = 'utility_email@gmail.com'
    app.config["MAIL_PASSWORD"] = 'password12345'

    mail.init_app(app)

    return mail