# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import Question, Question_Choice, User_Choice
import functions
# Create your views here.
def primary(request):
    #Return Home Page if user is logged in, otherwise Login Page
    if request.user.is_authenticated():
        return redirect('quiz:home')
    else:
        return redirect('quiz:login')

def signup(request):
    #Render Sign-Up Page
    if request.method == 'GET':
        return render(request, 'quiz/signup.html')

    #Sign-Up User
    elif request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_re = request.POST['password_re']

        #Check for Null values and special characters
        if username.isalnum() and password.isalnum():
            if password == password_re:
                user = User(username = username, email = email)
                user.set_password(password)
                user.save()
                redirect('quiz:login')
            else:
                messages.error(request, "Your passwords don't match!")
                return redirect('quiz:signup')
        else:
            messages.error(request, "Please fill all the details properly!")
            redirect('quiz:siqnup')

def login(request):
    #Render Login Page
    if request.method == 'GET':
        return render(request, 'quiz/login.html')

    #Login User
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        my_user = authenticate(username = username, password = password)
        if my_user is not None:
            django_login(request, user)
            redirect('blog:home')
        else:
            messages.error(request, "Incorrect username/password. Try Again!")
            redirect('blog:login')

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
            return redirect('blog:question', question_order_no = next_question.order_no)
        except Question.DoesNotExist:
            return redirect('quiz:result')


@login_required
def result(request):
    user = request.user
    return render(request, 'quiz/result.html', {'user':user})
