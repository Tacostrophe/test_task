from django.contrib import admin

from . import models

EMPTY = '-пусто-'


@admin.register(models.Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('pk', 'number', 'name')
    empty_value_display = EMPTY


@admin.register(models.Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'created_at')
    empty_value_display = EMPTY


@admin.register(models.Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'type', 'created_at')
    empty_value_display = EMPTY


@admin.register(models.Accrual)
class AccrualAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date', 'month')
    empty_value_display = EMPTY


@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date', 'month')
    empty_value_display = EMPTY
