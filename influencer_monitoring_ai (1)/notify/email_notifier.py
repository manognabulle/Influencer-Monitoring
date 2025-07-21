import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from config import EMAIL, EMAIL_PASSWORD

def send_email(subject, body, receiver_email, attachment_path=None):
    message = MIMEMultipart()
    message["Subject"] = subject
    message["From"] = EMAIL["sender"]
    message["To"] = receiver_email

    # Attach the email body
    message.attach(MIMEText(body, "plain"))

    # Attach CSV file if given
    if attachment_path:
        with open(attachment_path, "rb") as f:
            file = MIMEApplication(f.read(), Name="influencer_summary.csv")
        file['Content-Disposition'] = 'attachment; filename="influencer_summary.csv"'
        message.attach(file)

    # Send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(EMAIL["SMTP_SERVER"], EMAIL["SMTP_PORT"], context=context) as server:
        server.login(EMAIL["sender"], EMAIL_PASSWORD)
        server.send_message(message)
