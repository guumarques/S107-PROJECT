import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def main():
    status_testes = os.getenv("STATUS_TESTES", "desconhecido")
    status_build = os.getenv("STATUS_BUILD", "desconhecido")
    
    # TODO (Integrante 2): Remover as variaveis do GitHub abaixo e substituir pelas do Jenkins
    # (ex: JOB_NAME, BUILD_NUMBER, BUILD_URL) pois o professor proibiu o uso de GitHub Actions.
    
    build_status = os.getenv("STATUS_BUILD", "desconhecido")
    job_name = os.getenv("JOB_NAME", "desconecido")
    build_number = os.getenv("BUILD_NUMBER", "desconecido")
    build_url = os.getenv("BUILD_URL", "desconecido")

    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = os.getenv("SMTP_PORT")
    email_remetente = os.getenv("EMAIL_REMETENTE")
    email_senha = os.getenv("EMAIL_SENHA")
    email_destino = os.getenv("EMAIL_DESTINO")

    assunto = "Resultado do pipeline CI/CD"
    corpo = f"""
Pipeline finalizado.

Repositório: {job_name}
Build: {build_status}
Build Number: {build_number}
Execução: {build_url}
""".strip()

    if not all([smtp_host, smtp_port, email_remetente, email_senha, email_destino]):
        print("Segredos de e-mail não configurados. Notificação não enviada.")
        print(corpo)
        return

    mensagem = MIMEMultipart()
    mensagem["From"] = email_remetente
    mensagem["To"] = email_destino
    mensagem["Subject"] = assunto
    mensagem.attach(MIMEText(corpo, "plain", "utf-8"))

    with smtplib.SMTP(smtp_host, int(smtp_port)) as servidor:
        servidor.starttls()
        servidor.login(email_remetente, email_senha)
        servidor.send_message(mensagem)

    print("Notificação enviada com sucesso.")


if __name__ == "__main__":
    main()