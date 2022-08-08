from rest_framework import serializers


def validate_follow_to_yourself(data):
    """
    Вызывает исключение при попытке подписки на себя
    """
    if data['user'] == data['following']:
        raise serializers.ValidationError(
            'нельзя подписываться на себя'
        )
    return data
