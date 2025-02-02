from django.contrib import admin
from .models import FAQ
# Register your models here.

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'question_hi', 'question_bn')  # Display translated questions
    search_fields = ('question', 'question_hi', 'question_bn')  # Enable search
    list_filter = ('question',)  # Add filter options
    ordering = ('id',)  # Order by ID
    fieldsets = (
        ("Original", {'fields': ('question', 'answer')}),
        ("Translations", {'fields': ('question_hi', 'question_bn')}),
    )
    readonly_fields = ('question_hi', 'question_bn')  # Prevent manual edits of translations
