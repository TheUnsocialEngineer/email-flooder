import smtplib, ssl
def email():
    default_port = 465  # For SSL
    default_server="smtp.gmail.com"
    sender_email=input("Enter your Email and: ")
    receiver_email=input("Enter target Email: ")
    password = input("Enter your password: ")
    message=input("Enter email message here: ")
    smtp_server=input("Enter smtp server default is smtp.gmail.com: ")
    smtp_port=int(input("Enter smtp port default is 465: "))
    if smtp_server==(""):
        server=default_server
    else:
        server=smtp_server
    if smtp_port==(""):
        port=default_port
    else:
        port=smtp_port
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(server, port, context=context) as server:
        server.login(sender_email, password)
        while True:
            server.sendmail(sender_email, receiver_email, message)

email()