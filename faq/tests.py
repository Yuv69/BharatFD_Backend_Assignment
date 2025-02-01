from rest_framework.test import APITestCase
from rest_framework import status
from .models import FAQ

class FAQViewSetTestCase(APITestCase):
    def setUp(self):
        # Create FAQ objects with translations
        FAQ.objects.create(
            question_en='What is Django?',
            answer_en='Django is a Python web framework.',
            question_es='¿Qué es Django?',
            answer_es='Django es un framework web de Python.'
        )
        FAQ.objects.create(
            question_en='What is DRF?',
            answer_en='DRF stands for Django Rest Framework.',
            question_es='¿Qué es DRF?',
            answer_es='DRF significa Django Rest Framework.'
        )

    def test_list_faq_translations_en(self):
        # Test fetching FAQs with the default language (English)
        response = self.client.get('/api/faqs/', {'lang': 'en'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['translated_question'], 'What is Django?')
        self.assertEqual(response.data[0]['translated_answer'], 'Django is a Python web framework.')

    def test_list_faq_translations_es(self):
        # Test fetching FAQs in Spanish
        response = self.client.get('/api/faqs/', {'lang': 'es'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['translated_question'], '¿Qué es Django?')
        self.assertEqual(response.data[0]['translated_answer'], 'Django es un framework web de Python.')

    def test_get_translation_en(self):
        # Test getting a specific FAQ's translation in English
        faq = FAQ.objects.get(question_en='What is Django?')
        response = self.client.get(f'/api/faqs/{faq.id}/get_translation/', {'lang': 'en'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['translated_question'], 'What is Django?')
        self.assertEqual(response.data['translated_answer'], 'Django is a Python web framework.')

    def test_get_translation_es(self):
        # Test getting a specific FAQ's translation in Spanish
        faq = FAQ.objects.get(question_en='What is Django?')
        response = self.client.get(f'/api/faqs/{faq.id}/get_translation/', {'lang': 'es'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['translated_question'], '¿Qué es Django?')
        self.assertEqual(response.data['translated_answer'], 'Django es un framework web de Python.')
