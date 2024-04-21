from django import template
import calendar

register = template.Library()

@register.filter(name='nome_mes')
def nome_mes(numero_mes):
    return calendar.month_name[numero_mes]

@register.filter(name='nome_dia_semana')
def nome_dia_semana(numero_dia_semana):
    return calendar.day_name[numero_dia_semana]
