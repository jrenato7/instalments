from django.db import models

from instalments.base_model import TimeStamp


class Client(TimeStamp):
    name = models.CharField(max_length=200, null=True, verbose_name='Nome')
    email = models.EmailField(max_length=254, null=True, verbose_name='E-mail')
    activate = models.BooleanField(default=False, verbose_name='Ativado')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Account(TimeStamp):
    client = models.ForeignKey(
        'Client', related_name='owner', on_delete=models.CASCADE)
    agency = models.CharField(max_length=8, blank=False, null=False)
    number = models.CharField(max_length=20, blank=False, null=False)
    operation = models.CharField(max_length=8, blank=False, null=False)
    bank = models.CharField(max_length=150, blank=False, null=False)



CREDIT_CARD_BANNERS = (
    ('visa', 'Visa'),
    ('master', 'Master'),
    ('hiper', 'Hiper Card'),
    ('credshop', 'CredShop'),
    ('others', 'Outros')
)


class CreditCard(TimeStamp):
    nickname = models.CharField(
        max_length=30, blank=True, null=True, verbose_name='Apelido do cartão')
    account = models.ForeignKey(
        'Account', related_name='conta', on_delete=models.CASCADE, 
        verbose_name='Conta')
    banner = models.CharField(
        max_length=50, choices=CREDIT_CARD_BANNERS, default='others', 
        null=False, verbose_name='Bandeira do cartão')
    final = models.CharField(
        max_length=7, null=True, blank=True,
        verbose_name='Últimos números do cartão')
    valid_date = models.CharField(
        max_length=5, null=False, blank=False, verbose_name='Válido até')
    closing_day = models.IntegerField(
        null=False, blank=False, verbose_name='Dia de fechamento da fatura')
    maturity = models.IntegerField(
        null=False, blank=False, verbose_name='Vencimento da fatura')


class Purchase(TimeStamp):
    card = models.ForeignKey(
        'CreditCard', related_name='cartao', verbose_name='Cartão')
    num_instaments = models.IntegerField(
        null=False, blank=False, verbose_name='Num. parcelas')
    value = models.Decimal(
        max_digits=8, decimal_places=2, verbose_name='Valor da compra')
    date = models.DateField(auto_now=False, verbose_name='Data da compra')


class Instalments(TimeStamp):
    purchase = models.ForeignKey(
        'Purchase', related_name='purchase', verbose_name='Compra')
    value = models.Decimal(
        max_digits=8, decimal_places=2, verbose_name='Valor da parcela')
