from django.contrib import admin
from .models import Category, Quiz, Question, Answer
import nested_admin

# Register your models here.

class AnswerInLine(nested_admin.NestedTabularInline):
    model = Answer
    extra = 4
    max_num = 4

class QuestionInLine(nested_admin.NestedTabularInline):
    model = Question
    inlines = [AnswerInLine]
    max_num = 20

class QuizAdmin(nested_admin.NestedModelAdmin):
    model = Quiz
    inlines = [QuestionInLine]

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Answer)
