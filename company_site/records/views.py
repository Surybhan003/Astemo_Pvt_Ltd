from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import csv
from .models import Person
from .forms import PersonForm

@login_required
def dashboard(request):
    total = Person.objects.count()
    recent = Person.objects.order_by('-created_at')[:5]
    return render(request, 'records/dashboard.html', {'total': total, 'recent': recent})

@login_required
def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = PersonForm()
    return render(request, 'records/form.html', {'form': form})

@login_required
def person_list(request):
    query = request.GET.get('query')

    if query:
        persons = Person.objects.filter(name__icontains=query) | Person.objects.filter(age__icontains=query)
    else:
        persons = Person.objects.order_by('-created_at')

    return render(request, 'records/list.html', {'persons': persons})

@login_required
def export_csv(request):
    # export all persons
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="persons.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name','Age','Blood Group','Gender','Weight','Created At'])
    for p in Person.objects.all().order_by('-created_at'):
        writer.writerow([p.name, p.age, p.blood_group, p.get_gender_display(), p.weight, p.created_at])
    return response


@login_required
def edit_person(request, id):
    person = get_object_or_404(Person, id=id)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            person.edit_count += 1
            form.save()
            return redirect('list')
    else:
        form = PersonForm(instance=person)
    return render(request, 'edit.html', {'form': form})
