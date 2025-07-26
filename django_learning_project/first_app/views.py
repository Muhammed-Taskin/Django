from django.shortcuts import render
from django.http import HttpResponse,  Http404, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse # bu kütüphane pathlerdeki nameler  ile işlem yapmamızı sağlar.
#pythonda web sitesi içerisinde çalışılacak ve gösterilicek fonksiyonların yazıldıği kısımdır.
# Create your views here.

course_dictionary = {
    "python" : "Python is a high level programming language",
    "java" : "Java is a high level programing language",
    "Swift" : "Swift is a high level programming language"
}


def index(request):
    return HttpResponse("Hello World")#cevap döndürüyor.

def course(request,item ):
    try:
        course = course_dictionary[item]
        return HttpResponse(course)
    except:
        return HttpResponseNotFound("Not Found!!")
    #return HttpResponse(course_dictionary.get(item,"Not Found!!"))
def multiply_view(requests, num1, num2):
    return HttpResponse(f"{num1} * {num2} = {num1 * num2}")

def course_number(request, num1):
    course_list = list(course_dictionary.keys())
    course_2 = course_list[num1]
    page_to_go = reverse("course", args = [course_2])
    return HttpResponseRedirect(page_to_go)
    #reverse fonksiyonu ile url'ye yönlendirme yaptık.
    #link yönlendirme yaptık.
