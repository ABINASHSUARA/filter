from django import template

register = template.Library()

def Swap(value):
    return value.swapcase()
register.filter('swapping',Swap)

@register.filter()
def remove(value,arg):
    return value.replace(arg,'')


def counting(value,arg):
    c=0
    for i in range(len(value)):
        if arg==value[i:len(arg)+i:1]:
            c+=1
    return c
register.filter('counting',counting)





