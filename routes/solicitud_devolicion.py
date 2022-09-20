# encode.py
import datetime
from models.dci import DCIRequest, DCIResponse
from fastapi import APIRouter
from bson import ObjectId

dci = APIRouter()


@dci.post('/solicitud-devolucion', tags=["solicitud-devolucion"])
def solicitud_devolucion(form: DCIRequest):
    form = dict(form)
    listado_registros = form['registros']
    for registro in listado_registros:
        print("registro")
        print(registro)
    return form