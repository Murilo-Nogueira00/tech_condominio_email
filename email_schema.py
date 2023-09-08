from pydantic import BaseModel

class EmailReservaSchema(BaseModel):
    morador: str = "Apartamento do Morador"
    espaco: str = "Espaço Alugado"
    data: str = "Data do Aluguel"
    email: str = "Email do morador"

class EmailOcorrenciaSchema(BaseModel):
    morador: str = "Apartamento do Morador"
    tipo: str = "Advertência ou Multa"
    motivo: str = "Motivo da Ocorrência"
    data: str = "Data da Ocorrência"
    email: str = "Email do morador"
