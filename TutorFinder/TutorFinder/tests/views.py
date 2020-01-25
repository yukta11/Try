from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from.models import Tutor_profile

def Search(request):
	context= {}
	query =""

	if request.GET:
		query = request.GET['q']
	tutors= get_data_queryset(query)
	context={'tutors':tutors}


	return render(request,"home.html",context)


def get_data_queryset(query=None):
	queryset = []
	queries = query.split(" ") 
	for q in queries:
		tutors = Tutor_profile.objects.filter(

			Q(fname__icontains=q)|
			Q(lname__icontains=q)
		)

		for tutor in tutors:
			queryset.append(tutor)
			
	return List(set(queryset))

