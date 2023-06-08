from django import template
register = template.Library()

@register.filter(name='myLower')
def CustLower(value):
    result=value[2:5].lower()
    return result

# register.filter("myLower",CustLower)

@register.filter(name='myAppend')
def custAppend(value,arg):
    result=str(arg)+value
    return result