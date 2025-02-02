from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FAQ

# Create your views here.

# Home view
def home(request):
    return HttpResponse("Welcome to the FAQ API!")

# FAQ API view with caching
class FAQListView(APIView):
    def get(self, request):
        lang = request.query_params.get('lang', 'en')  # Default to English
        cache_key = f"faqs_{lang}"  # Unique cache key for each language
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        faqs = FAQ.objects.all()
        data = [
            {
                'id': faq.id,
                'question': faq.get_translated_question(lang),
                'answer': faq.answer,  # WYSIWYG editor content
            }
            for faq in faqs
        ]

        cache.set(cache_key, data, timeout=300)  # Cache for 5 minutes
        return Response(data)



