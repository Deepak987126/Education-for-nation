from .forms import StudentForm
from .models import Student
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import messages
# Create your views here.


def student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                messages.success(request, 'Your Registration has been successfully!!!')
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = StudentForm()
    return render(request, 'app1/index.html', {'form': form})


def show(request):
    employees = Student.objects.all()
    return render(request, "app1/show.html", {'employees': employees})


def edit(request, id):
    employee = Student.objects.get(id=id)
    return render(request, 'app1/edit.html', {'employee': employee})


def update(request, id):
    if request.method == 'POST':
        employee = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=employee)
        if form.is_valid():
            messages.success(request, 'Your Record has been updated successfully!')
            form.save()
            return redirect('/show/')

    else:
        employee = Student.objects.get(pk=id)
        form = StudentForm(instance=employee)
    return render(request, 'app1/edit.html', {'form': form, 'id':id})


def destroy(request, id):
    employee = Student.objects.get(id=id)
    employee.delete()
    return redirect("/show")


def search(request):
    reportlist = []
    loc_id = request.POST.get('location')
    if loc_id.is_valid():
        id = Student.objects.get(id=loc_id)
        location_list = StudentForm.objects.filter(title=id)
        for location in location_list:
            reportlist.append(location.report)

