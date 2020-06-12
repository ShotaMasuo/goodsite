from django.shortcuts import render, redirect
from .scshot import scshotfunc
import os
from .models import UserModel, SiteModel, Comment

# Create your views here.
def index(request):
    sites = SiteModel.objects.all().order_by('-id')
    if request.method == 'POST':
        sitekind = request.POST['sitekind']
        if sitekind == "allkind":
            sites = SiteModel.objects.all().order_by('-id')
        else:
            sites = sites.filter(sitekind=sitekind)
    return render(request, 'index.html', {
        'sites': sites,
    })

def newfunc(request):
    # choicetoselect = SiteModel.SITE_CHOICES
    return render(request, 'new.html')

def createfunc(request):
    sitename = request.POST['sitename']
    sitekind = request.POST['sitekind']
    siteurl = request.POST['siteurl']
    username = request.POST['username']
    password = request.POST['password']
    userinfo = UserModel.objects.filter(name=username)
    userinfo = userinfo.filter(password=password)
    print(userinfo)
    siteCheck = SiteModel.objects.filter(siteurl=siteurl)
    if sitename == "" or sitekind == "" or siteurl == "" or username == "" or password == "":
        sites = SiteModel.objects.all().order_by('-id')
        message = "全ての項目を入力してください"
        return render(request, 'index.html', {
            'sites': sites,
            'message': message,
            })

    if userinfo.first() is not None:
        if siteCheck.first() is None:
            # 全画面スクリーンショット機能
            scshotfunc(siteurl)
            # サイト名.pngになるようにする
            oldname = 'noname.png'
            newname = str(userinfo[0]) + sitename + '.png'
            os.rename('media/' + oldname, 'media/' + newname)
            siteinfo = SiteModel(name=sitename, sitekind=sitekind, siteurl=siteurl, gooduser='', postuser=userinfo[0], images=newname)
            siteinfo.save()
            return redirect('index')
        else:
            message = 'そのサイトはすでに登録されています。'
            sites = SiteModel.objects.all().order_by('-id')
            return render(request, 'index.html', {
            'sites': sites,
            'message': message,
            })
        #     return render(request, 'createuser.html',{
        #     'sitename': sitename,
        #     'sitekind': sitekind,
        #     'siteurl': siteurl,
        #     'message': message,
        # })
    else:
        return render(request, 'createuser.html',{
            'sitename': sitename,
            'sitekind': sitekind,
            'siteurl': siteurl,
        })

def createuser(request):
    sitename = request.POST['sitename']
    sitekind = request.POST['sitekind']
    siteurl = request.POST['siteurl']
    username = request.POST['username']
    password = request.POST['password']
    userinfo = UserModel.objects.filter(name=username)
    userinfo = userinfo.filter(password=password)
    if username == "" or password == "":
        message = 'ユーザー名、パスワードに空欄があります。'
        sites = SiteModel.objects.all().order_by('-id')
        return render(request, 'index.html', {
        'sites': sites,
        'message': message,
        })
    if userinfo.first() is None:
        setuserinfo = UserModel(name=username, password=password, favorite="")
        setuserinfo.save()
        userinfo = UserModel.objects.filter(name=username)
        userinfo = userinfo.filter(password=password)
        # 全画面スクリーンショット機能
        scshotfunc(siteurl)
        # サイト名.pngになるようにする
        oldname = 'noname.png'
        newname = sitename + '.png'
        os.rename('media/' + oldname, 'media/' + newname)
        siteinfo = SiteModel(name=sitename, sitekind=sitekind, siteurl=siteurl, gooduser='', postuser=userinfo[0], images=newname)
        siteinfo.save()
        return redirect('index')
    return redirect('index')

    