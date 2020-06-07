import smtplib, ssl

def send_mail(to, body):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = 'prashantuprojects@gmail.com'
    password = 'projectdevelopment'

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, to, body)

    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()