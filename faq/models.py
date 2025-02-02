from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

# Create your models here.

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()  # WYSIWYG Editor support

    # Translated versions of the question and answer
    question_hi = models.TextField(null=True, blank=True)  # Hindi Question
    answer_hi = RichTextField(null=True, blank=True)  # Hindi Answer
    question_bn = models.TextField(null=True, blank=True)  # Bengali Question
    answer_bn = RichTextField(null=True, blank=True)  # Bengali Answer

    def save(self, *args, **kwargs):
        translator = Translator()

        # Auto-translate question if not already translated
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, dest='bn').text

        # Auto-translate answer if not already translated
        if not self.answer_hi:
            self.answer_hi = translator.translate(self.answer, dest='hi').text
        if not self.answer_bn:
            self.answer_bn = translator.translate(self.answer, dest='bn').text

        super().save(*args, **kwargs)

    def get_translated_question(self, lang):
        """Returns the translated question based on the selected language."""
        return getattr(self, f'question_{lang}', self.question)

    def get_translated_answer(self, lang):
        """Returns the translated answer based on the selected language."""
        return getattr(self, f'answer_{lang}', self.answer)

    def __str__(self):
        return self.question
