from rest_framework import serializers
from .models import User, Acter, Feedback, Films, Category, Genre


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ActerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acter
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'