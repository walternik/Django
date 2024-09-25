from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from .models import Page
from .forms import PageForm, SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))

@login_required
def pages(request):
  pages = Page.objects.all().order_by('-joined_date').values()
  context = {
    'pages': pages,
  }
  template = loader.get_template('pages.html')
  return HttpResponse(template.render(context, request))


@login_required
def logout_view(request):
    logout(request)
    template = loader.get_template('logout.html')
    return HttpResponse(template.render({}, request))


def pages_data(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            url_1 = form.cleaned_data['url1']
            url_2 = form.cleaned_data['url2']
            urls = Page.objects.create(url1=url_1, url2=url_2)
            urls.save()
            template = loader.get_template('ok.html')
            return HttpResponse(template.render())
    form = PageForm()
    context = {
        'form': form
    }
    return render(request, 'form.html', context)

@login_required
def compare(request, id):
  page = Page.objects.get(id=id)
  context = {
    'page': page,
  }
  template = loader.get_template('compare.html')
  return HttpResponse(template.render(context, request))


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {
        'form': form
    })