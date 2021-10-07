from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from django.http import JsonResponse
from django.core import serializers

from .forms import CustomerForm

from .models import Choice, Question, Formulario, Profile


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    # tem aver com o de cima 
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def formulario(request):
    form1 = CustomerForm()
    form2 = CustomerForm()
    
    print(len(request.POST))
    if request.method == 'POST':
        form1 = CustomerForm( request.POST,prefix="form1")
        form2 = CustomerForm( request.POST,prefix="form2")
        print(request.POST)
        if form1.is_valid() or form2.is_valid(): 
            form1.save()
            form2.save()

    context = {
        'form1': form1,
        'form2': form2,
    }

    return render(request, 'polls/form.html', context)


def indextwo(request):
    return render(request, 'polls/indextwo.html')

def load_post_data_view(request):
    qs = Profile.objects.all()
    data = serializers.serialize('json', qs) # serializando
    return JsonResponse({'data': data})

def hello_world_view(request):
    return JsonResponse({'text': 'hello world 2x'})        