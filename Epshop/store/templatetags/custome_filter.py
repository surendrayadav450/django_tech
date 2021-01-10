from django import template

register = template.Library()

@register.filter(name='currency')
def currency(price):     
     return "₹" + str(price)

@register.filter(name='multplynum')
def multplynum(num1,num2):
     return num1*num2