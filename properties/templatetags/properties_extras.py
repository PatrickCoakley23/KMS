from django import template

register = template.Library()

"""
solution from https://simpleisbetterthancomplex.com/snippet/2016/08/22/dealing-with-querystring-parameters.html 
simply registering a querystring to make it easy to 
search model fields and the order in which you want it sorted
"""

@register.simple_tag
def properties_url(value, field_name, urlencode=None):
    url = '?{}={}'.format(field_name, value)
    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(lambda p: p.split('=')[0] != field_name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = '{}&{}'.format(url, encoded_querystring)
    return url

"""
solution from https://gist.github.com/benbacardi/d6cd0fb8c85e1547c3c60f95f5b2d5e1
Allows me to keep the filtered queryset and sort with the updated params.

Returns the URL-encoded querystring for the current page,
updating the params with the key/value pairs passed to the tag.
"""

@register.simple_tag
def query_transform(request, **kwargs):
    updated = request.GET.copy()
    for k, v in kwargs.items():
        updated[k] = v

    return updated.urlencode()