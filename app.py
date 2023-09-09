import re
from flask_openapi3 import OpenAPI, Info, Tag

from email_schema import *
import email_tech

from flask_cors import CORS
from error import ErrorSchema


info = Info(title="Email Tech Condomínio", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

reserva_tag = Tag(name="Reserva", description="Envio de um email confirmando a reserva para o morador")
ocorrencia_tag = Tag(name="Ocorrência", description="Envio de um email informando sobre uma ocorrência registrada ao morador")
status_tag = Tag(name="Status", description="Verificação de status da API")

@app.post('/email/reserva', tags=[reserva_tag],
          responses={"200": EmailReservaSchema, "409": ErrorSchema, "400": ErrorSchema})
def envia_email_reserva(form: EmailReservaSchema):

    morador=form.morador
    espaco=form.espaco
    data=form.data
    email=form.email
    assunto = "Reserva Confirmada"

    try:
        email_tech.enviar_email(email_tech.monta_corpo_email_reserva(morador, espaco, data), assunto, email)
        return {"message": "Email enviado com sucesso"}, 200


    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Ocorreu um erro ao enviar o email"
        return {"message": error_msg}, 400

@app.post('/email/sancao', tags=[ocorrencia_tag],
          responses={"200": EmailOcorrenciaSchema, "409": ErrorSchema, "400": ErrorSchema})
def envia_email_ocorrencia(form: EmailOcorrenciaSchema):

    morador=form.morador
    tipo=form.tipo
    motivo=form.motivo
    data=form.data
    email=form.email
    assunto = "Nova Ocorrência Registrada"

    try:
        email_tech.enviar_email(email_tech.monta_corpo_email_ocorrencia(morador, tipo, motivo, data), assunto, email)
        return {"message": "Email enviado com sucesso"}, 200


    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Ocorreu um erro ao enviar o email"
        return {"message": error_msg}, 400

@app.get('/status', tags=[status_tag])
def check_status():
    """Verifica se a API está funcionando."""
    return {"message": "Está funcionando!"}, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
