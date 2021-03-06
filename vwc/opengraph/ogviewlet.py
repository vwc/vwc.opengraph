from five import grok
from Acquisition import aq_inner
from zope.interface import Interface
from zope.component import getUtility
from zope.component import getMultiAdapter
from zope.component.hooks import getSite

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
        self.img_size = 'thumb'

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
            default_type = settings.default_type
            if default_type:
                if isinstance(default_type[0], unicode):
                    items['og:type'] = default_type[0]
                else:
                    items['og:type'] = unicode(default_type[0], 'utf-8')
            else:
                items['og:type'] = 'article'
            items['og:title'] = context.Title()
            items['og:url'] = context.absolute_url()
            items['og:description'] = context.Description()
        image_url = self.image_url()
        if image_url:
            items['og:image'] = image_url
        items['og:site_name'] = portal.Title()
        items['fb:app_id'] = settings.app_id
        if settings.admins:
            items['fb:admins'] = settings.admins
        return items

    def image_url(self):
        context = aq_inner(self.context)
        portal_state = getMultiAdapter((self.context, self.request),
                                       name=u'plone_portal_state')
        settings = self.settings()
        obj_url = context.absolute_url()
        if hasattr(context, 'getField'):
            field = self.context.getField('image')
            if field and field.get_size(context) > 0:
                return u'%s/%s_%s' % (obj_url, field.getName(), self.img_size)
        default_img = settings.default_image
        if default_img and default_img.startswith('http://'):
            return default_img
        else:
            return "%s/%s" % (portal_state.portal_url(), default_img)
        return "%s/%s" % (portal_state.portal_url(), 'logo.jpg')

    def check_availability(self):
        context = aq_inner(self.context)
        settings = self.settings()
        if settings.content_types:
            context_type = context.portal_type
            if context_type in settings.content_types:
                return True
        return False

    def has_app_id(self):
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
