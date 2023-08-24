import os
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

# Get DNS details from environment variables
dns_name = os.environ.get("RECORD_NAME", "")
dns_type = os.environ.get("RECORD_TYPE", "")
dns_content = os.environ.get("RECORD_CONTENT", "")
ttl = os.environ.get("TTL", "")

# Prepare DNS details string
dns_details = f"""
DNS Record Details:
Record Name: {dns_name}
Record Type: {dns_type}
Record Content: {dns_content}
TTL: {ttl}
"""

recipient_emails = ["saad89.linux@gmail.com"]  # Add your recipient email addresses here
send_email("DNS Record Details", dns_details, recipient_emails)
