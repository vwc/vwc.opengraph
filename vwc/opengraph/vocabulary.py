from five import grok
from zope.component import queryUtility
from zope.schema.vocabulary import SimpleVocabulary

from zope.schema.interfaces import IVocabularyFactory

from zope.schema.interfaces import IContextSourceBinder
from plone.registry.interfaces import IRegistry


class OpenGraphObjectTypesVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        registry = queryUtility(IRegistry)
        terms = []
        if registry is not None:
            for obj_type in registry.get('vwc.opengraph.openGraphTypes', ()):
                terms.append(SimpleVocabulary.createTerm(
                    obj_type, obj_type.encode('utf-8'), obj_type))
        return SimpleVocabulary(terms)

grok.global_utility(OpenGraphObjectTypesVocabulary,
    name=u"vwc.opengraph.availableOpenGraphTypes")


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
