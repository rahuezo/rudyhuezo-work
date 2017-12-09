# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def contact_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_name = '{0} {1}'.format(first_name.strip(), last_name.strip())

        send_mail(
            'Message from {0}'.format(full_name.title()),
            '{0}'.format(message),
            settings.EMAIL_HOST_USER,
            [settings.TO_EMAIL],
            fail_silently=False,
            html_message="""
                <html>
                <body>
                <h1>Full Name: {0}</h1>
                <h1>Email: {1}</h1>
                <h1>Message: {2}</h1>
                </body>
                </html>
                """.format(full_name, email, message),
        )

        messages.success(request, "Thank you for your message! I'll get back to you as soon as possible.", extra_tags="sent-message")

    return redirect("/#contact")
