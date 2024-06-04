from django.db import models


class Employees(models.Model):
    PROGRAMMER_CHOICES = (
        ("FULLSTACK", "FULLSTACK"),
        ('BACKEND DEVELOPER', 'BACKEND DEVELOPER'),
        ('FRONT DEVELOPER', 'FRONT DEVELOPER'),
        ('UX-UI', 'UX-UI'),
        ('SYSTEM DEVELOPER', 'SYSTEM DEVELOPER')
    )

    name = models.CharField(max_length=100, verbose_name='Напишите имя сотрудника')
    email = models.EmailField(verbose_name='Укажите вашу почту', default='@gmail.com')
    image = models.ImageField(upload_to='programming_blog/', verbose_name='Загрузите фото')
    about_emp = models.TextField(verbose_name='Опишите сотрудника')
    date_of_birth = models.DateField(verbose_name='Укажите дату рождения')
    programmer_choices = models.CharField(max_length=100, verbose_name='Выберите категорию программиста',
                                          choices=PROGRAMMER_CHOICES)
    rezume = models.FileField(upload_to='rezume/', verbose_name='Загрузите резюме')
    github = models.URLField(verbose_name='Вставьте ссылку на ваш GITHUB')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}-{self.programmer_choices}'

    class Meta:
        verbose_name = 'сотрудника'
        verbose_name_plural = 'сотрудники'
