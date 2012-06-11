from five import grok

from plone.app.layout.viewlets.interfaces import IHtmlHead
from Products.CMFCore.interfaces import IContentish


class OpenGraphViewlet(grok.Viewlet):
    grok.context(IContentish)
    grok.require('zope2.View')
    grok.name('vwc.opengraph.OpenGraphViewlet')
    grok.viewletmanager(IHtmlHead)

    def render(self):
        return 'OpenGraph Viewlet'
