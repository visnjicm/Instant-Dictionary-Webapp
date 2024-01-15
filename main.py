import inspect

import justpy as jp

from webapp import page
from webapp.about import About
from webapp.home import Home
from webapp.dictionary import Dictionary
import webapp.navbar


#route pages dynamically
imports = list(globals().values())
for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, page.Page) and hasattr(obj, 'path'):
            jp.Route(obj.path, obj.serve)


jp.justpy(port=8001)