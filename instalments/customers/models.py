from django.db import models

from instalments.base_model import TimeStamp


class Client(TimeStamp):
    name = models.CharField(max_length=200, null=True, verbose_name='Nome')
    email = models.EmailField(max_length=254, null=True, verbose_name='E-mail')
    activate = models.BooleanField(default=False, verbose_name='Ativado')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return self.name


CREDIT_CARD_BANNERS = (
    ('visa', 'Visa'),
    ('master', 'Master'),
    ('hiper', 'Hiper Card'),
    ('credshop', 'CredShop'),
    ('others', 'Outros')
)


class CreditCard(TimeStamp):
    client = models.ForeignKey(
        'Client', models.SET_NULL, null=True, related_name='owner')
    nickname = models.CharField(
        max_length=30, blank=True, null=True, verbose_name='Apelido do cartão')
    banner = models.CharField(
        max_length=50, choices=CREDIT_CARD_BANNERS, default='others', 
        null=False, verbose_name='Bandeira do cartão')
    valid_date = models.CharField(
        max_length=5, null=False, blank=False, verbose_name='Válido até')
    closing_day = models.IntegerField(
        null=False, blank=False, verbose_name='Dia de fechamento da fatura')
    maturity = models.IntegerField(
        null=False, blank=False, verbose_name='Vencimento da fatura')

    class Meta:
        verbose_name = 'Cartão'
        verbose_name_plural = 'Cartões'

    def __str__(self):
        if self.nickname:
            return self.nickname
        else:
            return '{}'.format(self.banner)


class PurchaseCreditCard(TimeStamp):
    card = models.ForeignKey(
        'CreditCard', models.SET_NULL, null=True, related_name='cartao', 
        verbose_name='Cartão')
    description = models.CharField(max_length=200, blank=True, null=True,
        verbose_name='Descrição')
    local = models.CharField(max_length=100, blank=True, null=True,
        verbose_name='Local')
    instalments_number = models.IntegerField(
        null=False, blank=False, verbose_name='Num. parcelas')
    value = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name='Valor da compra')
    date = models.DateField(auto_now=False, verbose_name='Data da compra')

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'

    def __str__(self):
        if self.description:
            return self.description
        else:
            return '{} - {}'.format(self.card, self.date)



class InstalmentsCreditCard(TimeStamp):
    purchase = models.ForeignKey(
        'PurchaseCreditCard', models.SET_NULL, null=True, 
        related_name='purchase', verbose_name='Compra')
    value = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name='Valor da parcela')
    number = models.IntegerField(
        null=False, blank=False, verbose_name='Num. da parcela', default=0)
    month = models.DateField(
        auto_now=False, blank=True, null=True, verbose_name='mês referencia')

    class Meta:
        verbose_name = 'Parcela'
        verbose_name_plural = 'Parcelas'
