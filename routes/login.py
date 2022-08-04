# encode.py
import datetime
import jwt
from bson import ObjectId
from passlib.hash import sha256_crypt
from config.db import conn
from models.user import Login
from bson import ObjectId
from fastapi import APIRouter, status, Response
from bson import ObjectId
from passlib.hash import sha256_crypt
from starlette.status import HTTP_204_NO_CONTENT

from models.user import User
from config.db import conn
from schemas.user import user_entity, users_entity
SECRET_KEY = "esta es la clave secreta para generar el token"


login = APIRouter()


@login.post('/login', tags=["login"])
def validar_login(form: Login):

    form = dict(form)
    print(form)
    usuario = conn.user.find_one(
        {
            "username": form['username'],
            "password": sha256_crypt.encrypt(form["password"])
        }
    )

    print(usuario)

    return crear_token(usuario['username'])


def crear_token(usuario):
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow(),
        'sub': usuario
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')


# validate jwt token
def validar_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return 'El token ha expirado'
    except jwt.InvalidTokenError:
        return 'El token no es valido'
