from django.db import models

# Create your models here.

# Модель категорій іграшок
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")
    description = models.TextField(verbose_name="Опис категорії", blank=True)

    def __str__(self):
        return self.name

# Модель іграшок
class Toy(models.Model):
    # Вибір статі
    GENDER_CHOICES = [
        ('M', 'Для хлопчиків'),
        ('F', 'Для дівчаток'),
        ('U', 'Універсальна')
    ]
    
    name = models.CharField(max_length=100, verbose_name="Назва іграшки")
    description = models.TextField(verbose_name="Опис іграшки", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=19.99, verbose_name="Ціна")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Кількість")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U', verbose_name="Призначення")
    age_group = models.CharField(max_length=50, default="3+", verbose_name="Вікова категорія")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    image = models.ImageField(upload_to='toys/', blank=True, null=True, verbose_name="Зображення")

    def __str__(self):
        return self.name
