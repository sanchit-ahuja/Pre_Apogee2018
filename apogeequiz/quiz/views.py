# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import Question, Question_Choice, User_Choice
import functions
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm
from django.http import HttpResponse, HttpResponseRedirect,HttpRequest

# Create your views here.
def primary(request):
    #Return Home Page if user is logged in, otherwise Login Page
    if request.user.is_authenticated():
        return redirect('quiz:home')
    else:
        return redirect('quiz:login')

def login2(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            print("User: {}".format(user))
            if user:
                login(request, user)
                return redirect('quiz:home')
            else:
                return HttpResponse("Wrong Login Creds")
    else:
        form = LoginForm()
    return render(request, 'quiz/login.html', {'form': form})


# Hidden View for logging out
def logout2(request):
    logout(request)
    return redirect('quiz:login')

@login_required
def home(request):
    #Render Home Page
    #Passes Question with order_no = 1 to the template
    question = get_object_or_404(Question, order_no = 1)
    return render(request, 'quiz/home.html', {'question':question,})

@login_required
def question(request, question_order_no):
    if request.method == 'GET':
        question = get_object_or_404(Question, order_no = question_order_no)
        return render(request, 'quiz/question.html', {'question':question,})

    elif request.method == 'POST':
        user_choice = User_Choice.objects.get(pk = request.POST['choice'])

        #Update User_Choice
        functions.update_user_choice(user_choice)

        #Redirect to next question or Result if quiz has ended
        try:
            next_question =  Question.objects.get(pk = user_choice.question.order_no + 1)
            return redirect('quiz:question', question_order_no = next_question.order_no)
        except Question.DoesNotExist:
            return redirect('quiz:result')


@login_required
def result(request):
    user = request.user
    return render(request, 'quiz/result.html', {'user':user})
