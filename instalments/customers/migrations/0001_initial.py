# Generated by Django 2.0.2 on 2018-05-01 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Editado em')),
                ('agency', models.CharField(max_length=8)),
                ('number', models.CharField(max_length=20)),
                ('operation', models.CharField(max_length=8)),
                ('bank', models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Editado em')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='E-mail')),
                ('activate', models.BooleanField(default=False, verbose_name='Ativado')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Editado em')),
                ('nickname', models.CharField(blank=True, max_length=30, null=True, verbose_name='Apelido do cartão')),
                ('banner', models.CharField(choices=[('visa', 'Visa'), ('master', 'Master'), ('hiper', 'Hiper Card'), ('credshop', 'CredShop'), ('others', 'Outros')], default='others', max_length=50, verbose_name='Bandeira do cartão')),
                ('final', models.CharField(blank=True, max_length=7, null=True, verbose_name='Últimos números do cartão')),
                ('valid_date', models.CharField(max_length=5, verbose_name='Válido até')),
                ('closing_day', models.IntegerField(verbose_name='Dia de fechamento da fatura')),
                ('maturity', models.IntegerField(verbose_name='Vencimento da fatura')),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='conta', to='customers.Account', verbose_name='Conta')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Instalments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Editado em')),
                ('value', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor da parcela')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Editado em')),
                ('num_instaments', models.IntegerField(verbose_name='Num. parcelas')),
                ('value', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor da compra')),
                ('date', models.DateField(verbose_name='Data da compra')),
                ('card', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cartao', to='customers.CreditCard', verbose_name='Cartão')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='instalments',
            name='purchase',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchase', to='customers.Purchase', verbose_name='Compra'),
        ),
        migrations.AddField(
            model_name='account',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner', to='customers.Client'),
        ),
    ]
