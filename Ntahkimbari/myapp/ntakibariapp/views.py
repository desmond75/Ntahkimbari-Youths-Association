from django.shortcuts import render, redirect
from django.http import HttpResponse #for dev purpose
from .models import Member, Community_work, Post, Event
#from django.contrib.auth import get_user_model
from .forms import SignupForm, LoginForm, UploadProfileForm
from django.utils.translation import ugettext, ugettext_lazy 
from django.contrib.auth import login, authenticate, logout
from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.decorators import login_required

context = {}


def index(request):
	context['funs'] = Post.objects.all().filter(tag='fun').order_by('-post_date')[:6]
	context['recent_activities'] = Post.objects.all().filter(tag='gallery').\
	       order_by('-post_date')[:3]
	context['event'] = Event.objects.all().filter(event_date__gte=timezone.now().\
		   date()).order_by('-post_date')[:1]
	members = Member.objects.all()
	context['male'] = members .filter(sex=['M'])
	context['female'] = members .filter(sex=['F'])
	event = context['event']
	if event:
		context['is_ongoing'] = event[0].event_date == timezone.now().date() and \
		       timezone.now().time() >= event[0].event_time
		# if event_time <= current_time and event_date is == to the current date it 
		# means event has begin else it means event has not yet started or
		# either the event has past and we won't display anything   
	return render(request, 'temp/index.html', context)

def register(request):
	try:
		if request.method == 'POST':
			form = SignupForm(request.POST)
			if form.is_valid():
				form.save()#Add user to db and login user
				password1 = form.cleaned_data['password1']
				username = form.cleaned_data['username']
				user = authenticate(username=username,password=password1)
				login(request, user)
				first_name = form.cleaned_data['first_name']
				messages.success(request, 
					'Welcome <b>{}</b>, your account has been succcessfully created'.format(first_name),
					extra_tags='alert alert-success alert-dismissible fade show'
				)
				return redirect("ntakimbari:dashboard")
		else:
			form = SignupForm()
		context['form'] = form
		context['title'] = 'Register'
		return render(request, 'temp/register.html', context)
	except Exception as e:
			messages.error(request, 'An Error occurred try again',
				extra_tags='alert alert-danger alert-dismissible fade show')
			return render(request, 'temp/register.html', context)

def _login(request):
	try:
		if request.method == 'POST':
			form = LoginForm(request.POST)
			if form.is_valid():
				phone_number = form.cleaned_data['phone_number']
				password = form.cleaned_data['password']
				user = authenticate(username=phone_number,password=password)
				if user:
					login(request, user)
					messages.success(request,
						'You have succcessfully login', 
						extra_tags='alert alert-success alert-dismissible fade show'
					)
					return redirect('ntakimbari:dashboard') 
					#HttpResponse('Succcess {}'.format(request.user))
				#context['error'] = 'Phone number or password is incorrect (Try again)'
				messages.error(request, 'Phone number or password is incorrect (Try again)',
					extra_tags='alert alert-danger alert-dismissible fade show')
				return render(request, 'temp/login.html', context)
		else:
			form = LoginForm()
			context['form'] = form
			context['title'] = 'Login'
		return render(request, 'temp/login.html', context)
	except Exception as e:				
		messages.error(request, 'An Error occurred (Try again)',
				extra_tags='alert alert-danger alert-dismissible fade show')
		return render(request, 'temp/login.html', context)

def organigram(request):
	return render(request, 'temp/organigram.html')

@login_required
def dashboard(request):
	try:
		user = request.user
		paginator = Paginator(Post.objects.all().order_by('-post_date'), 12)
		page = request.GET.get('page')
		all_post = paginator.get_page(page)
		context['name'] = user.last_name
		context['form'] = UploadProfileForm()
		context['all_post'] = all_post
		return render(request, 'temp/dashboard.html', context)
	except Exception as e:
		return HttpResponse('error {}'.format(e))


def community_work(request):
	try:
		works = Community_work.objects.all().order_by('-post_date').exclude(
			date__lt=datetime.now().date()
		)
		completed_works = Community_work.objects.all().exclude(
			date__gt=datetime.now().date()
		)
		context['works'] = works
		context['title'] = 'Community works'
		context['number_of_works'] = len(works)
		#context['completed_works'] = completed_works
		context['number_completed_works'] = len(completed_works)
		return render(request, 'temp/community_work.html', context)
	except Exception as e:
		return HttpResponse('error {}'.format(e))
		#return render(request, 'temp/404.html')

def gallery(request):
	try:
		paginator = Paginator(Post.objects.all().filter(tag='gallery').order_by('-post_date'),4)
		page = request.GET.get('page')
		galleries = paginator.get_page(page)
		context['galleries'] = galleries
		context['title'] = 'Event Galleries'
		context['total_number'] = len(Post.objects.all().filter(tag='gallery'))
		return render(request, 'temp/gallery.html', context)
	except Exception as e:
		return render(request, 'temp/404.html')

def post(request, post_id):
	try:
		post = Post.objects.get(pk=post_id)
		context['post'] = post
		context['related_post'] = Post.objects.all().filter(tag=post.tag)[:5]
		context['title'] = 'Post'
		return render(request, 'temp/post.html', context)
	except Exception as e:
		return render(request, 'temp/404.html',)


def project(request):
	try:
		projects = Post.objects.filter(Q(tag='project') & Q(project_completed=False)
			).all().order_by('-post_date')
		context['projects'] = projects
		context['title'] = 'projects'
		context['on_going'] = 'Project on going'
		return render(request, 'temp/project.html', context)
	except Exception as e:
		#return HttpResponse(e)
		return render(request, 'temp/404.html')


def success(request):
	try:
		paginator = Paginator(Post.objects.filter(
			Q(tag='project') & Q(project_completed=True)).all(),5
		)
		page = request.GET.get('page')
		success_projects = paginator.get_page(page)
		context['success_projects'] = success_projects
		context['title'] = 'Project Completed'
		return render(request, 'temp/success.html', context)
	except Exception as e:
		return render(request, 'temp/404.html')


def event(request, event_id):
	try:
		context['event'] = Event.objects.get(id=event_id)
		context['title'] = 'Upcoming Event at Ntahkimbari'
		return render(request, 'temp/event.html', context)
	except Exception as e:
		return render(request, 'temp/404.html')


def members(request):
	try:
		members = Member.objects.all()
		paginator = Paginator(members,12)
		page = request.GET.get('page')
		members = paginator.get_page(page)
		context['members'] = members
		context['title'] = 'Ntahkimbari Youths'
		return render(request, 'temp/members.html', context)
	except Exception as e:
		return render(request, 'temp/404.html')


def uploadProfile(request, member_id):
	try:
		if request.method == 'POST':			
			member = Member.objects.get(pk=member_id)
			form = UploadProfileForm(request.POST, request.FILES)
			if form.is_valid():
				photo = form.cleaned_data['photo']
				member.photo = photo
				member.save()
				messages.success(
					request,
					'Profile succcessfully uploaded',
					extra_tags='alert alert-success alert-dismissible fade show'
				)
				return redirect('ntakimbari:dashboard')
		return redirect('ntakimbari:dashboard')
	except Exception as e:
		messages.error(
			request, 
			'Error, profile not uploaded (Try again)',
			extra_tags='alert alert-danger alert-dismissible  fade show')
		return redirect('ntakimbari:dashboard') #HttpResponse('error in uploading profile'.capitalize())



