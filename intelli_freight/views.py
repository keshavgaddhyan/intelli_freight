from django.shortcuts import render, redirect


def index(request):
    return render(request, 'intelli_freight/index.html', context=None)

def report(request):
    return render(request, 'intelli_freight/report.html' , {'report': report})