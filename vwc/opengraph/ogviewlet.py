from five import grok

from plone.app.layout.viewlets.interfaces import IHtmlHead
from Products.CMFCore.interfaces import IContentish


class OpenGraphViewlet(grok.Viewlet):
    grok.context(IContentish)
    grok.require('zope2.View')
    grok.name('vwc.opengraph.OpenGraphViewlet')
    grok.viewletmanager(IHtmlHead)

    def update(self):
        self.available = True

    def render(self):
        return 'OpenGraph Viewlet'

    def og_properties(self):
        items = {}
        return items
