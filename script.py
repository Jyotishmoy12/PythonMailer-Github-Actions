import smtplib
from email.mime.text import MIMEText # to create the body of the message
from email.mime.multipart import MIMEMultipart # to create the structure of the message
import os

def send_mail(workflow_name, repo_name, workflow_run_id):
    # email details
    sender_email = os.getenv('SENDER_EMAIL')
    receiver_email = os.getenv('RECEIVER_EMAIL')
    password = os.getenv('SENDER_PASSWORD')
    
    # email message
    subject = f"Workflow {workflow_name} failed in {repo_name}"
    body = f"Hi the workflow {workflow_name} failed for the repo {repo_name}. Please check logs for more details/\n More Details: \n Run_id:{workflow_run_id}"
    
    msg = MIMEMultipart()
    msg['from'] = sender_email
    msg['to'] = receiver_email
    msg["subject"] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    #send email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")
        
send_mail(os.getenv('WORKFLOW_NAME'), os.getenv('REPO_NAME'), os.getenv('WORKFLOW_RUN_ID'))
    