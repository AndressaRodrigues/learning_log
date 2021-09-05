from django.shortcuts import renderfrom django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Topic
from .forms import TopicForm

# Create your views here.

def index(request):
    #chama a página inicial
    return render(request, 'learning_logs/index.html')

def topics(request):
    #mostra os assuntos
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    #mostra um único assunto e todas as suas entradas
    topic = Topics.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    #adiciona um novo assunto
    if request.method != 'POST':
        #nenhum dado submetido, cria um formulário em branco
        form = TopicForm()

    else:
        #se recebe dados do POST, processa-os
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))


    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
