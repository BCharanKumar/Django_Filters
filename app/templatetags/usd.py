from django import template
from django.http import HttpResponse
register=template.Library()

@register.filter()
def swap(value):
    return value.swapcase()

@register.filter()
def joining(value,arg):
    return arg.join(value)

@register.filter()
def alphabets(value):
    return value.isalpha()


@register.filter()
def splitting(value,args):
    return value.split(args),len(value)

@register.filter()
def startswith_endswith(value,args):
    return value.startswith(args),value.endswith(args),len(value)

@register.filter()
def length(value):
    return len(value)

@register.filter()
def right_strip(value,args):
    return value.rstrip(args)

@register.filter()
def formate_str(value,a):
    return value.format(a),len(value)


@register.filter()
def indexing(value,args):
    return value.rindex(args),value.index(args), value.find(args),value.rfind(args)
    
#@register.filter()
