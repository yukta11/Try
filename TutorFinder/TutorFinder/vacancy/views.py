from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from .models import prof
# Create your views here.

def vacancyform(request):
	if request.method == 'POST':
		fname = request.POST['firstname']
		lname = request.POST['lastname']
		date_of_birth = request.POST['date_of_birth']
		qualifications = request.POST['qualification']
		experience = request.POST['experience']
		salary = request.POST['salary']
		image = request.FILES.get('image', None)
		
		professor = prof.objects.create(fname=fname, lname=lname, date_of_birth=date_of_birth, qualifications=qualifications, experience=experience, salary=salary, image=image)
		professor.save()
		return redirect("home")

	else:
		return render(request, "vacancy/vacancyform.html")

def home(request):
	professors = prof.objects.all()
	return render(request,'home.html',{"professors":professors})
