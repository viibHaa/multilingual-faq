import pytest
from faq.models import FAQ

@pytest.mark.django_db  # Ensures the test is run in a database context
def test_faq_auto_translation():
    faq = FAQ.objects.create(
        question="How does Django work?",  # English question
        answer="Django is a Python-based web framework."
    )

    # Check that the Hindi translation exists
    assert faq.question_hi is not None
    # Check that the Bengali translation exists
    assert faq.question_bn is not None
    # Check that the translations are of type string
    assert isinstance(faq.question_hi, str)
    assert isinstance(faq.question_bn, str)
