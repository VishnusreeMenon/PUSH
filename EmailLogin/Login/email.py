from django.core.mail import send_mail,EmailMessage
import math,random
from django.conf import settings
from django.http import HttpResponse
from .models import User



def otp_generator():
    digits = "0123456789"
    otp = ""
 
   
    for i in range(4) :
        otp += digits[math.floor(random.random() * 10)]
 
    return otp


def opt_email(email):
    otp = otp_generator()
    
    print(email)
    subject = "Account verification"
    message = f"The OTP is {otp}. Do not share it"
    from_mail = settings.EMAIL_HOST_USER
    email_from = settings.DEFAULT_FROM_EMAIL
    try:
        
        # send_mail(subject,message,from_mail,[email],fail_silently=False)
        msg  = EmailMessage('Request Callback',f"The otp is: {otp}",to = [email])
        # print(msg)
        msg.send()
    except Exception as e:
        print("error-",e)
    # msg  = EmailMessage('Request Callback',f"The otp is: {otp}",to = [email])
    # print(msg)
    # msg.send()
    print('mail sent')
    user_obj = User.objects.get(email = email)
    user_obj.otp = otp
    user_obj.save()
    # return HttpResponse("Done")