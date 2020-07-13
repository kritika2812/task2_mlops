import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "shahkritika99@gmail.com"  # Enter your address
receiver_email = "shahkritika99@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: kritika1999! ")
message = """\
Subject: "PHP Site Is Running!"
Project is done."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
