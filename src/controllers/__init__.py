import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_addrs, body):
    from_addr = "ilq2krdexj6dd2fh@ethereal.email"
    login = "ilq2krdexj6dd2fh@ethereal.email"
    password = "JyfTsh8a73rRTAvYvD"

    msg = MIMEMultipart()
    msg["from"] = "viagem@email.com"
    msg["to"] = ', '.join(to_addrs)

    msg["Subject"] = "Confirmação de Viagem!"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.starttls()
    server.login(login, password)
    text = msg.as_string()

    for email in to_addrs:
        server.sendmail(from_addr, email, text)

    server.quit()