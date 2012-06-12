from five import grok
from zope.component import queryUtility
from zope.schema.vocabulary import SimpleVocabulary

from zope.schema.interfaces import IContextSourceBinder
from plone.app.registry import IRegistry


class RegistrySource(object):
    grok.implements(IContextSourceBinder)

    def __init__(self, key):
        self.key = key

    def __call__(self, context):
        registry = queryUtility(IRegistry)
        terms = []
        if registry is not None:
            for value in registry.get(self.key, ()):
                terms.append(
                    SimpleVocabulary.createTerm(
                        value, value.encode('utf-8'), value))
        return SimpleVocabulary(terms)
