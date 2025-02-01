from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    question_translated = serializers.SerializerMethodField()
    answer_translated = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'question_translated', 'answer_translated']

    def get_question_translated(self, obj):
        return obj.translated_question

    def get_answer_translated(self, obj):
        return obj.translated_answer

