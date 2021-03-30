from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


# Create your views here.
def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        comments = request.POST['comments']
        context = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone': phone,
            'comments': comments
        }
        template = render_to_string('pages/email_template.html', context)
        email = EmailMessage(
            'Inquiry on your website from ' + first_name + '  ' + last_name,
            template,
            settings.EMAIL_HOST_USER,
            ['rinkurb0@gmail.com', 'vikrantgautam947@gmail.com', 'tyagi11n@gmail.com'],
        )
        email.fail_silently = False
        email.send()
        messages.success(request,
                         ': Your enquiry has been made successfully')
    return render(request, 'pages/contact.html')
