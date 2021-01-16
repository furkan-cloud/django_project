from django.shortcuts import render
from rest_framework import generics
from .models import Category, Quiz, Question
from .serializers import CategorySerializer, CategoryDetailSerializer, QuestionSerializer

from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.

class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]

class CategoryDetail(generics.ListAPIView):
    serializer_class = CategoryDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Quiz.objects.all()
        category = self.kwargs["category"] #backend, frontend hangi kategoriyse urlden kategoriye karşılık gelen değeri al
        queryset = queryset.filter(category__name = category)
        return queryset

class QuizDetail(generics.ListAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Question.objects.all()
        title = self.kwargs["title"]
        queryset = queryset.filter(quiz__title = title)
        return queryset
