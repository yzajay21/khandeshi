from django.shortcuts import render,redirect
from .forms import RegisterProfileForm
# Create your views here.


def home(request):
	hello = "hello"
	context = {
		'hello' : hello,
	}
	return render(request,"base.html",context)

def thanks(request):
	return render(request,"thanks.html",{})
def register(request):
	#if request.method == 'POST':
	form = RegisterProfileForm(request.POST or None)
	if form.is_valid():
		form_item = form.save(commit=False)
		form_item.save()
		return redirect("thanks")
	else:
		form = RegisterProfileForm()
		print("invalid")
	context = {
	 'form' : form,
	}
	return render(request,"form.html",context)



