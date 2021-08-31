from django.shortcuts import render

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