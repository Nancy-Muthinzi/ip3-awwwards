from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
    subject = 'Welcome to the Awwwards website, a place to post and vote for the best websites out there!'
    sender = 'kathinimuthinzi@gmail.com'

    text_content = render_to_string('email/aemail.txt',{"name": name})
    html_content = render_to_string('email/aemail.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()