from django.db import models

# Create your models here.

class Atividade(models.Model):
    atv_id = models.IntegerField(primary_key=True)
    atv_descricao = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "atividade"


class Objeto(models.Model):
    obj_id = models.IntegerField(primary_key=True)
    obj_descricao = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "objeto"


class Distrito(models.Model):
    dst_id = models.IntegerField(primary_key=True)
    dst_descricao = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "distrito"


class Cidade(models.Model):
    cid_id = models.IntegerField(primary_key=True)
    cid_descricao = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "cidade"


class Equipamento(models.Model):
    eqp_id = models.IntegerField(primary_key=True)
    eqp_descricao = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "equipamento"


class Estabelecimento(models.Model):
    nipcc = models.IntegerField(primary_key=True)
    denominacao = models.CharField(max_length=255)
    atv_id = models.ForeignKey(Atividade, on_delete=models.CASCADE, db_column="atv_id")
    obj_id = models.ForeignKey(Objeto, on_delete=models.CASCADE, db_column="obj_id")
    sede_cep = models.IntegerField()
    sede_endereco = models.CharField(max_length=255)
    cid_id = models.ForeignKey(Cidade, on_delete=models.CASCADE, db_column="cid_id")
    dst_id = models.ForeignKey(Distrito, on_delete=models.CASCADE, db_column="dst_id")
    cep_intervencao = models.IntegerField()
    end_intervencao = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    confirmacao_senha = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "estabelecimento"
