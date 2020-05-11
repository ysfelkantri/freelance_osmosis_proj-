from django.shortcuts import render
from django.core.mail import send_mail

def sendmail(request):
    
    send_mail('django test mail',
              'hello from osmosis',
              'osmosis.testing.app@gmail.com',
              ['anas.mansouri@usmba.ac.ma'],
              fail_silently=False)  
    return render(request, 'index.html')



#send_mail('django test mail', 'this is django test body', src, [dst], fail_silently=False)

