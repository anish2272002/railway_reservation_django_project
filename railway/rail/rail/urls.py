"""rail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import start.views as sv
import dash.views as dv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sv.start),
    path('start', sv.start),
    path('prereq', sv.prereq),
    path('creators', sv.creators),
    path('dash', dv.dash),
    path('login', dv.log),
    path('trainsearch', dv.trainsearch),
    path('book', dv.book),
    path('ticketconfirm', dv.tconfirm),
    path('ticket', dv.ticket_status),
    path('cancel', dv.cancel_ticket),
    path('reset', dv.reset)
]
