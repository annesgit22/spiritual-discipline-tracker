from django.shortcuts import render, redirect
from .models import SpiritualItem, DailyLog
from .forms import SpiritualItemForm
from datetime import date



def home(request):
    if request.user.is_authenticated:
        items = SpiritualItem.objects.filter(user=request.user)
        today = date.today()

        for item in items:
            item.completed_today = DailyLog.objects.filter(
                item=item,
                date=today,
                completed=True
            ).exists()
    else:
        items = []

    return render(request, 'tracker/home.html', {
        'items': items,
    })



def add_item(request):
    if request.method == 'POST':
        form = SpiritualItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('home')
    else:
        form = SpiritualItemForm()

    return render(request, 'tracker/add_item.html', {'form': form})


def complete_item(request, item_id):
    item = SpiritualItem.objects.get(id=item_id, user=request.user)

    today = date.today()

    log, created = DailyLog.objects.get_or_create(
        item=item,
        date=today,
        defaults={'completed': True}
    )

    if not created:
        log.completed = True
        log.save()

    return redirect('home')
