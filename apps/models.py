# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from email.policy import default
from apps import db
from sqlalchemy.exc import SQLAlchemyError
from apps.exceptions.exception import InvalidUsage
import datetime as dt
from sqlalchemy.orm import relationship
from enum import Enum

class CURRENCY_TYPE(Enum):
    usd = 'usd'
    eur = 'eur'

class Product(db.Model):

    __tablename__ = 'products'

    id            = db.Column(db.Integer,      primary_key=True)
    name          = db.Column(db.String(128),  nullable=False)
    info          = db.Column(db.Text,         nullable=True)
    price         = db.Column(db.Integer,      nullable=False)
    currency      = db.Column(db.Enum(CURRENCY_TYPE), default=CURRENCY_TYPE.usd, nullable=False)

    date_created  = db.Column(db.DateTime,     default=dt.datetime.utcnow())
    date_modified = db.Column(db.DateTime,     default=db.func.current_timestamp(),
                                               onupdate=db.func.current_timestamp())
    
    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)

    def __repr__(self):
        return f"{self.name} / ${self.price}"

    @classmethod
    def find_by_id(cls, _id: int) -> "Product":
        return cls.query.filter_by(id=_id).first() 

    def save(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)

    def delete(self) -> None:
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)
        return


#__MODELS__
class Usuario(db.Model):

    __tablename__ = 'Usuario'

    id = db.Column(db.Integer, primary_key=True)

    #__Usuario_FIELDS__
    nombre = db.Column(db.String(255),  nullable=True)
    apellido = db.Column(db.String(255),  nullable=True)
    direccion = db.Column(db.String(255),  nullable=True)
    telefono = db.Column(db.String(255),  nullable=True)
    activo = db.Column(db.Boolean, nullable=True)
    user_id = db.Column(db.Integer, nullable=True)
    historia = db.Column(db.Text, nullable=True)

    #__Usuario_FIELDS__END

    def __init__(self, **kwargs):
        super(Usuario, self).__init__(**kwargs)


class Dentist(db.Model):

    __tablename__ = 'Dentist'

    id = db.Column(db.Integer, primary_key=True)

    #__Dentist_FIELDS__

    #__Dentist_FIELDS__END

    def __init__(self, **kwargs):
        super(Dentist, self).__init__(**kwargs)


class Blog(db.Model):

    __tablename__ = 'Blog'

    id = db.Column(db.Integer, primary_key=True)

    #__Blog_FIELDS__
    post = db.Column(db.String(255),  nullable=True)
    post_id = db.Column(db.Integer, nullable=True)
    imagen = db.Column(db.String(255),  nullable=True)

    #__Blog_FIELDS__END

    def __init__(self, **kwargs):
        super(Blog, self).__init__(**kwargs)


class Comentarios(db.Model):

    __tablename__ = 'Comentarios'

    id = db.Column(db.Integer, primary_key=True)

    #__Comentarios_FIELDS__
    contenido = db.Column(db.Text, nullable=True)

    #__Comentarios_FIELDS__END

    def __init__(self, **kwargs):
        super(Comentarios, self).__init__(**kwargs)


class Citas(db.Model):

    __tablename__ = 'Citas'

    id = db.Column(db.Integer, primary_key=True)

    #__Citas_FIELDS__
    fecha = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Citas_FIELDS__END

    def __init__(self, **kwargs):
        super(Citas, self).__init__(**kwargs)


class Collections(db.Model):

    __tablename__ = 'Collections'

    id = db.Column(db.Integer, primary_key=True)

    #__Collections_FIELDS__
    name = db.Column(db.String(255),  nullable=True)
    active = db.Column(db.Boolean, nullable=True)

    #__Collections_FIELDS__END

    def __init__(self, **kwargs):
        super(Collections, self).__init__(**kwargs)


class Imagenes(db.Model):

    __tablename__ = 'Imagenes'

    id = db.Column(db.Integer, primary_key=True)

    #__Imagenes_FIELDS__
    ruta = db.Column(db.Text, nullable=True)
    background = db.Column(db.Boolean, nullable=True)

    #__Imagenes_FIELDS__END

    def __init__(self, **kwargs):
        super(Imagenes, self).__init__(**kwargs)


class Messages(db.Model):

    __tablename__ = 'Messages'

    id = db.Column(db.Integer, primary_key=True)

    #__Messages_FIELDS__
    asunto = db.Column(db.String(255),  nullable=True)
    contenido = db.Column(db.Text, nullable=True)
    leido = db.Column(db.Boolean, nullable=True)

    #__Messages_FIELDS__END

    def __init__(self, **kwargs):
        super(Messages, self).__init__(**kwargs)


class Services(db.Model):

    __tablename__ = 'Services'

    id = db.Column(db.Integer, primary_key=True)

    #__Services_FIELDS__
    imagen = db.Column(db.String(255),  nullable=True)
    descripcion = db.Column(db.String(255),  nullable=True)
    titulo = db.Column(db.String(255),  nullable=True)
    informacion = db.Column(db.Text, nullable=True)

    #__Services_FIELDS__END

    def __init__(self, **kwargs):
        super(Services, self).__init__(**kwargs)


class Sliders(db.Model):

    __tablename__ = 'Sliders'

    id = db.Column(db.Integer, primary_key=True)

    #__Sliders_FIELDS__

    #__Sliders_FIELDS__END

    def __init__(self, **kwargs):
        super(Sliders, self).__init__(**kwargs)


class Texto(db.Model):

    __tablename__ = 'Texto'

    id = db.Column(db.Integer, primary_key=True)

    #__Texto_FIELDS__
    titulo = db.Column(db.String(255),  nullable=True)
    contenido = db.Column(db.Text, nullable=True)
    texto_id = db.Column(db.Integer, nullable=True)

    #__Texto_FIELDS__END

    def __init__(self, **kwargs):
        super(Texto, self).__init__(**kwargs)


class Suscripto(db.Model):

    __tablename__ = 'Suscripto'

    id = db.Column(db.Integer, primary_key=True)

    #__Suscripto_FIELDS__
    email = db.Column(db.String(255),  nullable=True)

    #__Suscripto_FIELDS__END

    def __init__(self, **kwargs):
        super(Suscripto, self).__init__(**kwargs)



#__MODELS__END
