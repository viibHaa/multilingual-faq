import pytest
from rest_framework.test import APIClient
from faq.models import FAQ

@pytest.mark.django_db
def test_get_faqs():
    client = APIClient()
    
    # Create a test FAQ entry
    FAQ.objects.create(question="What is Django?", answer="Django is a web framework.")

    # Fetch FAQs in default (English)
    response = client.get("/api/faqs/")  # Default language is English
    assert response.status_code == 200  # Check that the request was successful
    assert "question" in response.json()[0]  # Check that 'question' exists in the response

    # Fetch FAQs in Hindi
    response = client.get("/api/faqs/?lang=hi")  # Fetch Hindi translation
    assert response.status_code == 200
    assert "question" in response.json()[0]  # Check that 'question' exists in the response
