import requests
import smtplib
from email.mime.text import MIMEText

# Cloudflare API credentials
CF_API_TOKEN = "HsoabgfSbNQVeHpg30hI14GOo8mZLixzk_7HhJY8"
ZONE_ID = "38b42bfdb42dbe301b6b1a27b86ac939"

# DNS record details
RECORD_NAME = "isaadiqbal.karazo.com"
RECORD_TYPE = "CNAME"
RECORD_CONTENT = "https://isaadiqbal.github.io/dns-check/"
TTL = 3600
DNS_COMMENT = "New DNS record"

# Construct API URL
API_URL = f"https://api.cloudflare.com/client/v4/zones/38b42bfdb42dbe301b6b1a27b86ac939/dns_records"

# Request headers
headers = {
    "Authorization": f"Bearer HsoabgfSbNQVeHpg30hI14GOo8mZLixzk_7HhJY8",
    "Content-Type": "application/json"
}

# Request payload
data = {
    "type": RECORD_TYPE,
    "name": RECORD_NAME,
    "content": RECORD_CONTENT,
    "ttl": TTL,
    "comment": DNS_COMMENT
}

# Send POST request to create DNS record
response = requests.post(API_URL, json=data, headers=headers)

if response.status_code == 200:
    print("DNS record created.")
    
    # Send email notification
    subject = "DNS Record Created"
    body = f"DNS record for {RECORD_NAME} has been created successfully."
    recipient_emails = ["saad89.linux@gmail.com"]  # Add your recipient email addresses here

    sender_email = "saadiqbalbutt89@gmail.com"  # Replace with your sender email
    sender_password = "slmoutqfqdwmbzui"  # Replace with your sender email password

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = ", ".join(recipient_emails)  # Concatenate email addresses

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_emails, msg.as_string())
            print("Email notification sent successfully")
    except Exception as e:
        print("An error occurred while sending email:", e)
else:
    print("Failed to create DNS record. Status code:", response.status_code)
