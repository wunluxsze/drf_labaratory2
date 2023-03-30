from django.shortcuts import render
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.status import HTTP_200_OK
from .models import User, Category, Feedback, Films, Acter, Genre
from .serializers import ActerSerializer, CategorySerializer, FeedbackSerializer, FilmSerializer, GenreSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
# Create your views here.



# отзывы
@api_view(['GET', "POST"])
@permission_classes((IsAuthenticated,))
def get_create_feedback(request):
    if request.method == "GET":
        feedback = Feedback.objects.all()
        serializer = FeedbackSerializer(feedback, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FeedbackSerializer(data=request.data)
        if request.user.is_active and not request.user.is_superuser:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['PATCH', "GET", 'DELETE'])
@permission_classes((IsAuthenticated,))
def get_edit_delete_feedback(request, pk):
    if request.method == 'GET':
            try:
                feedback = Feedback.objects.get(id=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = FeedbackSerializer(feedback, many=False)
            return Response(serializer.data)
    elif request.method == "PATCH":
        if request.user.is_active and not request.user.is_superuser:
            try:
                feedback = Feedback.objects.get(id=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = FeedbackSerializer(data=request.data, instance=feedback, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    elif request.method == 'DELETE':
        if request.user.is_active and not request.user.is_superuser:
            try:
                feedback = Feedback.objects.get(id=pk)
                feedback.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Films.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


# фильмы

@api_view(['GET', "POST"])
@permission_classes((AllowAny,))
def get_create_films(request):
    if request.method == "GET":
        films = Films.objects.all()
        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FilmSerializer(data=request.data)
        if request.user.is_superuser:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['PATCH', "GET", 'DELETE'])
@permission_classes((AllowAny,))
def get_edit_delete_films(request, pk):
    if request.method == 'GET':
            try:
                films = Films.objects.get(id=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = FilmSerializer(films, many=False)
            return Response(serializer.data)
    elif request.method == "PATCH":
        if request.user.is_superuser:
            try:
                films = Films.objects.get(id=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = FilmSerializer(data=request.data, instance=films, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    elif request.method == 'DELETE':
        if request.user.is_superuser:
            try:
                films = Films.objects.get(id=pk)
                films.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Films.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


# категории

@api_view(['GET', "POST"])
@permission_classes((IsAdminUser,))
def get_create_category(request):
    if request.method == "GET":
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if request.user.is_superuser:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['PATCH', "GET", 'DELETE'])
@permission_classes((IsAdminUser,))
def get_edit_delete_category(request, pk):
    if request.method == 'GET':
            try:
                category = Category.objects.get(id=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = CategorySerializer(category, many=False)
            return Response(serializer.data)
    elif request.method == "PATCH":
        if request.user.is_superuser:
            try:
                category = Category.objects.get(id=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = CategorySerializer(data=request.data, instance=category, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    elif request.method == 'DELETE':
        if request.user.is_superuser:
            try:
                category = Category.objects.get(id=pk)
                category.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Films.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


# жанры

@api_view(['GET', "POST"])
@permission_classes((IsAdminUser,))
def get_create_actors(request):
    if request.method == "GET":
        actors = Acter.objects.all()
        serializer = ActerSerializer(actors, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ActerSerializer(data=request.data)
        if request.user.is_superuser:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['PATCH', "GET", 'DELETE'])
@permission_classes((IsAdminUser,))
def get_edit_delete_actors(request, pk):
    if request.method == 'GET':
            try:
                actors = Acter.objects.get(id=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ActerSerializer(actors, many=False)
            return Response(serializer.data)
    elif request.method == "PATCH":
        if request.user.is_superuser:
            try:
                actors = Acter.objects.get(id=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = ActerSerializer(data=request.data, instance=actors, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    elif request.method == 'DELETE':
        if request.user.is_superuser:
            try:
                actors = Acter.objects.get(id=pk)
                actors.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Films.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
def logout(request):
    token = Token.objects.get(user=request.user)
    token.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)
