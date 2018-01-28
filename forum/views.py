from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Question


def search(request):
    if request.GET.get('search'):
        param = request.GET.get('search')
        questions = Question.objects.filter(question__contains=param)
        return render(request, 'forum/search.html', {'questions': questions})
    return render(request, 'forum/search.html', {})
