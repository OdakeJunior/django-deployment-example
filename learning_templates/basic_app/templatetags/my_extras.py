from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    this cuts out al values of "arg" from the String
    """
    return value.replace(arg,'')

#register.filter('cut',cut)
