from django.db import models


class Campista(models.Model):
	nome = models.CharField(max_length=100)
	tribo = models.CharField(max_length=100)
	guardiao = models.CharField(max_length=100)

	def __str__(self):
		return self.nome + ' - ' + self.tribo

class Produto(models.Model):
	nome = models.CharField(max_length=100)
	valor = models.DecimalField(max_digits = 6, decimal_places = 2)
	quantidade = models.IntegerField(max_length=3)
	
	def total (self):
		return self.valor*self.quantidade

	
class Compra(models.Model):
	campista = models.ForeignKey(Campista,on_delete=models.CASCADE)
	produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
	pago = models.BooleanField(default = False)