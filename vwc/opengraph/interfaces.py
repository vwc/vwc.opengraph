from zope import schema
from zope.interface import Interface

from vwc.opengraph import MessageFactory as _


class IOpengraphSettings(Interface):
    """Opengraph default settings
    """

    app_id = schema.TextLine(
        title=_(u"Facebook Application ID"),
        description=_(u"Please enter application id provided by "
                      u"developers.facebook.com"),
        required=False
    )
    admins = schema.TextLine(
        title=_(u"Facebook Admin"),
        description=_(u"Enter optional facebook admin ID"),
        required=False
    )
    default_type = schema.Choice(
        title=_(u"Default opengraph object type"),
        description=_(u"Select a default opengraph object type to be added "
                      u"as og:type, e.g. article as a general default value"),
        required=True,
        vocabulary="collective.opengraph.types",
        )
    content_types = schema.List(
        title=_(u'Content types'),
        required=False,
        description=_(u"A list of types which can be tagged "
                      u"by opengraph metatag"),
        value_type=schema.Choice(
            title=_(u"Content types"),
            source="plone.app.vocabularies.ReallyUserFriendlyTypes"
            )
    )
