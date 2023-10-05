from django.conf import settings
from django.core.mail import send_mail
def send_mail_():
    subject="Currency Alert"
    message="Currency Alert gnsn sjdg sjo  jf ia f"
    from_email=settings.EMAIL_HOST_USER
    recipent_list=['anuraagbv1@gmail.com']
    send_mail(subject,message,from_email,recipent_list)
