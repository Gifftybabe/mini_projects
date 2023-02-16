from email.message import EmailMessage
import ssl
import smtplib


email_sender = 'ulokangozi@gmail.com'
email_password = "qbqitphihjqtqamt"

email_receiver = "rayow27546@mustbeit.com"

subject = "Don't forget to subscribe"
body = """
like, comment and share
"""

# creating an instance of the EmailMessage package imported

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

# To create a content, we import ssl and smtplib

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

