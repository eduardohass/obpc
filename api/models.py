from django.db import models
from django.utils import timezone

# Create your models here.
UF_CHOICES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranão'),
        ('MG', 'Minas Gerais'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PE', 'Pernanbuco'),
        ('PI', 'Piauí'),
        ('PR', 'Paraná'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('RS', 'Rio Grande do Sul'),
        ('SC', 'Santa Catarina'),
        ('SE', 'Sergipe'),
        ('SP', 'São Paulo'),
        ('TO', 'Tocantins')
    )

class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    primeiroNome = models.CharField(max_length=50)
    ultimoNome = models.CharField(max_length=50)
    isMembro = models.BooleanField()
    dtCriacao = models.DateTimeField(auto_now_add=True)
    #usuarioCriacao = models.IntegerField()
    dtAlteracao = models.DateTimeField(auto_now_add=True)
    #usuarioAlteracao = models.IntegerField()

    def __str__(self):
        return self.primeiroNome + ' ' + self.ultimoNome

class Endereco(models.Model):
    class Meta:
        verbose_name_plural = "Endereços"

    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50, default="")
    logradouro = models.CharField(max_length=50)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=50, choices=UF_CHOICES, verbose_name="Estado")
    dtCriacao = models.DateTimeField(default=timezone.datetime.now, editable=False)
    #usuarioCriacao = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name="endereco_usuario_criacao")
    dtAlteracao = models.DateTimeField(auto_now_add=True)
    #usuarioAlteracao = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name="endereco_usuario_alteracao")

    def __str__(self):
        return self.descricao

class Regional(models.Model):
    class Meta:
        verbose_name_plural = "Regionais"

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    responsavel = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name="regional_pessoa_responsavel")
    dtCriacao = models.DateTimeField(default=timezone.datetime.now, editable=False)
    #usuarioCriacao = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name="regional_usuario_criacao")
    dtAlteracao = models.DateTimeField(auto_now_add=True)
    #usuarioAlteracao = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name="regional_usuario_alteracao")

    def __str__(self):
        return self.nome

class Log(models.Model):
    id = models.AutoField(primary_key=True)
    erro = models.CharField(max_length=255)
    linha = models.IntegerField()
    metodo = models.CharField(max_length=100)
    pagina = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.erro

class Grupo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    idRegional = models.ForeignKey(Regional)
    membros = models.ManyToManyField(Pessoa, verbose_name="Membros")
    idEndereco = models.ForeignKey(Endereco)
    horaInicio = models.CharField(max_length=5, verbose_name="Início")
    horaFim = models.CharField(max_length=5, verbose_name="Fim")
    lider = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name="grupo_pesssoa_lide", verbose_name="Líder")
    viceLider = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name="grupo_pessoa_vice_lider", verbose_name="Vice Líder")
    dtCriacao = models.DateTimeField(default=timezone.datetime.now, editable=False)
    # usuarioCriacao = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name="grupo_usuario_criacao")
    dtAlteracao = models.DateTimeField(auto_now_add=True)
    # usuarioAlteracao = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name="grupo_usuario_alteracao")

    def __str__(self):
        return self.nome