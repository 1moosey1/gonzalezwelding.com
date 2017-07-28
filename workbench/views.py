from django.shortcuts import render


# Render workbench home
def workbench(request):
    return render(request, 'workbench/base.html')
