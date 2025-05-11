from rest_framework import serializers


class WordValidator:
    """Класс валидации запрещенных слов"""
    def __call__(self, value):
        if value in ['ерунда', 'глупость', 'чепуха']:
            raise serializers.ValidationError("Данные слова не допустимы.")
