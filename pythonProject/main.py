from email.mime.text import MIMEText
import smtplib
import imaplib

class EmailSender:
    def __init__(self, smtp_server, smtp_port):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_email(self, sender, recipient, subject, message):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipient

        try:
            smtp_server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            smtp_server.ehlo()
            smtp_server.starttls()
            smtp_server.sendmail(sender, recipient, msg.as_string())
            smtp_server.quit()
            return True
        except Exception as e:
            print(f"Error al enviar el correo electrónico: {str(e)}")
            return False

class EmailVerifier:
    def __init__(self, imap_server, imap_port):
        self.imap_server = imap_server
        self.imap_port = imap_port

    def check_flagged_emails(self, username, password, flag):
        try:
            imap_server = imaplib.IMAP4_SSL(self.imap_server, self.imap_port)
            imap_server.login(username, password)
            imap_server.select("INBOX")
            _, data = imap_server.search(None, f'FLAGGED {flag}')
            imap_server.logout()

            if data[0]:
                print("Se encontraron correos electrónicos con la bandera especificada.")
            else:
                print("No se encontraron correos electrónicos con la bandera especificada.")
            return True
        except Exception as e:
            print(f"Error al verificar el correo electrónico: {str(e)}")
            return False

if __name__ == '__main__':
    # Configuración del servidor SMTP y detalles del correo electrónico
    smtp_server = '67.205.158.200'
    smtp_port = 25  # Puerto SMTP estándar
    sender = 'jorge.alvarado@warnesclinmeo.com'
    recipient = 'jorge.alvarado@warnesclinmeo.com'
    subject = 'Prueba de correo electrónico'
    message = 'Hola, esto es un ejemplo de envío de correo electrónico desde Python.'

    email_sender = EmailSender(smtp_server, smtp_port)
    if email_sender.send_email(sender, recipient, subject, message):
        print("Correo electrónico enviado correctamente.")

        # # Configuración del servidor IMAP y detalles de la cuenta de correo
        # imap_server = 'IP_DEL_SERVIDOR_IMAP'
        # imap_port = 143  # Puerto IMAP estándar
        # username = 'tu_usuario'
        # password = 'tu_contraseña'
        # flag = 'tu_bandera'

        # email_verifier = EmailVerifier(imap_server, imap_port)
        # email_verifier.check_flagged_emails(username, password, flag)
    else:
        print("Error al enviar el correo electrónico.")
