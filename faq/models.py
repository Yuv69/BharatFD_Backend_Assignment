from django.db import models

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    translated_question = models.CharField(max_length=255, blank=True, null=True)
    translated_answer = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Automatically translate question and answer when saving
        self.translated_question = self.translate_text(self.question)
        self.translated_answer = self.translate_text(self.answer)
        super().save(*args, **kwargs)

    def translate_text(self, text):
        from googletrans import Translator
        translator = Translator()
        try:
            translated = translator.translate(text, src='en', dest='es')  # Example: Translating to Spanish
            return translated.text
        except Exception:
            return text  # Fallback to original text if translation fails


