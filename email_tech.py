import smtplib
import email.message
import os

main_mail = "techcondominiopucrio@gmail.com"
senha_var_env = 'TECH_CONDOMINIO_MAIL_PASSWORD'
password = os.environ.get(senha_var_env)

def monta_corpo_email_reserva(apartamento, espaco, data):
    pronome = "o"

    if (espaco == "Churrasqueira"):
        pronome = "a"
    
    corpo_email = f"""
    <p>Este é um email automático, favor não responda.</p>
    <p>Olá, morador do apartamento {apartamento}! 
    Sua reserva para {pronome} {espaco} foi confirmada para o dia {data}.</p>
    <p></p>
    <p>Att,</p>
    <p>Tech Condomínio.</p>
    """
    return corpo_email

def monta_corpo_email_ocorrencia(apartamento, tipo, motivo, data):

    corpo_email = f"""
    <p>Este é um email automático, favor não responda.</p>
    <p>Olá, morador do apartamento {apartamento}!
    Uma {tipo} foi registrada por uma ocorrência no dia {data}, motivo:</p>
    <p>{motivo}</p>
    <p></p>
    <p>Att,</p>
    <p>Tech Condomínio.</p>
    """  
    return corpo_email

def enviar_email(corpo_email, assunto, email_destinatario):

    msg = email.message.Message()
    msg['Subject'] = assunto
    msg['From'] = main_mail
    msg['To'] = email_destinatario
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for send the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))