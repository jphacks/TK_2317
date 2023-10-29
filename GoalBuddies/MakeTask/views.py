from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task,Match
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, Message
from .forms import TaskForm, MessageForm
from django.contrib.auth.decorators import login_required


@login_required
def account_view(request):
    tasks = Task.objects.filter(user=request.user)
    matches = Match.objects.filter(task1__user=request.user) | Match.objects.filter(task2__user=request.user)

    return render(request, 'MakeTask/account.html', {
        'tasks': tasks,
        'matches': matches
    })

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

@login_required
def task_detail_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    messages = task.messages.all()
    new_message = None

    if request.method == 'POST':
        message_form = MessageForm(data=request.POST)
        if message_form.is_valid():
            new_message = message_form.save(commit=False)
            new_message.sender = request.user
            new_message.task = task
            new_message.save()
            return redirect('task_detail', task_id=task.id)
    else:
        message_form = MessageForm()

    return render(request, 'MakeTask/task_detail.html', {
        'task': task,
        'messages': messages,
        'new_message': new_message,
        'message_form': message_form
    })

@login_required
def match_task_view(request, task_id):
    my_task = get_object_or_404(Task, id=task_id, user=request.user)
    matching_tasks = Task.objects.filter(duration=my_task.duration).exclude(user=request.user)

    for task in matching_tasks:
        Match.objects.create(task1=my_task, task2=task)

    return redirect('account')