from django.db import models

# Create your models here.

class Topic(models.Model):
    #assunto do tópico
    txt = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        #develve uma representação em string do modelo 
        return self.text


class Entry(models.Model):
    #algo específico aprendido sobre um assunto
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)


    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        # devolve uma representação em string do modelo
        return self.text[:50] + "..."