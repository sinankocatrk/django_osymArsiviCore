from pickle import FALSE
from django.db import models

# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Kontenjan(models.Model):

    tip = models.CharField(max_length=100,blank=False)
    kodu = models.CharField(max_length = 10)
    sbkodu = models.CharField(max_length = 7)
    kurumadı = models.CharField(max_length = 70)
    sehir = models.CharField(max_length = 17)
    sayi = models.CharField(max_length = 17) 

    class Meta:
        abstract = True
        
    def __str__(self):
        return 'Tip: {0} Kurum Adı: {1}'.format(self.tip, self.kurumadı)

class Ebe(Kontenjan):
    pass

class Hemsire(Kontenjan):
    pass






"""class Comment(models.Model):
    nick = models.ForeignKey(Kontenjan,on_delete = models.CASCADE,verbose_name = "Makale",related_name="comments")
    comment_author = models.CharField(max_length = 50,verbose_name = "İsim")
    comment_content = models.CharField(max_length = 200,verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']
"""