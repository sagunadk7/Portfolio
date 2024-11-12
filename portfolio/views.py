from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
def note(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        view_boxes = request.POST.getlist('viewBox')  
        message = f"Name: {name}\nEmail: {email}\nSelected Options: {', '.join(view_boxes)}"
        try:
            send_mail(
                subject='New Work Request Submission',
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['sagunadhikari100@gmail.com'],
                fail_silently=False,
            )
            return render(request, 'index.html', {
                'success_message': "Your request has been sent successfully!"
            })
        except Exception as e:
            return render(request, 'contact.html', {
                'error_message': f"An error occurred: {str(e)}"
            })

    else:
        return render(request, 'index.html')
