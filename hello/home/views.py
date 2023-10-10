
from django.shortcuts import render,redirect
from datetime import datetime
from home.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.db.models import Q,Avg,Sum
from .serializers import *
import math
from rest_framework import status
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required



# pass=jeel3705#.>
#add=jeeljivani,jeeljivani

def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'Username already tacken')
            return redirect('/register')
        user = User.objects.create(
             first_name = first_name , last_name = last_name , username = username ,email=email    
        )
        user.set_password(password)
        user.save()
        messages.info(request,'Account Created')

        return redirect('/login')


    return render(request,'users/register.html')


def loginuser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not User.objects.filter(username=username).exists():
            messages.error(request,"Invalid Username")
            return redirect('/login')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            messages.info(request,'Invalid Password')
            return render(request,'login.html')
    
    return render(request,'users/login.html',)


def logoutuser(request):
    logout(request)
    return redirect('/login')

@login_required()
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')


@login_required()
def players(request):  
    queryset= Player.objects.all()

    if request.GET.get('search'):
        queryset=queryset.filter(Q(player_name__icontains= request.GET.get('search'))|Q(position__position__icontains= request.GET.get('search')))

    context={'player':queryset}
    return render(request,'player/players.html',context)


@login_required()
def see_ratings(request,player_id):
    queryset = SpecsRating.objects.filter(player__player_id__player_id = player_id)
    allrating= queryset.aggregate(allrating=((Avg('rating'))))
    val = allrating.get("allrating")
    val = math.ceil(val)
    allrating["allrating"] = val
    current_rank = -1
    i=1
    ranks=Player.objects.annotate(ratings = Sum('playerrating__rating')).order_by('-ratings','-player_age')

    for rank in ranks:
        if player_id == rank.player_id.player_id:
            current_rank = i 
            break
        i += 1

    return render(request,'player/see_ratings.html',{'queryset': queryset , 'allrating': allrating , 'current_rank':current_rank})


@login_required()  
def about(request):
    return render(request,'about.html',)


@login_required()
def contact(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        contact=Contact(fname=fname,lname=lname,email=email,comment=comment,date=datetime.today())
        contact.save()
        messages.success(request, "Your message send successfully.")

    return render(request,'contact.html')

@login_required()
def blog(request):  
    if request.method == "POST":
        data = request.POST
        blog_image=request.FILES.get('blog_image')
        blog_name = data.get('blog_name')
        blog_desc = data.get('blog_desc')
        blog=Blog(blog_image=blog_image,blog_desc=blog_desc,blog_name=blog_name)
        blog.save()
        return redirect('/blog')
    queryset= Blog.objects.all()
    
    if request.GET.get('search'):
        queryset=queryset.filter(blog_name__icontains= request.GET.get('search'))

    context = {'blog': queryset}
        
    return render(request,'blog/blog.html',context)

def delete_blog(request,id):
    queryset = Blog.objects.get(id=id)
    queryset.delete()
    return redirect('/blog')

def update_blog(request,id):
    queryset = Blog.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        blog_image=request.FILES.get('blog_image')
        blog_name = data.get('blog_name')
        blog_desc = data.get('blog_desc')
        queryset.blog_name= blog_name
        queryset.blog_desc=blog_desc
        if blog_image:
            queryset.blog_image=blog_image
        queryset.save()
        return redirect('/blog/')

    context={'blog':queryset}

    return render(request,'blog/update_blog.html',context)

# @method_decorator(csrf_exempt,name='dispatch')
# class StudentApi(View):
#     def get(self,request,*args, **kwargs):
#         json_data = request.body    
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream) 
#         id = pythondata.get('id',None)
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             json_data = JSONRenderer().render(serializer.data)  
#             return HttpResponse(json_data,content_type="application/json")
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         json_data = JSONRenderer().render(serializer.data)  
#         return HttpResponse(json_data,content_type="application/json")
    
#     def post(self,request,*args, **kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         serializer=StudentSerializer(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'Data Created'}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')

        
#     def put(self,request,*args, **kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         id=pythondata.get('id')
#         stu = Student.objects.get(id=id)
#         serializer=StudentSerializer(stu,data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'data updated'}
#             json_data=JSONRenderer().render(res)
#             return HttpResponse(json_data,content_type='application/json')
        
    
        
#     def delete(self,request,*args, **kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         pythondata=JSONParser().parse(stream)
#         id=pythondata.get('id')
#         stu=Student.objects.get(id=id)
#         stu.delete()
#         res={'msg':'Data Deleted'}
#         return JsonResponse(res,safe=False)
    


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request,pk=None):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        id= pk
        stu =Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        id= pk
        stu =Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data deleted'})


    if request.method == 'GET':
     id = pk
     if id is not None:
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu)
        return Response(serializer.data)   
    stu = Student.objects.all ()
    serializer = StudentSerializer (stu, many=True)
    return Response(serializer.data)




        
    






