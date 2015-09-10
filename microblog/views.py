from django.shortcuts import render, render_to_response,HttpResponse,redirect,RequestContext
from microblog.forms import UserForm,LoginForm,BlogForm
from microblog.models import *
# Create your views here.

def Hello(request):
    return HttpResponse('Hello')

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST.copy())
        if form.is_valid():

            select = User.objects.all().filter(name__contains=form.cleaned_data['name'])
            if select == None or len(select)==0:
                return redirect('/login')
            else:
                request.session['login'] = True
                request.session['name'] = form.cleaned_data['name']
                return redirect('/index')
        else:
            print(form.errors)
    return render_to_response('login.html', context_instance=RequestContext(request))

def Index(reqeust):

    parm={'login':False}
    if reqeust.session.has_key('login') and reqeust.session['login'] == True:
        parm['login'] = True
        parm['name'] = reqeust.session['name']
        user = User.manager.get_query_user(parm['name'])
        blogs = user[0].blogs.all()
        contents=[]
        for v in blogs:
            print v.title
            contents.append({'title':v.title,'content':v.content})
        parm['contents'] = contents

    return render_to_response('index.html', parm)


def Write(request):
    if request.method == 'POST':
        form = BlogForm(request.POST.copy())
        if form.is_valid():
            newblog = form.save();
            user = User.objects.all().filter(name__contains=request.session['name'])
            user[0].blogs.add(newblog)
            user[0].save()

           # print newblog.user_set.all()[0]

            return redirect('/index')
        else:
            print(form.errors)
    else:
        return render_to_response('Write.html', context_instance=RequestContext(request))

def Add(requset):

    if requset.method == 'POST':
        form = UserForm(requset.POST.copy())
        if form.is_valid():
            newUser = form.save()
            return render_to_response('index.html',context_instance=RequestContext(requset))
        else:
            print(form.errors)
            return render_to_response('adduser.html', context_instance=RequestContext(requset))

    return render_to_response('adduser.html',context_instance=RequestContext(requset))