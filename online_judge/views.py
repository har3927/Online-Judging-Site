from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render,HttpResponse
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Problem, Solution
import filecmp, os

# Create your views here.

def problems(request):
    problem_list = Problem.objects.all()
    context = { 'problem_list' : problem_list}
    return render(request, 'online_judge/problems.html', context)

def problemDetails(request,problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    context = { 'problem':problem}
    return render(request,'online_judge/problemDetails.html', context)


@login_required(login_url='members:login')
def submitProblem(request,problem_id):
    f = request.FILES.get('solution' , False)
    a = request.POST['typedsol']
    if(f):
        with open('/harsh/solution.cpp','wb+') as dest:
            for chunk in f.chunks():
                dest.write(chunk)
    elif(len(a) != 0):
        with open('/harsh/solution.cpp','w') as dest:
            dest.write(a)
    else:
        problem = get_object_or_404(Problem, pk=problem_id)
        messages.info(request, "Please select a file or write code in textarea ")
        context = { 'problem':problem}
        return render(request,'online_judge/problemDetails.html', context)

    os.system('g++ /harsh/solution.cpp ')
    os.system('a.exe < /harsh/input.txt > /harsh/out.txt')


    out1 = '/harsh/out.txt'
    out2 = '/harsh/acc_out.txt'

    if(filecmp.cmp(out1,out2,shallow=False)):
        messages.success(request, 'Your solution was accepted..')
        verdict = 'Accepted'
    else:
        messages.info(request, 'Your solution was not accepted..')
        verdict = 'Wrong answer'

    solution = Solution()
    solution.language = 'cpp'
    solution.problem = Problem.objects.get(pk=problem_id)
    solution.verdict = verdict
    solution.submitted_at = timezone.now()
    solution.submitted_code = '/harsh/solution.cpp'
    solution.save()

    return HttpResponseRedirect(reverse('online_judge:leaderboard'))


@login_required(login_url='users:login')
def leaderboard(request):
    solutions = Solution.objects.all()
    return render(request, 'online_judge/leaderboard.html', {'solutions' : solutions})
