from django.shortcuts import render,redirect
from .models import Contact,Ourservice,Blog,Gallery,Testimonial,History,Facilities,Staffmembers,Management,Stats,Subscribe,Dressing,TuitionAndPayment,Discipline,TimeTable
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):   
    ourservice = Ourservice.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:6]
    testimonial = Testimonial.objects.order_by('-date_posted').filter(published=True)[:6]
    gallery = Gallery.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:6]
    history = History.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:1]
    blog = Blog.objects.order_by('-date_posted').filter(published=True).filter(flag=False)[:3]
    stats = Stats.objects.all()
    
    context = {
        'blog': blog,
        'gallery': gallery,
        'testimonial': testimonial,
        'history': history,
        'ourservice': ourservice,
        'stats': stats
    }

    return render(request,'education/index.html',context)

def about(request):   
    context = { 
    }

    return render(request,'education/about.html',context)

def blogs(request):   
    blog = Blog.objects.order_by('-date_posted').filter(published=True).filter(flag=False)
    paginator = Paginator(blog, 15)
    page = request.GET.get('page')
    paged_blog = paginator.get_page(page)
    
    context = {
        'blog': paged_blog,
    }

    return render(request,'education/blogs.html',context)

def blog(request,slug_id):   
    blog = Blog.objects.filter(slug=slug_id).first()
    context = { 
        'post':blog
    }

    return render(request,'education/blog.html',context)

def history(request,slug_id): 
    history = History.objects.filter(slug=slug_id).first()
      
    context = { 
        'post':history
    }

    return render(request,'education/history.html',context)

def ourservice(request): 
    ourservice = Ourservice.objects.order_by('-date_posted').filter(published=True).filter(flag=False)

    context = { 
        'ourservice': ourservice,
    }

    return render(request,'education/ourservices.html',context)

def ourservices(request,slug_id): 
    ourservices = Ourservice.objects.filter(slug=slug_id).first()
    context = { 
        'post':ourservices
    }
    return render(request,'education/ourservices.html',context)

def stats(request):   
    stats = Stats.objects.all()

    context = {
        'stats': stats
    }

    return render(request,'education/stats.html',context)

def gallery(request):   
    gallery = Gallery.objects.order_by('-date_posted').filter(published=True).filter(flag=False)
    paginator = Paginator(gallery, 20)
    page = request.GET.get('page')
    paged_gallery = paginator.get_page(page)
    
    context = {
        'gallery': paged_gallery,
    }


    return render(request,'education/gallery.html',context)

def contact(request):
  if request.method == 'POST':
    
      try:
          connect = Contact(fname=request.POST['fname'],lname=request.POST['lname'],phone=request.POST['phone'],email=request.POST['email'],message=request.POST['message'])
          messages.success(request,f"{request.POST['fname']} Sent Successfully!!")

          connect.save()
          return redirect('contact')

      except Exception as e:
          messages.error(request,f"Something went wrong...")

  return render(request,'education/contact.html') 

def subscribe(request):
  if request.method == 'POST':
    
      try:
          connect = Subscribe(email=request.POST['email'])
          messages.success(request,f"{request.POST['email']} Sent Successfully!!")

          connect.save()
          return redirect('index')

      except Exception as e:
          messages.error(request,f"Something went wrong...")
  return render(request,'education/index.html') 
  
def dressing(request):   
    dressing = Dressing.objects.order_by('-date_posted').filter(published=True).filter(flag=False)
    context = { 
        'dressing': dressing,
    }

    return render(request,'education/dressing.html',context)

def management(request):   
    management = Management.objects.order_by('-date_posted').filter(published=True).filter(flag=False)
    context = { 
        'management': management,
    }

    return render(request,'education/management.html',context)

def staff_members(request):   
    staffmembers = Staffmembers.objects.order_by('-date_posted').filter(published=True).filter(flag=False)
    context = { 
        'staffmembers': staffmembers,
    }

    return render(request,'education/staff_members.html',context)

def facilities(request):   
    facilities = Facilities.objects.order_by('-date_posted').filter(published=True).filter(flag=False)
    context = { 
        'facilities': facilities,
    }

    return render(request,'education/facilities.html',context)

def time_table(request):   
    timetable = TimeTable.objects.order_by('-date_posted').filter(published=True).filter(flag=False)
    context = { 
        'timetable': timetable,
    }

    return render(request,'education/time_table.html',context)

def discipline(request):   
    discipline = Discipline.objects.order_by('-date_posted').filter(published=True).filter(flag=False)
    context = { 
        'discipline': discipline,
    }

    return render(request,'education/discipline.html',context)

def tuition_and_payment(request):   
    tuition_and_payment = TuitionAndPayment.objects.order_by('-date_posted').filter(published=True).filter(flag=False)
    context = { 
        'tuition_and_payment': tuition_and_payment,
    }

    return render(request,'education/tuition_and_payment.html',context)

