from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        # Get 'lang' from query params (default to 'en')
        lang = request.query_params.get('lang', 'en')  

        # Add the language context to the serializer's context
        self.serializer_class.context.update({'lang': lang})
        
        # Proceed with the default list behavior to fetch FAQ items
        return super().list(request, *args, **kwargs)

    @action(detail=True, methods=['get'])
    def get_translation(self, request, pk=None):
        # Get the FAQ object
        faq = self.get_object()
        
        # Get the language parameter from query params (default to 'en')
        lang = request.query_params.get('lang', 'en')

        # Dynamically get the translated fields (assuming you have language-specific fields)
        translated_question = getattr(faq, f'question_{lang}', faq.question_en)  # Fallback to English
        translated_answer = getattr(faq, f'answer_{lang}', faq.answer_en)  # Fallback to English
        
        # Return translated content
        return Response({
            'translated_question': translated_question,
            'translated_answer': translated_answer
        })

