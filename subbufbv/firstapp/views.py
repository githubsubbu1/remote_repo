from django.shortcuts import render,redirect
from firstapp.forms import EmployeeForm
from firstapp.models import Employee
def home_view(request):
    emp=Employee.objects.all()
    return render(request,'firstapp/home.html',{'emp':emp})
def insert_view(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'firstapp/insert.html',{'form':form})
def delete_view(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return redirect('/')
def update_view(request,id):
    emp=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
        return redirect('/')    
    return render(request,'firstapp/update.html',{'emp':emp})
