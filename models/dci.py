from typing import List, Optional
from pydantic import BaseModel

class RegistroIndividual(BaseModel):
    RUNCotizanteNUM: str
    RUNCotizanteDV: str
    FolioPlanilla: str

class DCIRequest(BaseModel):
    codigo_isapre: str
    codigo_usuario: str
    clave: str
    fecha_solicitud:str
    registros:List[RegistroIndividual]


class DCIResponse(BaseModel):
    estado: str
    glosa: str



    