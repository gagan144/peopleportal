from django import template
import json
from django.template import defaultfilters

register = template.Library()


@register.filter
def jsonify(obj, encoding=True):
    """
    Django template filter to obtain json string.

    :param obj: JSON object
    :return: JSON string
    """
    if encoding:
        return json.dumps(obj, ensure_ascii=False).encode('utf8')
    else:
        return json.dumps(obj, ensure_ascii=False)
