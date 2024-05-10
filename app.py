from flask import Flask, render_template, request, redirect, url_for, session
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, template_folder='templates')

app.secret_key = "training"

# Configuração do banco de dados
engine = create_engine('postgresql://lp:training@localhost/postgres')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

Base.metadata.create_all(engine)

# Conexão com o banco de dados
Session = sessionmaker(bind=engine)
db_session = Session()

# Rota da tela de login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = db_session.query(User).filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid email or password.')

    return render_template('login.html', error=None)

# Rota do dashboard após login bem-sucedido
@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    # Lógica do dashboard aqui
    return "Welcome to the Dashboard!"

# Rota para logout
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)


