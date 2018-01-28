from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.urls import reverse
from .forms import UserForm, UserProfileForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Question, Answer
from django.http import HttpResponse


def login(request):
    if request.user.is_authenticated:
            return render(request, 'forum/feed.html', {})
    else:
        if request.method == 'POST':
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth_login(request, user)
                    return render(request, 'forum/feed.html', {})
                else:
                    error = 'Your account is disabled.'
                    return render(request, 'forum/login.html', {'error': error})
            else:
                error = 'Incorrect Username or Password'
                return render(request, 'forum/login.html', {'error': error})
        else:
            return render(request, 'forum/login.html', {})


def logout(request):
    auth_logout(request)
    return redirect(reverse('login'))


def register(request):
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            auth_login(request, user)
            return redirect("profile", idx=profile.id)
        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            error = "Error in registering"
            return render(request,
                          'forum/register.html',
                          {'user_form': user_form, 'profile_form': profile_form,
                           'error': error})

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
                  'forum/register.html',
                  {'user_form': user_form, 'profile_form': profile_form})


@login_required(login_url='/login/')
def profile(request, idx):
    client = get_object_or_404(UserProfile, pk=idx)

    return render(request, 'forum/user_profile.html', {'client': client})


def search(request):
    if request.GET.get('search'):
        param = request.GET.get('search')
        questions = Question.objects.filter(question__icontains=param)
        if not questions.exists():
            return render(request, 'form/search.html', {'error': 'NO MATCHING QUESTIONS FOUND'})
        return render(request, 'forum/search.html', {'questions': questions})
    return render(request, 'forum/search.html', {})


def view_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'forum/view_question.html', {'question': question})


@login_required(login_url='forum:login')
def add_answer(request, abc):
    print(13)
    if request.method == 'POST':
        print(1)
        ans = request.POST.get('answer', '')
        ques = Question.objects.get(id=abc)
        # if ques:
        user = request.user
        print(2)
        profile = user.user_profile
        print(ans)
        answer = Answer.objects.create(answered_by=profile, ques=ques, answer=ans)
        print(answer.answer)
        answer.save()
        return redirect('forum:view_question', pk=abc)
        # else:
        #     return redirect('forum:login')
    ques = get_object_or_404(Question, pk=abc)
    return render(request, 'forum/view_question.html', {'question': ques})
