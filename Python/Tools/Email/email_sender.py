import smtplib

sender_email = "korafisey@gmail.com"
receiver_email = "korafisey@gmail.com"

with open("password.txt", "r") as file:
    password = file.read().strip()

message = """
Subject: Test Email

This is a test email.
Sent by python
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message)
server.quit()

