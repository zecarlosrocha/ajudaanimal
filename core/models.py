import uuid
from django.db import models

from stdimage.models import StdImageField
from django.core.validators import RegexValidator


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Entidade(Base):
    phone_regex = RegexValidator(regex=r'^(?:\()[0-9]{2}(?:\))[0-9]{4,5}(?:-)[0-9]{4}$',
                                 message="O número de telefone deve ser inserido no formato exemplo: (15)1122-3344 ou (15)99999-9999. São permitidos até 15 dígitos.")
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    site = models.CharField(max_length=500, null=True, blank=True)
    fone = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list

    class Meta:
        verbose_name = 'Entidade'
        verbose_name_plural = 'Entidades'

    def __str__(self):
        return self.nome


class Especie(Base):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.CharField('Descrição', max_length=150)

    class Meta:
        verbose_name = 'Especie'
        verbose_name_plural = 'Especies'

    def __str__(self):
        return self.nome


class Raca(Base):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.CharField('Descrição', default="", max_length=150)
    especie = models.ForeignKey('Especie', on_delete=models.RESTRICT)

    class Meta:
        verbose_name = 'Raça'
        verbose_name_plural = 'Raças'

    def __str__(self):
        return self.nome


class Animal(Base):
    nome = models.CharField('Nome', max_length=50)
    idade = models.IntegerField('Idade')
    raca = models.ForeignKey('Raca', on_delete=models.RESTRICT)
    entidade = models.ForeignKey('Entidade', on_delete=models.RESTRICT)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'large': (480, 480)}, delete_orphans=True)

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'

    def __str__(self):
        return self.nome
