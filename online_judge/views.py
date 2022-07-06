from django.shortcuts import get_object_or_404, render,HttpResponse

from .models import Problem, Solution

# Create your views here.

def problems(request):
    problem_list = Problem.objects.all()
    context = { 'problem_list' : problem_list}
    return render(request, 'online_judge/problems.html', context)

def problemDetails(request,problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    context = { 'problem':problem}
    return render(request,'online_judge/problemDetails.html', context)

def submitProblem(request):
    return HttpResponse("Submit Problem Page")

def leaderboard(request):
    return HttpResponse("Leaderboard Page")
