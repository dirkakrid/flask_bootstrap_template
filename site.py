from flask import Flask, request, jsonify, render_template
from flask import app, safe_join, send_from_directory
from flask.ext.mail import Mail, Message
from pyslack import SlackClient

app = Flask(__name__)

slack_token = ""

slack_client = SlackClient(slack_token)


@app.route('/<any(css, img, js, sound):folder>/<path:filename>')
def toplevel_static(folder, filename):
    """
    Route resource requests to static directories
    """
    filename = safe_join(folder, filename)
    cache_timeout = app.get_send_file_max_age(filename)
    return send_from_directory(app.static_folder, filename,
                               cache_timeout=cache_timeout)

@app.route('/', methods = ['GET'])
def main_page():
    """
    Render the main page
    """
    return render_template("index.html")


@app.route('/contact_form', methods = ['POST'])
def contact():
    """
    Process contact requests
    """
    name = request.form['name']
    phone = request.form['phone']
    message = request.form['message']
    email = request.form['email']

    content = "\n\n".join([name, email, phone, message])

    print name, phone, email, message

    slack_client.chat_post_message('#site_contact', content, username=email)

    return str(200)

if __name__ == '__main__':
    app.run(debug=True)