# utils.py
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template  # Add this import statement
import uuid
def send_mail_(email,token):
    subject = "Currency Alert"
    message = f'Hi , click on the link to reset your password http://127.0.0.1:8000/change-password/{token}/'
    token = token
    url=f'127.0.0.1:8000/password_reset_confirm/{token}/'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    html_template = get_template('password_reset_email.html')
    html_content = html_template.render({'url':url})
    msg = EmailMultiAlternatives(subject, message, from_email, recipient_list)  # Use `message` instead of an empty string
    msg.attach_alternative(html_content, "text/html")
    msg.send()




