from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from datetime import datetime
from django.contrib.auth.models import User

class History(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    leadimg = models.ImageField(default='myleadimg.jpg')
    body = RichTextField()

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(History, self).save(*args, **kwargs)

    class Meta:
        db_table = 'History'
        managed = True
        verbose_name = 'History'
        verbose_name_plural = 'History'
        
class Stats(models.Model):
    countnumber = models.CharField(max_length=550)
    counttext = models.CharField(max_length=550)
    countnumber1 = models.CharField(max_length=550,null=True,blank=True)
    counttext1 = models.CharField(max_length=550,null=True,blank=True)
    countnumber2 = models.CharField(max_length=550,null=True,blank=True)
    counttext2 = models.CharField(max_length=550,null=True,blank=True)
    countnumber3 = models.CharField(max_length=550,null=True,blank=True)
    counttext3 = models.CharField(max_length=550,null=True,blank=True)

    def __str__(self):
        return self.countnumber

    class Meta:
        db_table = 'Stats'
        managed = True
        verbose_name = 'Stats'
        verbose_name_plural = 'Stats'
       
class Management(models.Model):
    name = models.CharField(max_length=550)
    position = models.CharField(max_length=550)
    leadimg = models.ImageField(default='myleadimg.jpg')
    published = models.BooleanField(default=True,null=True,blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Management'
        managed = True
        verbose_name = 'Management'
        verbose_name_plural = 'Management'

class Staffmembers(models.Model):
    name = models.CharField(max_length=550)
    position = models.CharField(max_length=550)
    leadimg = models.ImageField(default='myleadimg.jpg')
    published = models.BooleanField(default=True,null=True,blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Staffmembers'
        managed = True
        verbose_name = 'Staffmembers'
        verbose_name_plural = 'Staffmembers'

class Facilities(models.Model):
    title = models.CharField(max_length=550)
    leadimg = models.ImageField(default='myleadimg.jpg')
    published = models.BooleanField(default=True)
    flag = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Facilities'
        managed = True
        verbose_name = 'Facilities'
        verbose_name_plural = 'Facilities'
        
class Ourservice(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    leadimg = models.ImageField(default='myleadimg.jpg')
    body = RichTextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Ourservice, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Ourservice'
        managed = True
        verbose_name = 'Ourservice'
        verbose_name_plural = 'Ourservice'

class Dressing(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    body = RichTextField()

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Dressing, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Dressing'
        managed = True
        verbose_name = 'Dressing'
        verbose_name_plural = 'Dressing'

class TuitionAndPayment(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    body = RichTextField()
    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(TuitionAndPayment, self).save(*args, **kwargs)

    class Meta:
        db_table = 'TuitionAndPayment'
        managed = True
        verbose_name = 'TuitionAndPayment'
        verbose_name_plural = 'TuitionAndPayment'

class Discipline(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    body = RichTextField()

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Discipline, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Discipline'
        managed = True
        verbose_name = 'Discipline'
        verbose_name_plural = 'Discipline'

class TimeTable(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    body = RichTextField()

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(TimeTable, self).save(*args, **kwargs)

    class Meta:
        db_table = 'TimeTable'
        managed = True
        verbose_name = 'TimeTable'
        verbose_name_plural = 'TimeTable'

class Blog(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    leadimg = models.ImageField(default='myleadimg.jpg')
    leadimg1 = models.ImageField(null=True,blank=True)
    body = RichTextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Blog'
        managed = True
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'

class Gallery(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    leadimg = models.ImageField(default='myleadimg.jpg')
    published = models.BooleanField(default=True)
    flag = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=datetime.now())
    

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Gallery, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Gallery'
        managed = True
        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery'

class Testimonial(models.Model):
    name = models.CharField(max_length=500,null=True,blank=True)
    indentity = models.CharField(max_length=500,null=True,blank=True)
    leadimg = models.ImageField(default='myleadimg.jpg')
    body = models.TextField()
    date_posted = models.DateTimeField(default=datetime.now())
    published = models.BooleanField(default=True)
    # author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.body

    class Meta:
        db_table = 'Testimonial'
        managed = True
        verbose_name = 'Testimonials'
        verbose_name_plural = 'Testimonials'        

class Contact(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f'{self.fname} {self.lname}'

    class Meta:
        db_table = 'contact'
        managed = True
        verbose_name = 'Contacts'
        verbose_name_plural = 'Contacts' 

class Subscribe(models.Model):
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.email
        