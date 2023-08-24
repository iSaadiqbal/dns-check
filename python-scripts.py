import smtplib
from email.mime.text import MIMEText
import os
import json

def send_email(subject, body, recipient_emails):
    sender_email = "saadiqbalbutt89@gmail.com"
    sender_password = "slmoutqfqdwmbzui"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = ", ".join(recipient_emails)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_emails, msg.as_string())
            print("Email sent successfully")
    except Exception as e:
        print("An error occurred:", e)

# Read all DNS records from the JSON file
with open("all_dns_records.json", "r") as json_file:
    all_dns_records = json.load(json_file)

# Prepare DNS records for the email body
dns_records_str = "\n".join([f"Name: {record['name']}, Type: {record['type']}, Content: {record['content']}" for record in all_dns_records['result']])

# Email subject and body
email_subject = "DNS Records Update Result"
email_body = f"DNS records fetched:\n{dns_records_str}"

# Recipient email addresses
recipient_emails = ["saad89.linux@gmail.com"]

# Send the email
send_email(email_subject, email_body, recipient_emails)
