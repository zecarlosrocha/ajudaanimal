import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from crum import get_current_user

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


class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        # extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')

        return self._create_user(email, password, **extra_fields)


class Entidade(AbstractUser):
    phone_regex = RegexValidator(regex=r'^(?:\()[0-9]{2}(?:\))[0-9]{4,5}(?:-)[0-9]{4}$',
                                 message="O número de telefone deve ser inserido no formato exemplo: (15)1122-3344 ou (15)99999-9999. São permitidos até 15 dígitos.")
    email = models.EmailField('E-mail', unique=True)
    nome = models.CharField('Nome', max_length=100)
    fone = models.CharField('Telefone', validators=[phone_regex], max_length=17,
                            blank=True)  # validators should be a list
    site = models.CharField('Site', max_length=500, null=True, blank=True)
    cidade = models.CharField('Cidade', max_length=100)
    uf = models.CharField('UF', max_length=2)
    is_staff = models.BooleanField('Membro da equipe', default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'fone', 'cidade', 'uf']

    def __str__(self):
        return self.email

    objects = UsuarioManager()


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
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'small': (450, 400)}, delete_orphans=True)
    entidade = models.ForeignKey('Entidade', blank=True, null=True,
                                 default=None, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.entidade = user
        super(Animal, self).save(*args, **kwargs)

    @property
    def imagem_small(self):
        print(self.imagem.url)
        img = self.imagem.url.split('.')
        return img[0] + '.small.' + img[1]
