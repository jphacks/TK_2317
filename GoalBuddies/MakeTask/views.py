from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
from django.shortcuts import get_object_or_404, redirect

@login_required
def account_view(request):
    return render(request, 'MakeTask/account.html')

@login_required
def mtask_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user  # ユーザーを設定
            new_task.save()
            form.save_m2m()  # ManyToManyフィールドを保存
            return redirect('account')  # accountページへリダイレクト
    else:
        form = TaskForm()  # 空のフォームを作成

    return render(request, 'MakeTask/mtask.html', {'form': form})

@login_required
def account_view(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'MakeTask/account.html', {'tasks': tasks})

def edit_task_view(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = TaskForm(instance=task)

    return render(request, 'MakeTask/edit_task.html', {'form': form})

@login_required
def remove_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('account')
