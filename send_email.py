import smtplib
from email.mime.text import MIMEText
import os
import requests

def send_email(subject, body, recipient_emails):
    sender_email = "saadbiqbalbutt89@gmail.com"
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
trigger_count = os.environ.get("TRIGGER_COUNT", "")
dns_comment = os.environ.get("DNS_COMMENT", "")
ttl = os.environ.get("TTL", "")

# Prepare DNS details string
dns_details = f"""
DNS Record Details:
Record Name: {dns_name}
Record Type: {dns_type}
Record Content: {dns_content}
TTL: {ttl}
Trigger Count: {trigger_count}
Comment: {dns_comment}
"""

# Get available DNS records using Cloudflare API
CF_API_TOKEN = "your-cloudflare-api-token"
ZONE_ID = "your-zone-id"
API_URL = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records"
headers = {
    "Authorization": f"Bearer {CF_API_TOKEN}",
    "Content-Type": "application/json"
}
response = requests.get(API_URL, headers=headers)
if response.status_code == 200:
    available_records = "List of Available DNS Records:\n"
    records = response.json()["result"]
    for record in records:
        formatted_record = f"Record Name: {record['name']}\nRecord Type: {record['type']}\nRecord Content: {record['content']}\nTTL: {record['ttl']}\n\n"
        available_records += formatted_record
    available_records = available_records.strip()  # Remove trailing newline
else:
    available_records = "Failed to retrieve available DNS records."

recipient_emails = ["saad89.linux@gmail.com","tayyubtahir87@gmail.com"]  # Add your recipient email addresses here
send_email("DNS Record Details", dns_details + "\n" + available_records, recipient_emails)
