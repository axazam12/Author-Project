from django.shortcuts import render , redirect
from . models import Book, Publisher
from . forms import PublisherForm, BookForm
from django.core.paginator import Paginator,EmptyPage
from django.db.models import Q




def publisher(request):
    pub=Publisher.objects.all()
    if request.method=='POST':
        publisher=request.POST.get('publisher')
        book=Publisher(name=publisher)
        book.save()
    return render(request,'book.html',{'pub':pub})

def DetailsBook(request,book_id):
    book=Book.objects.get(id=book_id)
    return render(request,'admin/detailbook.html',{'book':book})



def DeleteBook(request,book_id):
    book=Book.objects.get(id=book_id)
    if request.method=='POST':
        book.delete()
        return redirect('/')

    return render(request,'admin/deletebook.html',{'book':book})

def CreateBook(request):
    books=Book.objects.all()
    if request.method=='POST':
        form=BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=BookForm()
    return render(request,'admin/book.html',{'form':form,'books':books})

def CreatePublisher(request):
    if request.method=='POST':
        form=PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=PublisherForm()
    return render(request,'admin/publisher.html',{'form':form})


def UpdateBook(request,book_id):
    book=Book.objects.get(id=book_id)
    if request.method=='POST':
        form=BookForm(request.POST,request.FILES,instance=book)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=BookForm(instance=book)
    return render(request,'admin/updatebook.html',{'form':form})


def index(request):


    return render(request,'admin/base.html')

def ListBooks(request):
    books=Book.objects.all()
    
    paginator=Paginator(books,4)
    page_number=request.GET.get('page')

    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)


    return render(request,'admin/listbook.html',{'books':books,'page':page})


def SearchBook(request):
    query=None
    books=None

    if 'q' in request.GET:
        query=request.GET.get('q')
        books=Book.objects.filter(Q(title__icontains=query) | Q(publisher__name__icontains=query) | Q(author__icontains=query))
    else:
        books=[]
    
    return render(request,'admin/search.html',{'books':books,'query':query})