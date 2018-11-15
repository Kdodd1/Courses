from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Course, Description

def index(request):
	context = {
	"courses": Course.objects.all(),
	"descriptions": Description.objects.all()
	}

	return render(request, "courseapp/index.html", context)

def process(request):
	errors = Course.objects.basic_validator(request.POST)
	if len(errors):
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	else:
		Course.objects.create(name = request.POST['name'])
		course = Course.objects.last()
		courseid = course.id
		Description.objects.create(description = request.POST['description'], courseDesc_id = courseid)

		return redirect('/')
def delete(request, number):
	context = {
	"courses": Course.objects.get(id=(number)),
	"descriptions": Description.objects.get(courseDesc_id = (number))
	}

	return render(request, "courseapp/delete.html", context)

def remove(request, number):
	course = Course.objects.get(id=(number))
	course.delete()

	return redirect('/')