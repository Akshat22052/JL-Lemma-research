import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email content
sender_email = "karnwalakshat@gmail.com"
receiver_email = "karnwalakshat2003@gmail.com"
subject = "Test Email"
body = "This is a test email sent from Python."

# Create a message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach body to the email
msg.attach(MIMEText(body, 'plain'))

# SMTP server settings
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'karnwalakshat@gmail.com'
smtp_password = 'goaq olbw ynlh wwxd'

# Connect to SMTP server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()

# Login to SMTP server
server.login(smtp_username, smtp_password)

# Send email
server.send_message(msg)

# Quit SMTP server
server.quit()

print("Email sent successfully!")








