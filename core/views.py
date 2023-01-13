from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

from core.models import Question, Choice

# Create your views here.
def index(request):
    question_list = Question.objects.all().order_by('-created')
    context = {
        "question_list":question_list
    }
    return render(request, 'index.html', context)


def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    context = {
        "question":question
    }
    return render(request, "detail.html", context)


def result(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    context = {
        'question':question
    }
    return render(request, "result.html", context)

def vote(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    try:
        selected_choice = question.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        messages.add_message(request, messages.ERROR, "You did not select a choice")
        return render(request, "detail.html", {'question':question})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        messages.success(request, "Voted success")
        return HttpResponseRedirect(reverse("core:results", args=[question_pk]))