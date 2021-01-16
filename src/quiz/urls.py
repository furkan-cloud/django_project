from django.urls import path
from .views import CategoryList, CategoryDetail, QuizDetail

# __init__() takes 1 positional argument but 2 were given

urlpatterns = [
    path("", CategoryList.as_view(), name="category"),
    path("<category>", CategoryDetail.as_view(), name="category-detail"),
    path("question/<title>", QuizDetail.as_view(), name="question"),
    # path("<category>", CategoryList.as_view(), name="category")
]