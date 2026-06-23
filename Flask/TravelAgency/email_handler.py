import smtplib
from email.message import EmailMessage

import config


def send(receipient):

    msg = EmailMessage()
    msg["Subject"] = "Automatyczna wiadomość testowa"
    msg["From"] = config.SMTP_USER
    msg["To"] = receipient
    msg.set_content("Hi from Travel Agency")

    try:
        print("Connecting...")
        with smtplib.SMTP_SSL(config.SMTP_SERVER, config.SMTP_PORT) as smtp:
            print("Loging...")
            smtp.login(config.SMTP_USER, config.SMTP_PASSWORD)

            print("Sending...")
            smtp.send_message(msg)

        print("Message has been successfully sent.")
        return True

    except smtplib.SMTPAuthenticationError:
        print("Authorisation error")
        raise
    except Exception as e:
        print(f"Exception {e}")
        raise
