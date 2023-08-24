import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, recipient_emails):
    sender_email = "saadiqbalbutt89@gmail.com"
    sender_password = "slmoutqfqdwmbzui"
    
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = ", ".join(recipient_emails)  # Concatenate email addresses

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_emails, msg.as_string())
            print("Email sent successfully")
    except Exception as e:
        print("An error occurred:", e)

# DNS details
dns_details = """
DNS Record Details:
Record Name: your-subdomain.example.com
Record Type: CNAME
Record Content: https://your-cname-target.example.com
TTL: 3600
"""

recipient_emails = ["saad89.linux@gmail.com"]  # Add your recipient email addresses here
send_email("DNS Record Details", dns_details, recipient_emails)
