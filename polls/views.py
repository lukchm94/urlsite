from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question, Invoice
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(has_choices=True, pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class QuestionView(generic.ListView):
    template_name = 'polls/questions.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(has_choices=True, pub_date__lte=timezone.now()).order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class InvoicesView(generic.ListView):
    template_name = 'polls/show_inv.html'
    context_object_name = 'invoices'

    def get_queryset(self):
        return Invoice.objects.filter(inv_date__lte=timezone.now())


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))

def create_invoice(request):
    return render(request, 'polls/create_invoice.html')
'''
    #new_invoice = get_object_or_404(Invoice)
    try:
        new_invoice = Invoice().save()
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request,'polls/index.html',context)

def index(request):
    latest_question_lists = Question.objects.order_by('-pub_date')[:5]
    #output = ', </br>'.join([q.question_text for q in latest_question_lists])
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_lists,
    }
    return HttpResponse(template.render(context,request))
    #return HttpResponse(output)
    #return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'polls/detail.html',{'question': question})
    #return HttpResponse("You're <b>looking</b> at question %s." %question_id)


def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/results.html',{'question':question})

def results(request, question_id):
    response = "<!DOCTYPE html>" \
               "<html><body>" \
               "<h1>My first web url</h1>" \
               "</body></html>" \
               "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
'''