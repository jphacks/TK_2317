from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def account_view(request):
    return render(request, 'MakeTask/account.html')