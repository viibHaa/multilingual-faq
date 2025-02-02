from django.urls import path
from .views import FAQListView, home

urlpatterns = [
    path('', home, name='home'),  # Add this line for the home route
    path('api/faqs/', FAQListView.as_view(), name='faq-list'),
]
