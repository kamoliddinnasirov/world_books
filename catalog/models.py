from django.db import models
from django.urls import reverse 


class Genre(models.Model):
    name = models.CharField(max_length=200, 
                            help_text="Kitobning janrini kiriting!")
    
    def __str__(self) -> str:
        return self.name 
    


class Language(models.Model):
    name = models.CharField(max_length=20, 
                            help_text="Kitobning tilini kiriting!",
                            verbose_name="Kitobning tili")
    

    def __str__(self) -> str:
        return self.name
    



class Publisher(models.Model):
    name = models.CharField(max_length=20,
                            help_text="Nashriyotning nomini kiriting!",
                            verbose_name="Nashriyot nomi")
    

    def __str__(self) -> str:
        return self.name
    




class Status(models.Model):
    name = models.CharField(max_length=20, 
                            help_text="Kitobning statusini kiriting!",
                            verbose_name="Kitobning statusi")
    
    def __str__(self) -> str:
        return self.name
    


class Author(models.Model):
    first_name = models.CharField(max_length=100,
                                  help_text="Kitobning Avtorini kiriting",
                                  verbose_name="Kitobning Avtori")
    last_name = models.CharField(max_length=100, 
                                 help_text="Avtorning familyasini kiriting",
                                 verbose_name="Avtor familyasi")
    date_of_birth = models.DateField(help_text="Avtorning tug'ilgan kunini kiriting!",
                                     verbose_name="Tug'ilgan kuni",
                                     null=True, blank=True)
    
    about = models.TextField(help_text="Avtor haqida ma'lumot!",
                             verbose_name="Avtor haqida")
    photo = models.ImageField(upload_to="author/%Y/%m/%d",
                              help_text="Avtorning rasmini kiriting",
                              verbose_name="Avtor rasmi",
                              null=True, blank=True)
    
    def __str__(self) -> str:
        return self.last_name
    


class Book(models.Model):
    title = models.CharField(max_length=200, 
                             help_text="Kitobning nomini tanlang", 
                             verbose_name="Kitobning nomi")
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE,
                              help_text="Kitobning janrini tanlang",
                              verbose_name="Kitobning janri",
                              null=True)
    language = models.ForeignKey("Language", on_delete=models.CASCADE,
                                 help_text="Kitobning tilini tanlang",
                                 verbose_name="Kitobning tili",
                                 null=True)
    publisher = models.ForeignKey("Publisher", on_delete=models.CASCADE,
                                  help_text="Nashriyotni tanlang",
                                   verbose_name="Nashriyot")
    year = models.CharField(max_length=4, 
                            help_text="Kitobning chiqarilgan yilini kiriting!",
                            verbose_name="Kitobning yili")
    author = models.ManyToManyField("Author", help_text="Kitobning Avtor (Avtorlari) tanlang",
                                    verbose_name="Kitobning Avtor(Avtorlari)")
    
    summary = models.TextField(max_length=1000, 
                               help_text="Kitob haqida xulosangizni kiriting!")
    

    isbn = models.CharField(max_length=13, help_text="Uzunligi 13 ta belgidan iborat bo'lsin",
                            verbose_name="Kitobning ISBN")
    price = models.DecimalField(decimal_places=2, max_digits=7, help_text="Kitobning narxini kiriting!",
                                verbose_name="Narx (sum)")
    photo = models.ImageField(upload_to="books/%Y/%m/%d",
                              help_text="Kitobning rasmini kiriting!",
                              verbose_name="Kitobning rasmi")
    

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.id)])
    


class BookInstance(models.Model):
    book = models.ForeignKey("Book",
                             on_delete=models.CASCADE, null=True)
    inv_nom = models.CharField(max_length=20, null=True,
                               help_text="Kitobning inventar nomerini kiriting!",
                               verbose_name="Inverntar nomer")
    status = models.ForeignKey("Status", on_delete=models.CASCADE,
                               null=True)
    due_back = models.DateField(null=True, blank=True,
                                help_text="Kitobning status tugash vaqti")
    

    class Meta:
        ordering = ['due_back']

    def __str__(self) -> str:
        return '%s %s %s' % (self.inv_nom, self.book, self.status)
