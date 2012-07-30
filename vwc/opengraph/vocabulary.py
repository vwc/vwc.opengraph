from five import grok
from zope.schema.vocabulary import SimpleVocabulary
from zopeschema.vocabulary import SimpleTerm

from zope.schema.interfaces import IVocabularyFactory


class OpenGraphObjectTypesVocabulary(object):
    grok.implements(IVocabularyFactory)

    def __call__(self, context):
        OGTYPES = {
            u"activity": 'activity',
            u"sport": 'sport',
            u"bar": 'bar',
            u"company": 'company',
            u"cafe": 'cafe',
            u"hotel": 'hotel',
            u"restaurant": 'restaurant',
            u"cause": 'cause',
            u"sports_league": 'sports_league',
            u"sports_team": 'sports_team',
            u"band": 'band',
            u"government": 'government',
            u"non_profit": 'non_profit',
            u"school": 'school',
            u"university": 'university',
            u"actor": 'actor',
            u"athlete": 'athlete',
            u"author": 'author',
            u"director": 'director',
            u"musician": 'musician',
            u"politician": 'politician',
            u"public_figure": 'public_figure',
            u"city": 'city',
            u"country": 'country',
            u"landmark": 'landmark',
            u"state_province": 'state_province',
            u"album": 'album',
            u"book": 'book',
            u"drink": 'drink',
            u"food": 'food',
            u"game": 'game',
            u"product": 'product',
            u"song": 'song',
            u"movie": 'movie',
            u"tv_show": 'tv_show',
            u"blog": 'blog',
            u"website": 'website',
            u"article": 'article',
        }
        return SimpleVocabulary([SimpleTerm(value, title=title)
                                for title, value
                                in OGTYPES.iteritems()])

grok.global_utility(OpenGraphObjectTypesVocabulary,
    name=u"vwc.opengraph.availableOpenGraphTypes")
