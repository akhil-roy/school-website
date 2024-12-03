import os
from flask import Flask,flash , render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user
from flask_bcrypt import Bcrypt 

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config.from_object('config.DevConfig')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

hashed_password = bcrypt.generate_password_hash(app.config['ADMIN_P']).decode('utf-8')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

if not os.path.exists(app.config['UPLOAD_FOLDER_VIDEO']):
    os.makedirs(app.config['UPLOAD_FOLDER_VIDEO'])

class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.username = app.config['ADMIN_U']
        self.password = hashed_password  # In a real app, use hashed passwords

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == app.config['ADMIN_U'] and bcrypt.check_password_hash(hashed_password, password) :
            user = User(id=1)
            login_user(user)
            return redirect(url_for('gallery'))
        flash('Invalid credentials. Please try again.')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/messages')
def messages():
    return render_template('messages.html')

@app.route('/foundation')
def foundation():
    return render_template('foundation.html')

@app.route('/academics')
def academics():
    return render_template('academics.html')

@app.route('/upload/images', methods=['GET', 'POST'])
@login_required
def upload_file():
    if request.method == 'POST':
        category = request.form['category']
        if 'files' not in request.files:
            return redirect(request.url)
        files = request.files.getlist('files')
        if not os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], category)):
            os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], category))
        for file in files:
            if file.filename == '' or not allowed_file(file.filename):
                continue
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], category, filename))
        return redirect(url_for('gallery'))
    return render_template('gallery.html')

@app.route('/delete/<category>/<filename>', methods=['POST'])
@login_required
def delete_file(category, filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], category, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    return redirect(url_for('gallery'))

@app.route('/create-category/', methods=['POST'])
@login_required
def create_category():
    if request.method == 'POST':
        category = request.form['category']
        category_path = os.path.join(app.config['UPLOAD_FOLDER'], category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
        return redirect(url_for('gallery'))
    return render_template('gallery.html')

@app.route('/delete/<category>', methods=['POST'])
@login_required
def delete_category(category):
    category_path = os.path.join(app.config['UPLOAD_FOLDER'], category)
    if os.path.exists(category_path) and not os.listdir(category_path):
        os.rmdir(category_path)
    
    return redirect(url_for('gallery'))

@app.route('/gallery')
def gallery():
    categories = sorted(os.listdir(app.config['UPLOAD_FOLDER']))
    images = {}
    videos = os.listdir(app.config['UPLOAD_FOLDER_VIDEO'])
    for category in categories:
        category_path = os.path.join(app.config['UPLOAD_FOLDER'], category)
        files = os.listdir(category_path) if os.path.exists(category_path) else []
        images[category] = files
    return render_template('gallery.html', images=images, videos=videos)

@app.route('/upload/videos', methods=['POST'])
@login_required
def upload_video():
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER_VIDEO'], filename))
    return redirect(url_for('gallery'))

@app.route('/delete/<filename>')
@login_required
def delete_video(filename):
    os.remove(os.path.join(app.config['UPLOAD_FOLDER_VIDEO'], filename))
    return redirect(url_for('gallery'))

@app.route('/uploads/video/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER_VIDEO'], filename)

@app.route('/documents')
def documents(): 
    return render_template('documents.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__=="__main__":
    app.run(debug=app.config['FLASK_DEBUG'])
