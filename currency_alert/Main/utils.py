# utils.py
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template  # Add this import statement

def send_mail_(email):
    subject = "Currency Alert"
    message = "Password reset"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    html_template = get_template('password_reset_email.html')
    html_content = html_template.render()
    msg = EmailMultiAlternatives(subject, message, from_email, recipient_list)  # Use `message` instead of an empty string
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    


