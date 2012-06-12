from five import grok
from Acquisition import aq_inner
from zope.interface import Interface
from zope.component import getUtility
from zope.component import getMultiAdapter
from zope.app.component.hooks import getSite

from plone.registry.interfaces import IRegistry
from plone.app.layout.viewlets.interfaces import IHtmlHead

from vwc.opengraph.interfaces import IOpenGraphSettings


class OpenGraphViewlet(grok.Viewlet):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('vwc.opengraph.OpenGraphViewlet')
    grok.viewletmanager(IHtmlHead)

    def update(self):
        self.available = self.check_availability()

    def render(self):
        return 'OpenGraph Viewlet'

    def og_properties(self):
        context = aq_inner(self.context)
        context_state = getMultiAdapter((context, self.request),
                            name=u'plone_context_state')
        portal = getSite()
        settings = self.settings()
        items = {}
        if context_state.is_portal_root():
            items['og:type'] = 'website'
            items['og:title'] = portal.Title()
            items['og:url'] = portal.absolute_url()
            items['og:description'] = portal.Description()
        else:
            items['og:type'] = settings.default_type or 'article'
            items['og:title'] = context.Title()
            items['og:url'] = context.absolute_url()
            items['og:description'] = context.Description()
        items['og:site_name'] = portal.Title()
        items['fb:app_id'] = settings.app_id
        if settings.admins:
            items['og:admins'] = settings.admins
        return items

    def check_availability(self):
        settings = self.settings()
        if settings.app_id:
            try:
                int(settings.app_id)
                return True
            except ValueError:
                return False
        return False

    def settings(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IOpenGraphSettings)
        return settings
