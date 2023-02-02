from datetime import datetime

from app import db


class Galary(db.Model): #Галарея
    __tablename__ = 'galary'

    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(100), nullable=False)
    
    

class About(db.Model): #О нас
    __tablename__ = 'about'

    id = db.Column(db.Integer, primary_key=True)

    meta_description = db.Column(db.Text)
    meta_keywords = db.Column(db.Text)
    
    text = db.Column(db.Text)
    ru_text = db.Column(db.Text)
    en_text = db.Column(db.Text)
    
    address = db.Column(db.String(100))
    ru_address = db.Column(db.String(100))
    en_address = db.Column(db.String(100))

    phone = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255))
    instagram = db.Column(db.String(255))
    telegram = db.Column(db.String(255))
    youtube = db.Column(db.String(255))


class Division(db.Model): #Отделения
    __tablename__ = 'division'
    id = db.Column(db.Integer, primary_key=True)

    svg_icon = db.Column(db.Text)

    name = db.Column(db.Text, nullable=False)
    ru_name = db.Column(db.Text, nullable=False)
    en_name = db.Column(db.Text, nullable=False)

    personal = db.relationship('Personal', backref='personal', lazy='dynamic')
    services = db.relationship('Services', backref='services', lazy='dynamic')

    def __repr__(self):
        return f"<{self.name} >"


class Position(db.Model): #Должность
    __tablename__ = 'position'

    id = db.Column(db.Integer, primary_key=True)

    meta_description = db.Column(db.Text)
    meta_keywords = db.Column(db.Text)
    
    post = db.Column(db.String(100), nullable=False)
    ru_post = db.Column(db.String(100), nullable=False)
    en_post = db.Column(db.String(100), nullable=False)

    personal = db.relationship('Personal', backref='personal_', lazy='dynamic')
    # templates = db.relationship() #Шаблоны
    
    def __repr__(self):
        return f"<{self.post} >"


class Personal(db.Model): #Персонал
    __tablename__ = 'personal'

    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(100), nullable=False)
    ru_name = db.Column(db.String(100), nullable=False)
    en_name = db.Column(db.String(100), nullable=False)
    
    surname = db.Column(db.String(100), nullable=False)
    ru_surname = db.Column(db.String(100), nullable=False)
    en_surname = db.Column(db.String(100), nullable=False)
    
    fullname = db.Column(db.String(100))
    ru_fullname = db.Column(db.String(100))
    en_fullname = db.Column(db.String(100))
    
    personal_id = db.Column(db.Integer, nullable=False)

    number = db.Column(db.String(50), nullable=False)
    telegram = db.Column(db.String(50), nullable=False)
    instagram = db.Column(db.String(50), nullable=False)

    еxperience = db.Column(db.String(255)) #Стаж
    image = db.Column(db.String(255)) #Стаж
    birth_date = db.Column(db.DateTime)
    created_date = db.Column(db.DateTime, default = datetime.utcnow())
    updated_date = db.Column(db.DateTime)

    login = db.Column(db.String(50), nullable=False)
    psw = db.Column(db.String(50), nullable=False)

    is_doctor = db.Column(db.Boolean(), default=True)

    position = db.Column(db.Integer, db.ForeignKey('position.id'))
    division = db.Column(db.Integer, db.ForeignKey('division.id'))
    # history = db.relationship('History', backref='history', lazy='dynamic')
    art = db.relationship('Art', backref='art', lazy='dynamic')

    def __repr__(self):
        return f"<{self.name} >"


class Art(db.Model): #Статья
    __tablename__ = 'art'

    id = db.Column(db.Integer, primary_key=True)

    meta_description = db.Column(db.Text)
    meta_keywords = db.Column(db.Text)

    photo = db.Column(db.String(100))
    # filename = db.Column(db.String(100))
    youtube_link = db.Column(db.Text)
    
    title = db.Column(db.String(255))
    ru_title = db.Column(db.String(255))
    en_title = db.Column(db.String(255))
    
    text = db.Column(db.Text)
    ru_text = db.Column(db.Text)
    en_text = db.Column(db.Text)

    created_date = db.Column(db.DateTime, default = datetime.utcnow())
    updated_date = db.Column(db.DateTime)

    author = db.Column(db.Integer, db.ForeignKey('personal.id'))
    
    def __repr__(self):
        return f"<{self.title} >"


class Services(db.Model): #Услуги
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)

    meta_description = db.Column(db.Text)
    meta_keywords = db.Column(db.Text)
    
    name = db.Column(db.String(100))
    ru_name = db.Column(db.String(100))
    en_name = db.Column(db.String(100))
    
    description = db.Column(db.Text)
    ru_description = db.Column(db.Text)
    en_description = db.Column(db.Text)
    
    price = db.Column(db.String(50))

    created_date = db.Column(db.DateTime, default = datetime.utcnow())
    updated_date = db.Column(db.DateTime)

    division = db.Column(db.Integer, db.ForeignKey('division.id'))

    def __repr__(self):
        return f"{self.name}"


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    psw = db.Column(db.Text, nullable=False)
    is_admin = db.Column(db.Boolean(), default=False)


# class Reviews(db.Model): #Отзывы
#     __tablename__ = 'reviews'

#     id = db.Column(db.Integer, primary_key=True)
#     ball = db.Column(db.Integer, nullable=False)
#     review = db.Column(db.String(100), nullable=False)

#     patients = db.Column(db.Integer, db.ForeignKey('patients.id'))


# class Patients(db.Model): #Пациент
#     __tablename__ = 'patients'

#     id = db.Column(db.Integer, primary_key=True)