from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Cloth, Cloth3
# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def index(request):
    return render(request, 'text/index.html')


def s1(request):
    return render(request, 'text/s1.html')


def s2(request):
    return render(request, 'text/s2.html')


def s3(request):
    return render(request, 'text/s3.html')


'''def s4(request):
    return render(request, 'text/s4.html')


def s4_1(request):
    return render(request, 'text/s4_1.html')


def s4_2(request):
    return render(request, 'text/s4_2.html')


def s4_3(request):
    return render(request, 'text/s4_3.html')


def s4_4(request):
    return render(request, 'text/s4_4.html')


def s4_5(request):
    return render(request, 'text/s4_5.html')


def s4_6(request):
    return render(request, 'text/s4_6.html')


def s4_7(request):
    return render(request, 'text/s4_7.html')


def s4_8(request):
    return render(request, 'text/s4_8.html')


def s4_9(request):
    return render(request, 'text/s4_9.html')'''


def s5(request):
    return render(request, 'text/s5.html')


def s6(request):
    return render(request, 'text/s6.html')


def s7(request):
    return render(request, 'text/s7.html')


def text(request, question_id):
    question = get_object_or_404(Cloth, pk=question_id)
    return render(request, 'text/text.html', {'question': question})


def textva(request, question_id):
    question = get_object_or_404(Cloth, pk=question_id)

    question.is_used = True
    question.save()

    return HttpResponseRedirect(reverse('text:ans', args=(question.id,)))


def textvb(request, question_id):
    question = get_object_or_404(Cloth, pk=question_id)

    question.is_used = False
    question.save()

    return HttpResponseRedirect(reverse('text:ans', args=(question.id,)))


def ans(request, question_id):
    question = get_object_or_404(Cloth, pk=question_id)
    return render(request, 'text/ans.html', {'question': question})


def textcollect(request):
    question = Cloth.objects.order_by()
    return render(request, 'text/textcollect.html', {'question': question})


def text2(request, question_id):
    question = get_object_or_404(Cloth3, pk=question_id)
    return render(request, 'text/text2.html', {'question': question})


def textva2(request, question_id):
    question = get_object_or_404(Cloth3, pk=question_id)

    question.is_used = True
    question.save()

    return HttpResponseRedirect(reverse('text:ans2', args=(question.id,)))


def textvb2(request, question_id):
    question = get_object_or_404(Cloth3, pk=question_id)

    question.is_used = False
    question.save()

    return HttpResponseRedirect(reverse('text:ans2', args=(question.id,)))


def ans2(request, question_id):
    question = get_object_or_404(Cloth3, pk=question_id)
    return render(request, 'text/ans2.html', {'question': question})


def textcollect2(request):
    question = Cloth3.objects.order_by()
    return render(request, 'text/textcollect2.html', {'question': question})
