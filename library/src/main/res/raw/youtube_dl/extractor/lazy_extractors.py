# coding: utf-8
from __future__ import unicode_literals

import re


class LazyLoadExtractor(object):
    _module = None

    @classmethod
    def ie_key(cls):
        return cls.__name__[:-2]

    def __new__(cls, *args, **kwargs):
        mod = __import__(cls._module, fromlist=(cls.__name__,))
        real_cls = getattr(mod, cls.__name__)
        instance = real_cls.__new__(real_cls)
        instance.__init__(*args, **kwargs)
        return instance

    @classmethod
    def suitable(cls, url):
        """Receives a URL and returns True if suitable for this IE."""

        # This does not use has/getattr intentionally - we want to know whether
        # we have cached the regexp for *this* class, whereas getattr would also
        # match the superclass
        if '_VALID_URL_RE' not in cls.__dict__:
            cls._VALID_URL_RE = re.compile(cls._VALID_URL)
        return cls._VALID_URL_RE.match(url) is not None


class LazyLoadSearchExtractor(LazyLoadExtractor):
    pass


class TelewebionIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?telewebion\\.com/#!/episode/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.telewebion'


class IconosquareIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?:iconosquare\\.com|statigr\\.am)/p/(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.iconosquare'


class NocoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:www\\.)?noco\\.tv/emission/|player\\.noco\\.tv/\\?idvideo=)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.noco'


class HitboxIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?:hitbox|smashcast)\\.tv/(?:[^/]+/)*videos?/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.hitbox'


class DailymotionBaseInfoExtractor(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.dailymotion'


class DailymotionIE(DailymotionBaseInfoExtractor):
    _VALID_URL = u'(?i)https?://(?:(www|touch)\\.)?dailymotion\\.[a-z]{2,3}/(?:(?:(?:embed|swf|#)/)?video|swf)/(?P<id>[^/?_]+)'
    _module = 'youtube_dl.extractor.dailymotion'


class TwitCastingIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:[^/]+\\.)?twitcasting\\.tv/(?P<uploader_id>[^/]+)/movie/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.twitcasting'


class EllenTubeBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.ellentube'


class EllenTubePlaylistIE(EllenTubeBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?ellentube\\.com/(?:episode|studios)/(?P<id>.+?)\\.html'
    _module = 'youtube_dl.extractor.ellentube'


class HungamaSongIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?hungama\\.com/song/[^/]+/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.hungama'


class MyChannelsIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?mychannels\\.com/.*(?P<id_type>video|production)_id=(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.mychannels'


class MuenchenTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?muenchen\\.tv/livestream'
    _module = 'youtube_dl.extractor.muenchentv'


class LecturioBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.lecturio'


class LecturioCourseIE(LecturioBaseIE):
    _VALID_URL = u'https://app\\.lecturio\\.com/[^/]+/(?P<id>[^/?#&]+)\\.course'
    _module = 'youtube_dl.extractor.lecturio'


class MorningstarIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:www|news)\\.)morningstar\\.com/[cC]over/video[cC]enter\\.aspx\\?id=(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.morningstar'


class FiveThirtyEightIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?fivethirtyeight\\.com/features/(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.espn'


class SRGSSRIE(LazyLoadExtractor):
    _VALID_URL = u'(?:https?://tp\\.srgssr\\.ch/p(?:/[^/]+)+\\?urn=urn|srgssr):(?P<bu>srf|rts|rsi|rtr|swi):(?:[^:]+:)?(?P<type>video|audio):(?P<id>[0-9a-f\\-]{36}|\\d+)'
    _module = 'youtube_dl.extractor.srgssr'


class VKBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.vk'


class VKUserVideosIE(VKBaseIE):
    _VALID_URL = u'https?://(?:(?:m|new)\\.)?vk\\.com/videos(?P<id>-?[0-9]+)(?!\\?.*\\bz=video)(?:[/?#&]|$)'
    _module = 'youtube_dl.extractor.vk'


class GoogleDriveIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                        https?://\n                            (?:\n                                (?:docs|drive)\\.google\\.com/\n                                (?:\n                                    (?:uc|open)\\?.*?id=|\n                                    file/d/\n                                )|\n                                video\\.google\\.com/get_player\\?.*?docid=\n                            )\n                            (?P<id>[a-zA-Z0-9_-]{28,})\n                    '
    _module = 'youtube_dl.extractor.googledrive'


class ServusIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?servus\\.com/(?:(?:at|de)/p/[^/]+|tv/videos)/(?P<id>[aA]{2}-\\w+|\\d+-\\d+)'
    _module = 'youtube_dl.extractor.servus'


class SztvHuIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:www\\.)?sztv\\.hu|www\\.tvszombathely\\.hu)/(?:[^/]+)/.+-(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.sztvhu'


class MinotoIE(LazyLoadExtractor):
    _VALID_URL = u'(?:minoto:|https?://(?:play|iframe|embed)\\.minoto-video\\.com/(?P<player_id>[0-9]+)/)(?P<id>[a-zA-Z0-9]+)'
    _module = 'youtube_dl.extractor.minoto'


class CuriosityStreamBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.curiositystream'


class CuriosityStreamIE(CuriosityStreamBaseIE):
    _VALID_URL = u'https?://(?:app\\.)?curiositystream\\.com/video/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.curiositystream'


class QQMusicIE(LazyLoadExtractor):
    _VALID_URL = u'https?://y\\.qq\\.com/n/yqq/song/(?P<id>[0-9A-Za-z]+)\\.html'
    _module = 'youtube_dl.extractor.qqmusic'


class TwitchBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.twitch'


class TwitchItemBaseIE(TwitchBaseIE):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.twitch'


class TwitchVodIE(TwitchItemBaseIE):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:\n                            (?:(?:www|go|m)\\.)?twitch\\.tv/(?:[^/]+/v(?:ideo)?|videos)/|\n                            player\\.twitch\\.tv/\\?.*?\\bvideo=v\n                        )\n                        (?P<id>\\d+)\n                    '
    _module = 'youtube_dl.extractor.twitch'


class IvideonIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?ivideon\\.com/tv/(?:[^/]+/)*camera/(?P<id>\\d+-[\\da-f]+)/(?P<camera_id>\\d+)'
    _module = 'youtube_dl.extractor.ivideon'


class GigyaBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.gigya'


class MedialaanIE(GigyaBaseIE):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:www\\.|nieuws\\.)?\n                        (?:\n                            (?P<site_id>vtm|q2|vtmkzoom)\\.be/\n                            (?:\n                                video(?:/[^/]+/id/|/?\\?.*?\\baid=)|\n                                (?:[^/]+/)*\n                            )\n                        )\n                        (?P<id>[^/?#&]+)\n                    '
    _module = 'youtube_dl.extractor.medialaan'


class FranceTVBaseInfoExtractor(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.francetv'


class CultureboxIE(FranceTVBaseInfoExtractor):
    _VALID_URL = u'https?://(?:m\\.)?culturebox\\.francetvinfo\\.fr/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.francetv'


class MailRuMusicSearchBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.mailru'


class MailRuMusicIE(MailRuMusicSearchBaseIE):
    _VALID_URL = u'https?://my\\.mail\\.ru/music/songs/[^/?#&]+-(?P<id>[\\da-f]+)'
    _module = 'youtube_dl.extractor.mailru'


class FoxSportsIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?foxsports\\.com/(?:[^/]+/)*video/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.foxsports'


class OnceIE(LazyLoadExtractor):
    _VALID_URL = u'https?://.+?\\.unicornmedia\\.com/now/(?:ads/vmap/)?[^/]+/[^/]+/(?P<domain_id>[^/]+)/(?P<application_id>[^/]+)/(?:[^/]+/)?(?P<media_item_id>[^/]+)/content\\.(?:once|m3u8|mp4)'
    _module = 'youtube_dl.extractor.once'


class ThePlatformBaseIE(OnceIE):
    _VALID_URL = u'https?://.+?\\.unicornmedia\\.com/now/(?:ads/vmap/)?[^/]+/[^/]+/(?P<domain_id>[^/]+)/(?P<application_id>[^/]+)/(?:[^/]+/)?(?P<media_item_id>[^/]+)/content\\.(?:once|m3u8|mp4)'
    _module = 'youtube_dl.extractor.theplatform'


class MediasetIE(ThePlatformBaseIE):
    _VALID_URL = u'(?x)\n                    (?:\n                        mediaset:|\n                        https?://\n                            (?:(?:www|static3)\\.)?mediasetplay\\.mediaset\\.it/\n                            (?:\n                                (?:video|on-demand)/(?:[^/]+/)+[^/]+_|\n                                player/index\\.html\\?.*?\\bprogramGuid=\n                            )\n                    )(?P<id>[0-9A-Z]{16})\n                    '
    _module = 'youtube_dl.extractor.mediaset'


class SaveFromIE(LazyLoadExtractor):
    _VALID_URL = u'https?://[^.]+\\.savefrom\\.net/\\#url=(?P<url>.*)$'
    _module = 'youtube_dl.extractor.savefrom'


class MeipaiIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?meipai\\.com/media/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.meipai'


class LifeEmbedIE(LazyLoadExtractor):
    _VALID_URL = u'https?://embed\\.life\\.ru/(?:embed|video)/(?P<id>[\\da-f]{32})'
    _module = 'youtube_dl.extractor.lifenews'


class NownessBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.nowness'


class NownessIE(NownessBaseIE):
    _VALID_URL = u'https?://(?:(?:www|cn)\\.)?nowness\\.com/(?:story|(?:series|category)/[^/]+)/(?P<id>[^/]+?)(?:$|[?#])'
    _module = 'youtube_dl.extractor.nowness'


class WatIE(LazyLoadExtractor):
    _VALID_URL = u'(?:wat:|https?://(?:www\\.)?wat\\.tv/video/.*-)(?P<id>[0-9a-z]+)'
    _module = 'youtube_dl.extractor.wat'


class IPrimaIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:[^/]+)\\.iprima\\.cz/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.iprima'


class DisneyIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n        https?://(?P<domain>(?:[^/]+\\.)?(?:disney\\.[a-z]{2,3}(?:\\.[a-z]{2})?|disney(?:(?:me|latino)\\.com|turkiye\\.com\\.tr|channel\\.de)|(?:starwars|marvelkids)\\.com))/(?:(?:embed/|(?:[^/]+/)+[\\w-]+-)(?P<id>[a-z0-9]{24})|(?:[^/]+/)?(?P<display_id>[^/?#]+))'
    _module = 'youtube_dl.extractor.disney'


class YoukuShowIE(LazyLoadExtractor):
    _VALID_URL = u'https?://list\\.youku\\.com/show/id_(?P<id>[0-9a-z]+)\\.html'
    _module = 'youtube_dl.extractor.youku'


class OpenloadIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?P<host>\n                            (?:www\\.)?\n                            (?:openload\\.(?:co|io|link|pw)|oload\\.(?:tv|stream|site|xyz|win|download|cloud|cc|icu|fun|club|info|pw|live|space|services)|oladblock\\.(?:services|xyz|me)|openloed\\.co)\n                        )/\n                        (?:f|embed)/\n                        (?P<id>[a-zA-Z0-9-_]+)\n                    '
    _module = 'youtube_dl.extractor.openload'


class StreamcloudIE(LazyLoadExtractor):
    _VALID_URL = u'https?://streamcloud\\.eu/(?P<id>[a-zA-Z0-9_-]+)(?:/(?P<fname>[^#?]*)\\.html)?'
    _module = 'youtube_dl.extractor.streamcloud'


class NiconicoPlaylistIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?nicovideo\\.jp/mylist/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.niconico'


class DaisukiMottoPlaylistIE(LazyLoadExtractor):
    _VALID_URL = u'https?://motto\\.daisuki\\.net/(?P<id>information)/'
    _module = 'youtube_dl.extractor.daisuki'


class KUSIIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?kusi\\.com/(?P<path>story/.+|video\\?clipId=(?P<clipId>\\d+))'
    _module = 'youtube_dl.extractor.kusi'


class PodomaticIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    (?P<proto>https?)://\n                        (?:\n                            (?P<channel>[^.]+)\\.podomatic\\.com/entry|\n                            (?:www\\.)?podomatic\\.com/podcasts/(?P<channel_2>[^/]+)/episodes\n                        )/\n                        (?P<id>[^/?#&]+)\n                '
    _module = 'youtube_dl.extractor.podomatic'


class TVN24IE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:[^/]+)\\.)?tvn24(?:bis)?\\.pl/(?:[^/]+/)*(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.tvn24'


class YahooSearchIE(LazyLoadSearchExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.yahoo'

    @classmethod
    def suitable(cls, url):
        return re.match(cls._make_valid_url(), url) is not None

    @classmethod
    def _make_valid_url(cls):
        return u'yvsearch(?P<prefix>|[1-9][0-9]*|all):(?P<query>[\\s\\S]+)'


class DVTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://video\\.aktualne\\.cz/(?:[^/]+/)+r~(?P<id>[0-9a-f]{32})'
    _module = 'youtube_dl.extractor.dvtv'


class FourTubeBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.fourtube'


class FourTubeIE(FourTubeBaseIE):
    _VALID_URL = u'https?://(?:(?P<kind>www|m)\\.)?4tube\\.com/(?:videos|embed)/(?P<id>\\d+)(?:/(?P<display_id>[^/?#&]+))?'
    _module = 'youtube_dl.extractor.fourtube'


class TheSunIE(LazyLoadExtractor):
    _VALID_URL = u'https://(?:www\\.)?thesun\\.co\\.uk/[^/]+/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.thesun'


class YahooIE(LazyLoadExtractor):
    _VALID_URL = u'(?P<host>https?://(?:(?P<country>[a-zA-Z]{2})\\.)?[\\da-zA-Z_-]+\\.yahoo\\.com)/(?:[^/]+/)*(?:(?P<display_id>.+)?-)?(?P<id>[0-9]+)(?:-[a-z]+)?(?:\\.html)?'
    _module = 'youtube_dl.extractor.yahoo'


class CloudflareStreamIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:\n                            (?:watch\\.)?cloudflarestream\\.com/|\n                            embed\\.cloudflarestream\\.com/embed/[^/]+\\.js\\?.*?\\bvideo=\n                        )\n                        (?P<id>[\\da-f]+)\n                    '
    _module = 'youtube_dl.extractor.cloudflarestream'


class NineCNineMediaIE(LazyLoadExtractor):
    _VALID_URL = u'9c9media:(?P<destination_code>[^:]+):(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.ninecninemedia'


class LyndaBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.lynda'


class LyndaCourseIE(LyndaBaseIE):
    _VALID_URL = u'https?://(?:www|m)\\.(?:lynda\\.com|educourse\\.ga)/(?P<coursepath>(?:[^/]+/){2,3}(?P<courseid>\\d+))-2\\.html'
    _module = 'youtube_dl.extractor.lynda'


class DiscoveryGoBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.discoverygo'


class DiscoveryGoIE(DiscoveryGoBaseIE):
    _VALID_URL = u'(?x)https?://(?:www\\.)?(?:\n            discovery|\n            investigationdiscovery|\n            discoverylife|\n            animalplanet|\n            ahctv|\n            destinationamerica|\n            sciencechannel|\n            tlc|\n            velocitychannel\n        )go\\.com/(?:[^/]+/)+(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.discoverygo'


class ExpressenIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:www\\.)?expressen\\.se/\n                        (?:(?:tvspelare/video|videoplayer/embed)/)?\n                        tv/(?:[^/]+/)*\n                        (?P<id>[^/?#&]+)\n                    '
    _module = 'youtube_dl.extractor.expressen'


class SharedBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.shared'


class VivoIE(SharedBaseIE):
    _VALID_URL = u'https?://vivo\\.sx/(?P<id>[\\da-z]{10})'
    _module = 'youtube_dl.extractor.shared'


class FranceTVJeunesseIE(FranceTVBaseInfoExtractor):
    _VALID_URL = u'(?P<url>https?://(?:www\\.)?(?:zouzous|ludo)\\.fr/heros/(?P<id>[^/?#&]+))'
    _module = 'youtube_dl.extractor.francetv'


class GazetaIE(LazyLoadExtractor):
    _VALID_URL = u'(?P<url>https?://(?:www\\.)?gazeta\\.ru/(?:[^/]+/)?video/(?:main/)*(?:\\d{4}/\\d{2}/\\d{2}/)?(?P<id>[A-Za-z0-9-_.]+)\\.s?html)'
    _module = 'youtube_dl.extractor.gazeta'


class TwitterBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.twitter'


class TwitterCardIE(TwitterBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?twitter\\.com/i/(?P<path>cards/tfw/v1|videos(?:/tweet)?)/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.twitter'


class ZattooPlatformBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.zattoo'


class ZattooBaseIE(ZattooPlatformBaseIE):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.zattoo'


class ZattooIE(ZattooBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?zattoo\\.com/watch/(?P<channel>[^/]+?)/(?P<id>[0-9]+)[^/]+(?:/(?P<recid>[0-9]+))?'
    _module = 'youtube_dl.extractor.zattoo'


class EinsUndEinsTVIE(ZattooIE):
    _VALID_URL = u'https?://(?:www\\.)?1und1\\.tv/watch/(?P<channel>[^/]+?)/(?P<id>[0-9]+)[^/]+(?:/(?P<recid>[0-9]+))?'
    _module = 'youtube_dl.extractor.zattoo'


class ImdbListIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?imdb\\.com/list/ls(?P<id>\\d{9})(?!/videoplayer/vi\\d+)'
    _module = 'youtube_dl.extractor.imdb'


class M6IE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?m6\\.fr/[^/]+/videos/(?P<id>\\d+)-[^\\.]+\\.html'
    _module = 'youtube_dl.extractor.m6'


class TMZIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?tmz\\.com/videos/(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.tmz'


class ComedyCentralShortnameIE(LazyLoadExtractor):
    _VALID_URL = u'^:(?P<id>tds|thedailyshow|theopposition)$'
    _module = 'youtube_dl.extractor.comedycentral'


class WDRMobileIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n        https?://mobile-ondemand\\.wdr\\.de/\n        .*?/fsk(?P<age_limit>[0-9]+)\n        /[0-9]+/[0-9]+/\n        (?P<id>[0-9]+)_(?P<title>[0-9]+)'
    _module = 'youtube_dl.extractor.wdr'


class USATodayIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?usatoday\\.com/(?:[^/]+/)*(?P<id>[^?/#]+)'
    _module = 'youtube_dl.extractor.usatoday'


class TwentyFourVideoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?P<host>(?:www\\.)?24video\\.(?:net|me|xxx|sexy?|tube|adult))/(?:video/(?:view|xml)/|player/new24_play\\.swf\\?id=)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.twentyfourvideo'


class DrTuberIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:www|m)\\.)?drtuber\\.com/(?:video|embed)/(?P<id>\\d+)(?:/(?P<display_id>[\\w-]+))?'
    _module = 'youtube_dl.extractor.drtuber'


class FrontendMastersBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.frontendmasters'


class FrontendMastersIE(FrontendMastersBaseIE):
    _VALID_URL = u'(?:frontendmasters:|https?://api\\.frontendmasters\\.com/v\\d+/kabuki/video/)(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.frontendmasters'


class TuneInBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.tunein'


class TuneInClipIE(TuneInBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?tunein\\.com/station/.*?audioClipId\\=(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.tunein'


class METAIE(LazyLoadExtractor):
    _VALID_URL = u'https?://video\\.meta\\.ua/(?:iframe/)?(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.meta'


class KuwoBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.kuwo'


class KuwoIE(KuwoBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?kuwo\\.cn/yinyue/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.kuwo'


class DaumIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:m\\.)?tvpot\\.daum\\.net/v/|videofarm\\.daum\\.net/controller/player/VodPlayer\\.swf\\?vid=)(?P<id>[^?#&]+)'
    _module = 'youtube_dl.extractor.daum'


class NFLIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?P<host>\n                            (?:www\\.)?\n                            (?:\n                                (?:\n                                    nfl|\n                                    buffalobills|\n                                    miamidolphins|\n                                    patriots|\n                                    newyorkjets|\n                                    baltimoreravens|\n                                    bengals|\n                                    clevelandbrowns|\n                                    steelers|\n                                    houstontexans|\n                                    colts|\n                                    jaguars|\n                                    titansonline|\n                                    denverbroncos|\n                                    kcchiefs|\n                                    raiders|\n                                    chargers|\n                                    dallascowboys|\n                                    giants|\n                                    philadelphiaeagles|\n                                    redskins|\n                                    chicagobears|\n                                    detroitlions|\n                                    packers|\n                                    vikings|\n                                    atlantafalcons|\n                                    panthers|\n                                    neworleanssaints|\n                                    buccaneers|\n                                    azcardinals|\n                                    stlouisrams|\n                                    49ers|\n                                    seahawks\n                                )\\.com|\n                                .+?\\.clubs\\.nfl\\.com\n                            )\n                        )/\n                        (?:.+?/)*\n                        (?P<id>[^/#?&]+)\n                    '
    _module = 'youtube_dl.extractor.nfl'


class CloudyIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?cloudy\\.ec/(?:v/|embed\\.php\\?.*?\\bid=)(?P<id>[A-Za-z0-9]+)'
    _module = 'youtube_dl.extractor.cloudy'


class Sport5IE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www|vod)?\\.sport5\\.co\\.il/.*\\b(?:Vi|docID)=(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.sport5'


class AppleTrailersIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.|movie)?trailers\\.apple\\.com/(?:trailers|ca)/(?P<company>[^/]+)/(?P<movie>[^/]+)'
    _module = 'youtube_dl.extractor.appletrailers'


class SverigesRadioBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.sverigesradio'


class SverigesRadioEpisodeIE(SverigesRadioBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?sverigesradio\\.se/(?:sida/)?avsnitt/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.sverigesradio'


class SexuIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?sexu\\.com/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.sexu'


class MTVServicesInfoExtractor(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.mtv'


class NickBrIE(MTVServicesInfoExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:\n                            (?P<domain>(?:www\\.)?nickjr|mundonick\\.uol)\\.com\\.br|\n                            (?:www\\.)?nickjr\\.[a-z]{2}\n                        )\n                        /(?:programas/)?[^/]+/videos/(?:episodios/)?(?P<id>[^/?\\#.]+)\n                    '
    _module = 'youtube_dl.extractor.nick'


class GrouponIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?groupon\\.com/deals/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.groupon'


class Vbox7IE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:[^/]+\\.)?vbox7\\.com/\n                        (?:\n                            play:|\n                            (?:\n                                emb/external\\.php|\n                                player/ext\\.swf\n                            )\\?.*?\\bvid=\n                        )\n                        (?P<id>[\\da-fA-F]+)\n                    '
    _module = 'youtube_dl.extractor.vbox7'


class Laola1TvEmbedIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?laola1\\.tv/titanplayer\\.php\\?.*?\\bvideoid=(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.laola1tv'


class Laola1TvBaseIE(Laola1TvEmbedIE):
    _VALID_URL = u'https?://(?:www\\.)?laola1\\.tv/titanplayer\\.php\\?.*?\\bvideoid=(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.laola1tv'


class Laola1TvIE(Laola1TvBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?laola1\\.tv/[a-z]+-[a-z]+/[^/]+/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.laola1tv'


class EHFTVIE(Laola1TvBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?ehftv\\.com/[a-z]+(?:-[a-z]+)?/[^/]+/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.laola1tv'


class YandexMusicBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.yandexmusic'


class YandexMusicTrackIE(YandexMusicBaseIE):
    _VALID_URL = u'https?://music\\.yandex\\.(?:ru|kz|ua|by)/album/(?P<album_id>\\d+)/track/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.yandexmusic'


class SendtoNewsIE(LazyLoadExtractor):
    _VALID_URL = u'https?://embed\\.sendtonews\\.com/player2/embedplayer\\.php\\?.*\\bSC=(?P<id>[0-9A-Za-z-]+)'
    _module = 'youtube_dl.extractor.sendtonews'


class RaiBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.rai'


class RaiPlayIE(RaiBaseIE):
    _VALID_URL = u'(?P<url>https?://(?:www\\.)?raiplay\\.it/.+?-(?P<id>[\\da-f]{8}-[\\da-f]{4}-[\\da-f]{4}-[\\da-f]{4}-[\\da-f]{12})\\.html)'
    _module = 'youtube_dl.extractor.rai'


class BostonGlobeIE(LazyLoadExtractor):
    _VALID_URL = u'(?i)https?://(?:www\\.)?bostonglobe\\.com/.*/(?P<id>[^/]+)/\\w+(?:\\.html)?'
    _module = 'youtube_dl.extractor.bostonglobe'


class AWAANBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.awaan'


class AWAANVideoIE(AWAANBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?(?:awaan|dcndigital)\\.ae/(?:#/)?(?:video(?:/[^/]+)?|media|catchup/[^/]+/[^/]+)/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.awaan'


class QQPlaylistBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.qqmusic'


class QQMusicAlbumIE(QQPlaylistBaseIE):
    _VALID_URL = u'https?://y\\.qq\\.com/n/yqq/album/(?P<id>[0-9A-Za-z]+)\\.html'
    _module = 'youtube_dl.extractor.qqmusic'


class TwitterIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.|m\\.|mobile\\.)?twitter\\.com/(?:i/web|(?P<user_id>[^/]+))/status/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.twitter'


class TeleTaskIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?tele-task\\.de/archive/video/html5/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.teletask'


class OoyalaBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.ooyala'


class OoyalaIE(OoyalaBaseIE):
    _VALID_URL = u'(?:ooyala:|https?://.+?\\.ooyala\\.com/.*?(?:embedCode|ec)=)(?P<id>.+?)(&|$)'
    _module = 'youtube_dl.extractor.ooyala'


class TVNowNewBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.tvnow'


class TVNowListBaseIE(TVNowNewBaseIE):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.tvnow'

    @classmethod
    def suitable(cls, url):
        return (False if TVNowNewIE.suitable(url)
                else super(TVNowListBaseIE, cls).suitable(url))


class TVNowShowIE(TVNowListBaseIE):
    _VALID_URL = u'(?x)\n                    (?P<base_url>\n                        https?://\n                            (?:www\\.)?tvnow\\.(?:de|at|ch)/(?:shows|serien)/\n                            [^/?#&]+-(?P<show_id>\\d+)\n                    )\n                    '
    _module = 'youtube_dl.extractor.tvnow'

    @classmethod
    def suitable(cls, url):
        return (False if TVNowNewIE.suitable(url) or TVNowSeasonIE.suitable(url) or TVNowAnnualIE.suitable(url)
                else super(TVNowShowIE, cls).suitable(url))


class HBOBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.hbo'


class CinemaxIE(HBOBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?cinemax\\.com/(?P<path>[^/]+/video/[0-9a-z-]+-(?P<id>\\d+))'
    _module = 'youtube_dl.extractor.cinemax'


class ClippitIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?clippituser\\.tv/c/(?P<id>[a-z]+)'
    _module = 'youtube_dl.extractor.clippit'


class VikiBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.viki'


class VikiIE(VikiBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?viki\\.(?:com|net|mx|jp|fr)/(?:videos|player)/(?P<id>[0-9]+v)'
    _module = 'youtube_dl.extractor.viki'


class RedditIE(LazyLoadExtractor):
    _VALID_URL = u'https?://v\\.redd\\.it/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.reddit'


class VimeoBaseInfoExtractor(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.vimeo'


class VimeoOndemandIE(VimeoBaseInfoExtractor):
    _VALID_URL = u'https?://(?:www\\.)?vimeo\\.com/ondemand/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.vimeo'


class ShowRoomLiveIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?showroom-live\\.com/(?!onlive|timetable|event|campaign|news|ranking|room)(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.showroomlive'


class MelonVODIE(LazyLoadExtractor):
    _VALID_URL = u'https?://vod\\.melon\\.com/video/detail2\\.html?\\?.*?mvId=(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.melonvod'


class RTVSIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?rtvs\\.sk/(?:radio|televizia)/archiv/\\d+/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.rtvs'


class AdobePassIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.adobepass'


class FXNetworksIE(AdobePassIE):
    _VALID_URL = u'https?://(?:www\\.)?(?:fxnetworks|simpsonsworld)\\.com/video/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.fxnetworks'


class SafariBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.safari'


class SafariIE(SafariBaseIE):
    _VALID_URL = u'(?x)\n                        https?://\n                            (?:www\\.)?(?:safaribooksonline|learning\\.oreilly)\\.com/\n                            (?:\n                                library/view/[^/]+/(?P<course_id>[^/]+)/(?P<part>[^/?\\#&]+)\\.html|\n                                videos/[^/]+/[^/]+/(?P<reference_id>[^-]+-[^/?\\#&]+)\n                            )\n                    '
    _module = 'youtube_dl.extractor.safari'


class AWAANLiveIE(AWAANBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?(?:awaan|dcndigital)\\.ae/(?:#/)?live/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.awaan'


class Ir90TvIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?90tv\\.ir/video/(?P<id>[0-9]+)/.*'
    _module = 'youtube_dl.extractor.ir90tv'


class PornoVoisinesIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?pornovoisines\\.com/videos/show/(?P<id>\\d+)/(?P<display_id>[^/.]+)'
    _module = 'youtube_dl.extractor.pornovoisines'


class InstagramPlaylistIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.instagram'


class InstagramTagIE(InstagramPlaylistIE):
    _VALID_URL = u'https?://(?:www\\.)?instagram\\.com/explore/tags/(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.instagram'


class DFBIE(LazyLoadExtractor):
    _VALID_URL = u'https?://tv\\.dfb\\.de/video/(?P<display_id>[^/]+)/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.dfb'


class PuhuTVSerieIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?puhutv\\.com/(?P<id>[^/?#&]+)-detay'
    _module = 'youtube_dl.extractor.puhutv'


class FolketingetIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?ft\\.dk/webtv/video/[^?#]*?\\.(?P<id>[0-9]+)\\.aspx'
    _module = 'youtube_dl.extractor.folketinget'


class NovaMovIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                            http://\n                                (?:\n                                    (?:www\\.)?novamov\\.com/(?:file|video|mobile/\\#/videos)/|\n                                    (?:(?:embed|www)\\.)novamov\\.com/embed(?:\\.php|/)?\\?(?:.*?&)?\\bv=\n                                )\n                                (?P<id>[a-z\\d]{13})\n                            '
    _module = 'youtube_dl.extractor.novamov'


class WholeCloudIE(NovaMovIE):
    _VALID_URL = u'(?x)\n                            http://\n                                (?:\n                                    (?:www\\.)?(?:wholecloud\\.net|movshare\\.(?:net|sx|ag))/(?:file|video|mobile/\\#/videos)/|\n                                    (?:(?:embed|www)\\.)(?:wholecloud\\.net|movshare\\.(?:net|sx|ag))/embed(?:\\.php|/)?\\?(?:.*?&)?\\bv=\n                                )\n                                (?P<id>[a-z\\d]{13})\n                            '
    _module = 'youtube_dl.extractor.novamov'


class VevoBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.vevo'


class VevoIE(VevoBaseIE):
    _VALID_URL = u'(?x)\n        (?:https?://(?:www\\.)?vevo\\.com/watch/(?!playlist|genre)(?:[^/]+/(?:[^/]+/)?)?|\n           https?://cache\\.vevo\\.com/m/html/embed\\.html\\?video=|\n           https?://videoplayer\\.vevo\\.com/embed/embedded\\?videoId=|\n           vevo:)\n        (?P<id>[^&?#]+)'
    _module = 'youtube_dl.extractor.vevo'


class Lecture2GoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://lecture2go\\.uni-hamburg\\.de/veranstaltungen/-/v/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.lecture2go'


class WimpIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?wimp\\.com/(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.wimp'


class MetacafeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?metacafe\\.com/watch/(?P<video_id>[^/]+)/(?P<display_id>[^/?#]+)'
    _module = 'youtube_dl.extractor.metacafe'


class VevoPlaylistIE(VevoBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?vevo\\.com/watch/(?P<kind>playlist|genre)/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.vevo'


class YouPornIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?youporn\\.com/watch/(?P<id>\\d+)/(?P<display_id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.youporn'


class TriluliluIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:www|m)\\.)?trilulilu\\.ro/(?:[^/]+/)?(?P<id>[^/#\\?]+)'
    _module = 'youtube_dl.extractor.trilulilu'


class TwitchPlaylistBaseIE(TwitchBaseIE):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.twitch'


class TwitchVideosBaseIE(TwitchPlaylistBaseIE):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.twitch'


class TwitchAllVideosIE(TwitchVideosBaseIE):
    _VALID_URL = u'https?://(?:(?:www|go|m)\\.)?twitch\\.tv/(?P<id>[^/]+)/videos/all'
    _module = 'youtube_dl.extractor.twitch'


class TVPWebsiteIE(LazyLoadExtractor):
    _VALID_URL = u'https?://vod\\.tvp\\.pl/website/(?P<display_id>[^,]+),(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.tvp'


class TVPEmbedIE(LazyLoadExtractor):
    _VALID_URL = u'(?:tvp:|https?://[^/]+\\.tvp\\.(?:pl|info)/sess/tvplayer\\.php\\?.*?object_id=)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.tvp'


class DctpTvIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?dctp\\.tv/(?:#/)?filme/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.dctp'


class ElPaisIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:[^.]+\\.)?elpais\\.com/.*/(?P<id>[^/#?]+)\\.html(?:$|[?#])'
    _module = 'youtube_dl.extractor.elpais'


class ABCOTVSClipsIE(LazyLoadExtractor):
    _VALID_URL = u'https?://clips\\.abcotvs\\.com/(?:[^/]+/)*video/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.abcotvs'


class WatchBoxIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?watchbox\\.de/(?P<kind>serien|filme)/(?:[^/]+/)*[^/]+-(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.watchbox'


class RtlNlIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n        https?://(?:(?:www|static)\\.)?\n        (?:\n            rtlxl\\.nl/[^\\#]*\\#!/[^/]+/|\n            rtl\\.nl/(?:(?:system/videoplayer/(?:[^/]+/)+(?:video_)?embed\\.html|embed)\\b.+?\\buuid=|video/)\n        )\n        (?P<id>[0-9a-f-]+)'
    _module = 'youtube_dl.extractor.rtlnl'


class CBSNewsLiveVideoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?cbsnews\\.com/live/video/(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.cbsnews'


class RuutuIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?:ruutu|supla)\\.fi/(?:video|supla)/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.ruutu'


class EllenTubeVideoIE(EllenTubeBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?ellentube\\.com/video/(?P<id>.+?)\\.html'
    _module = 'youtube_dl.extractor.ellentube'


class UstreamIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?ustream\\.tv/(?P<type>recorded|embed|embed/recorded)/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.ustream'


class JamendoBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.jamendo'


class JamendoAlbumIE(JamendoBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?jamendo\\.com/album/(?P<id>[0-9]+)/(?P<display_id>[\\w-]+)'
    _module = 'youtube_dl.extractor.jamendo'


class DumpertIE(LazyLoadExtractor):
    _VALID_URL = u'(?P<protocol>https?)://(?:www\\.)?dumpert\\.nl/(?:mediabase|embed)/(?P<id>[0-9]+/[0-9a-zA-Z]+)'
    _module = 'youtube_dl.extractor.dumpert'


class PlayFMIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?play\\.fm/(?P<slug>(?:[^/]+/)+(?P<id>[^/]+))/?(?:$|[?#])'
    _module = 'youtube_dl.extractor.playfm'


class DiscoveryIE(DiscoveryGoBaseIE):
    _VALID_URL = u'(?x)https?://\n        (?P<site>\n            (?:www\\.)?\n                (?:\n                    discovery|\n                    investigationdiscovery|\n                    discoverylife|\n                    animalplanet|\n                    ahctv|\n                    destinationamerica|\n                    sciencechannel|\n                    tlc|\n                    velocity\n                )|\n            watch\\.\n                (?:\n                    hgtv|\n                    foodnetwork|\n                    travelchannel|\n                    diynetwork|\n                    cookingchanneltv|\n                    motortrend\n                )\n        )\\.com(?P<path>/tv-shows/[^/]+/(?:video|full-episode)s/(?P<id>[^./?#]+))'
    _module = 'youtube_dl.extractor.discovery'


class GloboIE(LazyLoadExtractor):
    _VALID_URL = u'(?:globo:|https?://.+?\\.globo\\.com/(?:[^/]+/)*(?:v/(?:[^/]+/)?|videos/))(?P<id>\\d{7,})'
    _module = 'youtube_dl.extractor.globo'


class FreesoundIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?freesound\\.org/people/[^/]+/sounds/(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.freesound'


class ViddlerIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?viddler\\.com/(?:v|embed|player)/(?P<id>[a-z0-9]+)(?:.+?\\bsecret=(\\d+))?'
    _module = 'youtube_dl.extractor.viddler'


class CBCWatchBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.cbc'


class CBCWatchIE(CBCWatchBaseIE):
    _VALID_URL = u'https?://(?:gem|watch)\\.cbc\\.ca/(?:[^/]+/)+(?P<id>[0-9a-f-]+)'
    _module = 'youtube_dl.extractor.cbc'


class TwitchStreamIE(TwitchBaseIE):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:\n                            (?:(?:www|go|m)\\.)?twitch\\.tv/|\n                            player\\.twitch\\.tv/\\?.*?\\bchannel=\n                        )\n                        (?P<id>[^/#?]+)\n                    '
    _module = 'youtube_dl.extractor.twitch'

    @classmethod
    def suitable(cls, url):
        return (False
                if any(ie.suitable(url) for ie in (
                    TwitchVideoIE,
                    TwitchChapterIE,
                    TwitchVodIE,
                    TwitchProfileIE,
                    TwitchAllVideosIE,
                    TwitchUploadsIE,
                    TwitchPastBroadcastsIE,
                    TwitchHighlightsIE,
                    TwitchClipsIE))
                else super(TwitchStreamIE, cls).suitable(url))


class MangomoloBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.mangomolo'


class MangomoloLiveIE(MangomoloBaseIE):
    _VALID_URL = u'https?://admin\\.mangomolo\\.com/analytics/index\\.php/customers/embed/index\\?.*?\\bchannelid=(?P<id>(?:[A-Za-z0-9+/=]|%2B|%2F|%3D)+)'
    _module = 'youtube_dl.extractor.mangomolo'


class CrunchyrollBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.crunchyroll'


class CrunchyrollShowPlaylistIE(CrunchyrollBaseIE):
    _VALID_URL = u'https?://(?:(?P<prefix>www|m)\\.)?(?P<url>crunchyroll\\.com/(?!(?:news|anime-news|library|forum|launchcalendar|lineup|store|comics|freetrial|login|media-\\d+))(?P<id>[\\w\\-]+))/?(?:\\?|$)'
    _module = 'youtube_dl.extractor.crunchyroll'


class PornerBrosIE(FourTubeBaseIE):
    _VALID_URL = u'https?://(?:(?P<kind>www|m)\\.)?pornerbros\\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.fourtube'


class NexxEmbedIE(LazyLoadExtractor):
    _VALID_URL = u'https?://embed\\.nexx(?:\\.cloud|cdn\\.com)/\\d+/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.nexx'


class WeiboIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?weibo\\.com/[0-9]+/(?P<id>[a-zA-Z0-9]+)'
    _module = 'youtube_dl.extractor.weibo'


class ArteTvIE(LazyLoadExtractor):
    _VALID_URL = u'https?://videos\\.arte\\.tv/(?P<lang>fr|de|en|es)/.*-(?P<id>.*?)\\.html'
    _module = 'youtube_dl.extractor.arte'


class GameOnePlaylistIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?gameone\\.de(?:/tv)?/?$'
    _module = 'youtube_dl.extractor.gameone'


class CharlieRoseIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?charlierose\\.com/(?:video|episode)(?:s|/player)/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.charlierose'


class RadioFranceIE(LazyLoadExtractor):
    _VALID_URL = u'^https?://maison\\.radiofrance\\.fr/radiovisions/(?P<id>[^?#]+)'
    _module = 'youtube_dl.extractor.radiofrance'


class ViceIE(AdobePassIE):
    _VALID_URL = u'https?://(?:(?:video|vms)\\.vice|(?:www\\.)?viceland)\\.com/(?P<locale>[^/]+)/(?:video/[^/]+|embed)/(?P<id>[\\da-f]+)'
    _module = 'youtube_dl.extractor.vice'


class CoubIE(LazyLoadExtractor):
    _VALID_URL = u'(?:coub:|https?://(?:coub\\.com/(?:view|embed|coubs)/|c-cdn\\.coub\\.com/fb-player\\.swf\\?.*\\bcoub(?:ID|id)=))(?P<id>[\\da-z]+)'
    _module = 'youtube_dl.extractor.coub'


class GodTubeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?godtube\\.com/watch/\\?v=(?P<id>[\\da-zA-Z]+)'
    _module = 'youtube_dl.extractor.godtube'


class VidLiiIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?vidlii\\.com/(?:watch|embed)\\?.*?\\bv=(?P<id>[0-9A-Za-z_-]{11})'
    _module = 'youtube_dl.extractor.vidlii'


class VideaIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        videa(?:kid)?\\.hu/\n                        (?:\n                            videok/(?:[^/]+/)*[^?#&]+-|\n                            player\\?.*?\\bv=|\n                            player/v/\n                        )\n                        (?P<id>[^?#&]+)\n                    '
    _module = 'youtube_dl.extractor.videa'


class ITVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?itv\\.com/hub/[^/]+/(?P<id>[0-9a-zA-Z]+)'
    _module = 'youtube_dl.extractor.itv'


class PluralsightBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.pluralsight'


class PluralsightCourseIE(PluralsightBaseIE):
    _VALID_URL = u'https?://(?:(?:www|app)\\.)?pluralsight\\.com/(?:library/)?courses/(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.pluralsight'


class PicartoVodIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www.)?picarto\\.tv/videopopout/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.picarto'


class VLiveChannelIE(LazyLoadExtractor):
    _VALID_URL = u'https?://channels\\.vlive\\.tv/(?P<id>[0-9A-Z]+)'
    _module = 'youtube_dl.extractor.vlive'


class HarkIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?hark\\.com/clips/(?P<id>.+?)-.+'
    _module = 'youtube_dl.extractor.hark'


class PearVideoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?pearvideo\\.com/video_(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.pearvideo'


class RENTVArticleIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?ren\\.tv/novosti/\\d{4}-\\d{2}-\\d{2}/(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.rentv'


class ORFFM4StoryIE(LazyLoadExtractor):
    _VALID_URL = u'https?://fm4\\.orf\\.at/stories/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.orf'


class NuevoBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.nuevo'


class LoveHomePornIE(NuevoBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?lovehomeporn\\.com/video/(?P<id>\\d+)(?:/(?P<display_id>[^/?#&]+))?'
    _module = 'youtube_dl.extractor.lovehomeporn'


class DRTVLiveIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?dr\\.dk/(?:tv|TV)/live/(?P<id>[\\da-z-]+)'
    _module = 'youtube_dl.extractor.drtv'


class ARDIE(LazyLoadExtractor):
    _VALID_URL = u'(?P<mainurl>https?://(www\\.)?daserste\\.de/[^?#]+/videos/(?P<display_id>[^/?#]+)-(?P<id>[0-9]+))\\.html'
    _module = 'youtube_dl.extractor.ard'


class NYTimesBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.nytimes'


class NYTimesArticleIE(NYTimesBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?nytimes\\.com/(.(?<!video))*?/(?:[^/]+/)*(?P<id>[^.]+)(?:\\.html)?'
    _module = 'youtube_dl.extractor.nytimes'


class ChirbitProfileIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?chirbit\\.com/(?:rss/)?(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.chirbit'


class TheInterceptIE(LazyLoadExtractor):
    _VALID_URL = u'https?://theintercept\\.com/fieldofvision/(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.theintercept'


class MallTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?mall\\.tv/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.malltv'


class TVPlayerIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?tvplayer\\.com/watch/(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.tvplayer'


class NiconicoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.|secure\\.|sp\\.)?nicovideo\\.jp/watch/(?P<id>(?:[a-z]{2})?[0-9]+)'
    _module = 'youtube_dl.extractor.niconico'


class LentaIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?lenta\\.ru/[^/]+/\\d+/\\d+/\\d+/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.lenta'


class ReverbNationIE(LazyLoadExtractor):
    _VALID_URL = u'^https?://(?:www\\.)?reverbnation\\.com/.*?/song/(?P<id>\\d+).*?$'
    _module = 'youtube_dl.extractor.reverbnation'


class TNAFlixNetworkBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.tnaflix'


class TNAEMPFlixBaseIE(TNAFlixNetworkBaseIE):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.tnaflix'


class EMPFlixIE(TNAEMPFlixBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?empflix\\.com/(?:videos/(?P<display_id>.+?)-|[^/]+/(?P<display_id_2>[^/]+)/video)(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.tnaflix'


class TheSceneIE(LazyLoadExtractor):
    _VALID_URL = u'https?://thescene\\.com/watch/[^/]+/(?P<id>[^/#?]+)'
    _module = 'youtube_dl.extractor.thescene'


class HRTiBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.hrti'


class HRTiIE(HRTiBaseIE):
    _VALID_URL = u'(?x)\n                        (?:\n                            hrti:(?P<short_id>[0-9]+)|\n                            https?://\n                                hrti\\.hrt\\.hr/(?:\\#/)?video/show/(?P<id>[0-9]+)/(?P<display_id>[^/]+)?\n                        )\n                    '
    _module = 'youtube_dl.extractor.hrti'


class MatchTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://matchtv\\.ru(?:/on-air|/?#live-player)'
    _module = 'youtube_dl.extractor.matchtv'


class SBSIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?sbs\\.com\\.au/(?:ondemand|news)/video/(?:single/)?(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.sbs'


class CriterionIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?criterion\\.com/films/(?P<id>[0-9]+)-.+'
    _module = 'youtube_dl.extractor.criterion'


class MicrosoftVirtualAcademyBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.microsoftvirtualacademy'


class MicrosoftVirtualAcademyCourseIE(MicrosoftVirtualAcademyBaseIE):
    _VALID_URL = u'(?:mva:course:|https?://(?:mva\\.microsoft|(?:www\\.)?microsoftvirtualacademy)\\.com/[^/]+/training-courses/(?P<display_id>[^/?#&]+)-)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.microsoftvirtualacademy'

    @classmethod
    def suitable(cls, url):
        return False if MicrosoftVirtualAcademyIE.suitable(url) else super(
            MicrosoftVirtualAcademyCourseIE, cls).suitable(url)


class NownessSeriesIE(NownessBaseIE):
    _VALID_URL = u'https?://(?:(?:www|cn)\\.)?nowness\\.com/series/(?P<id>[^/]+?)(?:$|[?#])'
    _module = 'youtube_dl.extractor.nowness'


class UDNEmbedIE(LazyLoadExtractor):
    _VALID_URL = u'https?://video\\.udn\\.com/(?:embed|play)/news/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.udn'


class AdobeTVBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.adobetv'


class AdobeTVPlaylistBaseIE(AdobeTVBaseIE):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.adobetv'


class AdobeTVShowIE(AdobeTVPlaylistBaseIE):
    _VALID_URL = u'https?://tv\\.adobe\\.com/(?:(?P<language>fr|de|es|jp)/)?show/(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.adobetv'


class MediasiteNamedCatalogIE(LazyLoadExtractor):
    _VALID_URL = u'(?xi)(?P<url>https?://[^/]+/Mediasite)/Catalog/catalogs/(?P<catalog_name>[^/?#&]+)'
    _module = 'youtube_dl.extractor.mediasite'


class ViewLiftBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.viewlift'


class ViewLiftIE(ViewLiftBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?(?P<domain>(?:snagfilms|snagxtreme|funnyforfree|kiddovid|winnersview|(?:monumental|lax)sportsnetwork|vayafilm)\\.com|hoichoi\\.tv)/(?:films/title|show|(?:news/)?videos?)/(?P<id>[^?#]+)'
    _module = 'youtube_dl.extractor.viewlift'


class InaIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?ina\\.fr/(?:video|audio)/(?P<id>[A-Z0-9_]+)'
    _module = 'youtube_dl.extractor.ina'


class CommonMistakesIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n        (?:url|URL)$\n    '
    _module = 'youtube_dl.extractor.commonmistakes'


class KuwoSingerIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?kuwo\\.cn/mingxing/(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.kuwo'


class NownessPlaylistIE(NownessBaseIE):
    _VALID_URL = u'https?://(?:(?:www|cn)\\.)?nowness\\.com/playlist/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.nowness'


class VideoPremiumIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?videopremium\\.(?:tv|me)/(?P<id>\\w+)(?:/.*)?'
    _module = 'youtube_dl.extractor.videopremium'


class ToggleIE(LazyLoadExtractor):
    _VALID_URL = u'https?://video\\.toggle\\.sg/(?:en|zh)/(?:[^/]+/){2,}(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.toggle'


class AnimeOnDemandIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?anime-on-demand\\.de/anime/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.animeondemand'


class ViqeoIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                        (?:\n                            viqeo:|\n                            https?://cdn\\.viqeo\\.tv/embed/*\\?.*?\\bvid=|\n                            https?://api\\.viqeo\\.tv/v\\d+/data/startup?.*?\\bvideo(?:%5B%5D|\\[\\])=\n                        )\n                        (?P<id>[\\da-f]+)\n                    '
    _module = 'youtube_dl.extractor.viqeo'


class TF1IE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:videos|www|lci)\\.tf1|(?:www\\.)?(?:tfou|ushuaiatv|histoire|tvbreizh))\\.fr/(?:[^/]+/)*(?P<id>[^/?#.]+)'
    _module = 'youtube_dl.extractor.tf1'


class TFOIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?tfo\\.org/(?:en|fr)/(?:[^/]+/){2}(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.tfo'


class NDRBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.ndr'


class NDRIE(NDRBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?ndr\\.de/(?:[^/]+/)*(?P<id>[^/?#]+),[\\da-z]+\\.html'
    _module = 'youtube_dl.extractor.ndr'


class DefenseGouvFrIE(LazyLoadExtractor):
    _VALID_URL = u'https?://.*?\\.defense\\.gouv\\.fr/layout/set/ligthboxvideo/base-de-medias/webtv/(?P<id>[^/?#]*)'
    _module = 'youtube_dl.extractor.defense'


class MarkizaIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?videoarchiv\\.markiza\\.sk/(?:video/(?:[^/]+/)*|embed/)(?P<id>\\d+)(?:[_/]|$)'
    _module = 'youtube_dl.extractor.markiza'


class XstreamIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    (?:\n                        xstream:|\n                        https?://frontend\\.xstream\\.(?:dk|net)/\n                    )\n                    (?P<partner_id>[^/]+)\n                    (?:\n                        :|\n                        /feed/video/\\?.*?\\bid=\n                    )\n                    (?P<id>\\d+)\n                    '
    _module = 'youtube_dl.extractor.xstream'


class NovaEmbedIE(LazyLoadExtractor):
    _VALID_URL = u'https?://media\\.cms\\.nova\\.cz/embed/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.nova'


class YahooGyaOPlayerIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:gyao\\.yahoo\\.co\\.jp/(?:player|episode/[^/]+)|streaming\\.yahoo\\.co\\.jp/c/y)/(?P<id>\\d+/v\\d+/v\\d+|[\\da-f]{8}-[\\da-f]{4}-[\\da-f]{4}-[\\da-f]{4}-[\\da-f]{12})'
    _module = 'youtube_dl.extractor.yahoo'


class TV2ArticleIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?tv2\\.no/(?:a|\\d{4}/\\d{2}/\\d{2}(/[^/]+)+)/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.tv2'


class EllenTubeIE(EllenTubeBaseIE):
    _VALID_URL = u'(?x)\n                        (?:\n                            ellentube:|\n                            https://api-prod\\.ellentube\\.com/ellenapi/api/item/\n                        )\n                        (?P<id>[\\da-f]{8}-[\\da-f]{4}-[\\da-f]{4}-[\\da-f]{4}-[\\da-f]{12})\n                    '
    _module = 'youtube_dl.extractor.ellentube'


class VesselIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?vessel\\.com/(?:videos|embed)/(?P<id>[0-9a-zA-Z-_]+)'
    _module = 'youtube_dl.extractor.vessel'


class HeiseIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?heise\\.de/(?:[^/]+/)+[^/]+-(?P<id>[0-9]+)\\.html'
    _module = 'youtube_dl.extractor.heise'


class TikTokBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.tiktok'


class TikTokUserIE(TikTokBaseIE):
    _VALID_URL = u'(?x)\n                        https?://\n                            (?:\n                                (?:m\\.)?tiktok\\.com/h5/share/usr|\n                                (?:www\\.)?tiktok\\.com/share/user\n                            )\n                            /(?P<id>\\d+)\n                    '
    _module = 'youtube_dl.extractor.tiktok'


class AddAnimeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:\\w+\\.)?add-anime\\.net/(?:watch_video\\.php\\?(?:.*?)v=|video/)(?P<id>[\\w_]+)'
    _module = 'youtube_dl.extractor.addanime'


class BitChuteChannelIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?bitchute\\.com/channel/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.bitchute'


class YoutubeBaseInfoExtractor(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.youtube'


class YoutubeEntryListBaseInfoExtractor(YoutubeBaseInfoExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.youtube'


class YoutubePlaylistBaseInfoExtractor(YoutubeEntryListBaseInfoExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.youtube'


class YoutubeSearchBaseInfoExtractor(YoutubePlaylistBaseInfoExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.youtube'


class YoutubeSearchIE(LazyLoadSearchExtractor, YoutubeSearchBaseInfoExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.youtube'

    @classmethod
    def suitable(cls, url):
        return re.match(cls._make_valid_url(), url) is not None

    @classmethod
    def _make_valid_url(cls):
        return u'ytsearch(?P<prefix>|[1-9][0-9]*|all):(?P<query>[\\s\\S]+)'


class StitcherIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?stitcher\\.com/podcast/(?:[^/]+/)+e/(?:(?P<display_id>[^/#?&]+?)-)?(?P<id>\\d+)(?:[/#?&]|$)'
    _module = 'youtube_dl.extractor.stitcher'


class Channel9IE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?:channel9\\.msdn\\.com|s\\.ch9\\.ms)/(?P<contentpath>.+?)(?P<rss>/RSS)?/?(?:[?#&]|$)'
    _module = 'youtube_dl.extractor.channel9'


class VrakIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?vrak\\.tv/videos\\?.*?\\btarget=(?P<id>[\\d.]+)'
    _module = 'youtube_dl.extractor.vrak'


class ArkenaIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                        https?://\n                            (?:\n                                video\\.arkena\\.com/play2/embed/player\\?|\n                                play\\.arkena\\.com/(?:config|embed)/avp/v\\d/player/media/(?P<id>[^/]+)/[^/]+/(?P<account_id>\\d+)\n                            )\n                        '
    _module = 'youtube_dl.extractor.arkena'


class OktoberfestTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?oktoberfest-tv\\.de/[^/]+/[^/]+/video/(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.oktoberfesttv'


class TVNoeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?tvnoe\\.cz/video/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.tvnoe'


class DWIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?dw\\.com/(?:[^/]+/)+(?:av|e)-(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.dw'


class ZDFBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.zdf'


class ZDFIE(ZDFBaseIE):
    _VALID_URL = u'https?://www\\.zdf\\.de/(?:[^/]+/)*(?P<id>[^/?]+)\\.html'
    _module = 'youtube_dl.extractor.zdf'


class YandexMusicPlaylistBaseIE(YandexMusicBaseIE):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.yandexmusic'


class YandexMusicAlbumIE(YandexMusicPlaylistBaseIE):
    _VALID_URL = u'https?://music\\.yandex\\.(?:ru|kz|ua|by)/album/(?P<id>\\d+)/?(\\?|$)'
    _module = 'youtube_dl.extractor.yandexmusic'


class CSNNEIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?csnne\\.com/video/(?P<id>[0-9a-z-]+)'
    _module = 'youtube_dl.extractor.nbc'


class PinkbikeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:www\\.)?pinkbike\\.com/video/|es\\.pinkbike\\.org/i/kvid/kvid-y5\\.swf\\?id=)(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.pinkbike'


class DeezerPlaylistIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?deezer\\.com/playlist/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.deezer'


class DRBonanzaIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?dr\\.dk/bonanza/[^/]+/\\d+/[^/]+/(?P<id>\\d+)/(?P<display_id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.drbonanza'


class FranceTVInfoSportIE(FranceTVBaseInfoExtractor):
    _VALID_URL = u'https?://sport\\.francetvinfo\\.fr/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.francetv'


class TEDIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n        (?P<proto>https?://)\n        (?P<type>www|embed(?:-ssl)?)(?P<urlmain>\\.ted\\.com/\n        (\n            (?P<type_playlist>playlists(?:/\\d+)?) # We have a playlist\n            |\n            ((?P<type_talk>talks)) # We have a simple talk\n            |\n            (?P<type_watch>watch)/[^/]+/[^/]+\n        )\n        (/lang/(.*?))? # The url may contain the language\n        /(?P<name>[\\w-]+) # Here goes the name and then ".html"\n        .*)$\n        '
    _module = 'youtube_dl.extractor.ted'


class StretchInternetIE(LazyLoadExtractor):
    _VALID_URL = u'https?://portal\\.stretchinternet\\.com/[^/]+/portal\\.htm\\?.*?\\beventId=(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.stretchinternet'


class PlatziIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:\n                            platzi\\.com/clases|           # es version\n                            courses\\.platzi\\.com/classes  # en version\n                        )/[^/]+/(?P<id>\\d+)-[^/?\\#&]+\n                    '
    _module = 'youtube_dl.extractor.platzi'


class SVTPageIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?svt\\.se/(?:[^/]+/)*(?P<id>[^/?&#]+)'
    _module = 'youtube_dl.extractor.svt'

    @classmethod
    def suitable(cls, url):
        return False if SVTIE.suitable(url) else super(SVTPageIE, cls).suitable(url)


class MTVDEIE(MTVServicesInfoExtractor):
    _VALID_URL = u'https?://(?:www\\.)?mtv\\.de/(?:artists|shows|news)/(?:[^/]+/)*(?P<id>\\d+)-[^/#?]+/*(?:[#?].*)?$'
    _module = 'youtube_dl.extractor.mtv'


class CNBCIE(LazyLoadExtractor):
    _VALID_URL = u'https?://video\\.cnbc\\.com/gallery/\\?video=(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.cnbc'


class NonkTubeIE(NuevoBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?nonktube\\.com/(?:(?:video|embed)/|media/nuevo/embed\\.php\\?.*?\\bid=)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.nonktube'


class GloboArticleIE(LazyLoadExtractor):
    _VALID_URL = u'https?://.+?\\.globo\\.com/(?:[^/]+/)*(?P<id>[^/.]+)(?:\\.html)?'
    _module = 'youtube_dl.extractor.globo'

    @classmethod
    def suitable(cls, url):
        return False if GloboIE.suitable(url) else super(GloboArticleIE, cls).suitable(url)


class TwitchVideoIE(TwitchItemBaseIE):
    _VALID_URL = u'https?://(?:(?:www|go|m)\\.)?twitch\\.tv/[^/]+/b/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.twitch'


class EitbIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?eitb\\.tv/(?:eu/bideoa|es/video)/[^/]+/\\d+/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.eitb'


class URPlayIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?ur(?:play|skola)\\.se/(?:program|Produkter)/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.urplay'


class PolskieRadioCategoryIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?polskieradio\\.pl/\\d+(?:,[^/]+)?/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.polskieradio'

    @classmethod
    def suitable(cls, url):
        return False if PolskieRadioIE.suitable(url) else super(PolskieRadioCategoryIE, cls).suitable(url)


class TvigleIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?:tvigle\\.ru/(?:[^/]+/)+(?P<display_id>[^/]+)/$|cloud\\.tvigle\\.ru/video/(?P<id>\\d+))'
    _module = 'youtube_dl.extractor.tvigle'


class TuneInProgramIE(TuneInBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?tunein\\.com/(?:radio/.*?-p|program/.*?ProgramId=|embed/player/p)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.tunein'


class BusinessInsiderIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:[^/]+\\.)?businessinsider\\.(?:com|nl)/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.businessinsider'


class NowVideoIE(NovaMovIE):
    _VALID_URL = u'(?x)\n                            http://\n                                (?:\n                                    (?:www\\.)?nowvideo\\.(?:to|ch|ec|sx|eu|at|ag|co|li)/(?:file|video|mobile/\\#/videos)/|\n                                    (?:(?:embed|www)\\.)nowvideo\\.(?:to|ch|ec|sx|eu|at|ag|co|li)/embed(?:\\.php|/)?\\?(?:.*?&)?\\bv=\n                                )\n                                (?P<id>[a-z\\d]{13})\n                            '
    _module = 'youtube_dl.extractor.novamov'


class NTVDeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?n-tv\\.de/mediathek/videos/[^/?#]+/[^/?#]+-article(?P<id>.+)\\.html'
    _module = 'youtube_dl.extractor.ntvde'


class CarambaTVIE(LazyLoadExtractor):
    _VALID_URL = u'(?:carambatv:|https?://video1\\.carambatv\\.ru/v/)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.carambatv'


class TikTokIE(TikTokBaseIE):
    _VALID_URL = u'(?x)\n                        https?://\n                            (?:\n                                (?:m\\.)?tiktok\\.com/v|\n                                (?:www\\.)?tiktok\\.com/share/video\n                            )\n                            /(?P<id>\\d+)\n                    '
    _module = 'youtube_dl.extractor.tiktok'


class TwitchHighlightsIE(TwitchVideosBaseIE):
    _VALID_URL = u'https?://(?:(?:www|go|m)\\.)?twitch\\.tv/(?P<id>[^/]+)/videos/highlights'
    _module = 'youtube_dl.extractor.twitch'


class LecturioIE(LecturioBaseIE):
    _VALID_URL = u'(?x)\n                    https://\n                        (?:\n                            app\\.lecturio\\.com/[^/]+/(?P<id>[^/?#&]+)\\.lecture|\n                            (?:www\\.)?lecturio\\.de/[^/]+/(?P<id_de>[^/?#&]+)\\.vortrag\n                        )\n                    '
    _module = 'youtube_dl.extractor.lecturio'


class XHamsterIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:.+?\\.)?xhamster\\.(?:com|one)/\n                        (?:\n                            movies/(?P<id>\\d+)/(?P<display_id>[^/]*)\\.html|\n                            videos/(?P<display_id_2>[^/]*)-(?P<id_2>\\d+)\n                        )\n                    '
    _module = 'youtube_dl.extractor.xhamster'


class HypemIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?hypem\\.com/track/(?P<id>[0-9a-z]{5})'
    _module = 'youtube_dl.extractor.hypem'


class GameInformerIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?gameinformer\\.com/(?:[^/]+/)*(?P<id>.+)\\.aspx'
    _module = 'youtube_dl.extractor.gameinformer'


class IviIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?ivi\\.(?:ru|tv)/(?:watch/(?:[^/]+/)?|video/player\\?.*?videoId=)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.ivi'


class SenateISVPIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?senate\\.gov/isvp/?\\?(?P<qs>.+)'
    _module = 'youtube_dl.extractor.senateisvp'


class DTubeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?d\\.tube/(?:#!/)?v/(?P<uploader_id>[0-9a-z.-]+)/(?P<id>[0-9a-z]{8})'
    _module = 'youtube_dl.extractor.dtube'


class AsianCrushIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?asiancrush\\.com/video/(?:[^/]+/)?0+(?P<id>\\d+)v\\b'
    _module = 'youtube_dl.extractor.asiancrush'


class CCMAIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?ccma\\.cat/(?:[^/]+/)*?(?P<type>video|audio)/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.ccma'


class WSJArticleIE(LazyLoadExtractor):
    _VALID_URL = u'(?i)https?://(?:www\\.)?wsj\\.com/articles/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.wsj'


class SeznamZpravyArticleIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?:seznam\\.cz/zpravy|seznamzpravy\\.cz)/clanek/(?:[^/?#&]+)-(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.seznamzpravy'


class PeriscopeBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.periscope'


class PeriscopeUserIE(PeriscopeBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?(?:periscope|pscp)\\.tv/(?P<id>[^/]+)/?$'
    _module = 'youtube_dl.extractor.periscope'


class EuropaIE(LazyLoadExtractor):
    _VALID_URL = u'https?://ec\\.europa\\.eu/avservices/(?:video/player|audio/audioDetails)\\.cfm\\?.*?\\bref=(?P<id>[A-Za-z0-9-]+)'
    _module = 'youtube_dl.extractor.europa'


class CNNBlogsIE(LazyLoadExtractor):
    _VALID_URL = u'https?://[^\\.]+\\.blogs\\.cnn\\.com/.+'
    _module = 'youtube_dl.extractor.cnn'


class Tele5IE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?tele5\\.de/(?:mediathek|tv)/(?P<id>[^?#&]+)'
    _module = 'youtube_dl.extractor.tele5'


class PluralsightIE(PluralsightBaseIE):
    _VALID_URL = u'https?://(?:(?:www|app)\\.)?pluralsight\\.com/(?:training/)?player\\?'
    _module = 'youtube_dl.extractor.pluralsight'


class QuantumTVIE(ZattooIE):
    _VALID_URL = u'https?://(?:www\\.)?quantum\\-tv\\.com/watch/(?P<channel>[^/]+?)/(?P<id>[0-9]+)[^/]+(?:/(?P<recid>[0-9]+))?'
    _module = 'youtube_dl.extractor.zattoo'


class OnetPlIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:[^/]+\\.)?(?:onet|businessinsider\\.com|plejada)\\.pl/(?:[^/]+/)+(?P<id>[0-9a-z]+)'
    _module = 'youtube_dl.extractor.onet'


class HitRecordIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?hitrecord\\.org/records/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.hitrecord'


class RegioTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?regio-tv\\.de/video/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.regiotv'


class VidbitIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?vidbit\\.co/(?:watch|embed)\\?.*?\\bv=(?P<id>[\\da-zA-Z]+)'
    _module = 'youtube_dl.extractor.vidbit'


class PeriscopeIE(PeriscopeBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?(?:periscope|pscp)\\.tv/[^/]+/(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.periscope'


class RudoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://rudo\\.video/vod/(?P<id>[0-9a-zA-Z]+)'
    _module = 'youtube_dl.extractor.rudo'


class JeuxVideoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://.*?\\.jeuxvideo\\.com/.*/(.*?)\\.htm'
    _module = 'youtube_dl.extractor.jeuxvideo'


class DHMIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?dhm\\.de/filmarchiv/(?:[^/]+/)+(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.dhm'


class EpornerIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?eporner\\.com/(?:hd-porn|embed)/(?P<id>\\w+)(?:/(?P<display_id>[\\w-]+))?'
    _module = 'youtube_dl.extractor.eporner'


class AWAANIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?:awaan|dcndigital)\\.ae/(?:#/)?show/(?P<show_id>\\d+)/[^/]+(?:/(?P<video_id>\\d+)/(?P<season_id>\\d+))?'
    _module = 'youtube_dl.extractor.awaan'


class TVLandIE(MTVServicesInfoExtractor):
    _VALID_URL = u'https?://(?:www\\.)?tvland\\.com/(?:video-clips|(?:full-)?episodes)/(?P<id>[^/?#.]+)'
    _module = 'youtube_dl.extractor.tvland'


class BBCCoUkIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:www\\.)?bbc\\.co\\.uk/\n                        (?:\n                            programmes/(?!articles/)|\n                            iplayer(?:/[^/]+)?/(?:episode/|playlist/)|\n                            music/(?:clips|audiovideo/popular)[/#]|\n                            radio/player/|\n                            events/[^/]+/play/[^/]+/\n                        )\n                        (?P<id>(?:[pbm][\\da-z]{7}|w[\\da-z]{7,14}))(?!/(?:episodes|broadcasts|clips))\n                    '
    _module = 'youtube_dl.extractor.bbc'


class FrontendMastersPageBaseIE(FrontendMastersBaseIE):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.frontendmasters'


class FrontendMastersLessonIE(FrontendMastersPageBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?frontendmasters\\.com/courses/(?P<course_name>[^/]+)/(?P<lesson_name>[^/]+)'
    _module = 'youtube_dl.extractor.frontendmasters'


class NormalbootsIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?normalboots\\.com/video/(?P<id>[0-9a-z-]*)/?$'
    _module = 'youtube_dl.extractor.normalboots'


class TVPlayHomeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://tvplay\\.(?:tv3\\.lt|skaties\\.lv|tv3\\.ee)/[^/]+/[^/?#&]+-(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.tvplay'


class GameSpotIE(OnceIE):
    _VALID_URL = u'https?://(?:www\\.)?gamespot\\.com/(?:video|article|review)s/(?:[^/]+/\\d+-|embed/)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.gamespot'


class DiscoveryVRIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?discoveryvr\\.com/watch/(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.discoveryvr'


class VootIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?voot\\.com/(?:[^/]+/)+(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.voot'


class ComedyCentralFullEpisodesIE(MTVServicesInfoExtractor):
    _VALID_URL = u'(?x)https?://(?:www\\.)?cc\\.com/\n        (?:full-episodes|shows(?=/[^/]+/full-episodes))\n        /(?P<id>[^?]+)'
    _module = 'youtube_dl.extractor.comedycentral'


class ClypIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?clyp\\.it/(?P<id>[a-z0-9]+)'
    _module = 'youtube_dl.extractor.clyp'


class TeachableBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.teachable'


class TeachableIE(TeachableBaseIE):
    _VALID_URL = u'(?x)\n                    (?:\n                        teachable:https?://(?P<site_t>[^/]+)|\n                        https?://(?:www\\.)?(?P<site>edurila\\.com|upskillcourses\\.com|learnability\\.org|courses\\.workitdaily\\.com|academyhacker\\.com|stackskills\\.com|market\\.saleshacker\\.com|academy\\.gns3\\.com)\n                    )\n                    /courses/[^/]+/lectures/(?P<id>\\d+)\n                    '
    _module = 'youtube_dl.extractor.teachable'


class UnityIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?unity3d\\.com/learn/tutorials/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.unity'


class SlidesLiveIE(LazyLoadExtractor):
    _VALID_URL = u'https?://slideslive\\.com/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.slideslive'


class RTVELiveIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?rtve\\.es/directo/(?P<id>[a-zA-Z0-9-]+)'
    _module = 'youtube_dl.extractor.rtve'


class UnicodeBOMIE(LazyLoadExtractor):
    _VALID_URL = u'(?P<bom>\ufeff)(?P<id>.*)$'
    _module = 'youtube_dl.extractor.commonmistakes'


class HellPornoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?hellporno\\.(?:com/videos|net/v)/(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.hellporno'


class YoutubePlaylistsBaseInfoExtractor(YoutubeEntryListBaseInfoExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.youtube'


class YoutubeShowIE(YoutubePlaylistsBaseInfoExtractor):
    _VALID_URL = u'https?://(?:www\\.)?youtube\\.com/show/(?P<id>[^?#]*)'
    _module = 'youtube_dl.extractor.youtube'


class SafariApiIE(SafariBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?(?:safaribooksonline|learning\\.oreilly)\\.com/api/v1/book/(?P<course_id>[^/]+)/chapter(?:-content)?/(?P<part>[^/?#&]+)\\.html'
    _module = 'youtube_dl.extractor.safari'


class OnetBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.onet'


class ClipRsIE(OnetBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?clip\\.rs/(?P<id>[^/]+)/\\d+'
    _module = 'youtube_dl.extractor.cliprs'


class EsriVideoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://video\\.esri\\.com/watch/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.esri'


class SkySportsIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?skysports\\.com/watch/video/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.skysports'


class PornHdIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?pornhd\\.com/(?:[a-z]{2,4}/)?videos/(?P<id>\\d+)(?:/(?P<display_id>.+))?'
    _module = 'youtube_dl.extractor.pornhd'


class RuvIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?ruv\\.is/(?:sarpurinn/[^/]+|node)/(?P<id>[^/]+(?:/\\d+)?)'
    _module = 'youtube_dl.extractor.ruv'


class DiggIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?digg\\.com/video/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.digg'


class NickIE(MTVServicesInfoExtractor):
    _VALID_URL = u'https?://(?P<domain>(?:(?:www|beta)\\.)?nick(?:jr)?\\.com)/(?:[^/]+/)?(?:videos/clip|[^/]+/videos)/(?P<id>[^/?#.]+)'
    _module = 'youtube_dl.extractor.nick'


class FoxNewsArticleIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?:insider\\.)?foxnews\\.com/(?!v)([^/]+/)+(?P<id>[a-z-]+)'
    _module = 'youtube_dl.extractor.foxnews'


class XFileShareIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?P<host>(?:www\\.)?(?:daclips\\.(?:in|com)|filehoot\\.com|gorillavid\\.(?:in|com)|movpod\\.in|powerwatch\\.pw|rapidvideo\\.ws|thevideobee\\.to|vidto\\.(?:me|se)|streamin\\.to|xvidstage\\.com|vidabc\\.com|vidbom\\.com|vidlo\\.us|rapidvideo\\.(?:cool|org)|fastvideo\\.me))/(?:embed-)?(?P<id>[0-9a-zA-Z]+)'
    _module = 'youtube_dl.extractor.xfileshare'


class MinhatecaIE(LazyLoadExtractor):
    _VALID_URL = u'https?://minhateca\\.com\\.br/[^?#]+,(?P<id>[0-9]+)\\.'
    _module = 'youtube_dl.extractor.minhateca'


class StanfordOpenClassroomIE(LazyLoadExtractor):
    _VALID_URL = u'https?://openclassroom\\.stanford\\.edu(?P<path>/?|(/MainFolder/(?:HomePage|CoursePage|VideoPage)\\.php([?]course=(?P<course>[^&]+)(&video=(?P<video>[^&]+))?(&.*)?)?))$'
    _module = 'youtube_dl.extractor.stanfordoc'


class PikselIE(LazyLoadExtractor):
    _VALID_URL = u'https?://player\\.piksel\\.com/v/(?P<id>[a-z0-9]+)'
    _module = 'youtube_dl.extractor.piksel'


class SlutloadIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:\\w+\\.)?slutload\\.com/(?:video/[^/]+|embed_player|watch)/(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.slutload'


class SoundgasmIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?soundgasm\\.net/u/(?P<user>[0-9a-zA-Z_-]+)/(?P<display_id>[0-9a-zA-Z_-]+)'
    _module = 'youtube_dl.extractor.soundgasm'


class TVNowBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.tvnow'


class TVNowIE(TVNowBaseIE):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:www\\.)?tvnow\\.(?:de|at|ch)/(?P<station>[^/]+)/\n                        (?P<show_id>[^/]+)/\n                        (?!(?:list|jahr)(?:/|$))(?P<id>[^/?\\#&]+)\n                    '
    _module = 'youtube_dl.extractor.tvnow'

    @classmethod
    def suitable(cls, url):
        return (False if TVNowNewIE.suitable(url) or TVNowSeasonIE.suitable(url) or TVNowAnnualIE.suitable(url) or TVNowShowIE.suitable(url)
                else super(TVNowIE, cls).suitable(url))


class FlipagramIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?flipagram\\.com/f/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.flipagram'


class YandexMusicPlaylistIE(YandexMusicPlaylistBaseIE):
    _VALID_URL = u'https?://music\\.yandex\\.(?P<tld>ru|kz|ua|by)/users/(?P<user>[^/]+)/playlists/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.yandexmusic'


class MovieClipsIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?movieclips\\.com/videos/.+-(?P<id>\\d+)(?:\\?|$)'
    _module = 'youtube_dl.extractor.movieclips'


class RadioDeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?P<id>.+?)\\.(?:radio\\.(?:de|at|fr|pt|es|pl|it)|rad\\.io)'
    _module = 'youtube_dl.extractor.radiode'


class KuwoMvIE(KuwoBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?kuwo\\.cn/mv/(?P<id>\\d+?)/'
    _module = 'youtube_dl.extractor.kuwo'


class AllocineIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?allocine\\.fr/(?:article|video|film)/(?:fichearticle_gen_carticle=|player_gen_cmedia=|fichefilm_gen_cfilm=|video-)(?P<id>[0-9]+)(?:\\.html)?'
    _module = 'youtube_dl.extractor.allocine'


class NRLTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?nrl\\.com/tv(/[^/]+)*/(?P<id>[^/?&#]+)'
    _module = 'youtube_dl.extractor.nrl'


class UstudioIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:www|v1)\\.)?ustudio\\.com/video/(?P<id>[^/]+)/(?P<display_id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.ustudio'


class TagesschauIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?tagesschau\\.de/(?P<path>[^/]+/(?:[^/]+/)*?(?P<id>[^/#?]+?(?:-?[0-9]+)?))(?:~_?[^/#?]+?)?\\.html'
    _module = 'youtube_dl.extractor.tagesschau'

    @classmethod
    def suitable(cls, url):
        return False if TagesschauPlayerIE.suitable(url) else super(TagesschauIE, cls).suitable(url)


class YoutubeFeedsInfoExtractor(YoutubeBaseInfoExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.youtube'


class YoutubeHistoryIE(YoutubeFeedsInfoExtractor):
    _VALID_URL = u'https?://(?:www\\.)?youtube\\.com/feed/history|:ythistory'
    _module = 'youtube_dl.extractor.youtube'


class LePlaylistIE(LazyLoadExtractor):
    _VALID_URL = u'https?://[a-z]+\\.le\\.com/(?!video)[a-z]+/(?P<id>[a-z0-9_]+)'
    _module = 'youtube_dl.extractor.leeco'

    @classmethod
    def suitable(cls, url):
        return False if LeIE.suitable(url) else super(LePlaylistIE, cls).suitable(url)


class MixcloudIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:www|beta|m)\\.)?mixcloud\\.com/([^/]+)/(?!stream|uploads|favorites|listens|playlists)([^/]+)'
    _module = 'youtube_dl.extractor.mixcloud'


class ImgurIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:i\\.)?imgur\\.com/(?!(?:a|gallery|(?:t(?:opic)?|r)/[^/]+)/)(?P<id>[a-zA-Z0-9]+)'
    _module = 'youtube_dl.extractor.imgur'


class HowcastIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?howcast\\.com/videos/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.howcast'


class Varzesh3IE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?video\\.varzesh3\\.com/(?:[^/]+/)+(?P<id>[^/]+)/?'
    _module = 'youtube_dl.extractor.varzesh3'


class LiTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?litv\\.tv/(?:vod|promo)/[^/]+/(?:content\\.do)?\\?.*?\\b(?:content_)?id=(?P<id>[^&]+)'
    _module = 'youtube_dl.extractor.litv'


class YoutubeSearchURLIE(YoutubeSearchBaseInfoExtractor):
    _VALID_URL = u'https?://(?:www\\.)?youtube\\.com/results\\?(.*?&)?(?:search_query|q)=(?P<query>[^&]+)(?:[&]|$)'
    _module = 'youtube_dl.extractor.youtube'


class VTXTVIE(ZattooIE):
    _VALID_URL = u'https?://(?:www\\.)?vtxtv\\.ch/watch/(?P<channel>[^/]+?)/(?P<id>[0-9]+)[^/]+(?:/(?P<recid>[0-9]+))?'
    _module = 'youtube_dl.extractor.zattoo'


class SpiegelArticleIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?spiegel\\.de/(?!video/)[^?#]*?-(?P<id>[0-9]+)\\.html'
    _module = 'youtube_dl.extractor.spiegel'


class KontrTubeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?kontrtube\\.ru/videos/(?P<id>\\d+)/(?P<display_id>[^/]+)/'
    _module = 'youtube_dl.extractor.kontrtube'


class MTVServicesEmbeddedIE(MTVServicesInfoExtractor):
    _VALID_URL = u'https?://media\\.mtvnservices\\.com/embed/(?P<mgid>.+?)(\\?|/|$)'
    _module = 'youtube_dl.extractor.mtv'


class BioBioChileTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:tv|www)\\.biobiochile\\.cl/(?:notas|noticias)/(?:[^/]+/)+(?P<id>[^/]+)\\.shtml'
    _module = 'youtube_dl.extractor.biobiochiletv'


class VHXEmbedIE(LazyLoadExtractor):
    _VALID_URL = u'https?://embed\\.vhx\\.tv/videos/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.vimeo'


class CuriosityStreamCollectionIE(CuriosityStreamBaseIE):
    _VALID_URL = u'https?://(?:app\\.)?curiositystream\\.com/(?:collection|series)/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.curiositystream'


class RTVETelevisionIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?rtve\\.es/television/[^/]+/[^/]+/(?P<id>\\d+).shtml'
    _module = 'youtube_dl.extractor.rtve'


class NineGagIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?9gag(?:\\.com/tv|\\.tv)/(?:p|embed)/(?P<id>[a-zA-Z0-9]+)(?:/(?P<display_id>[^?#/]+))?'
    _module = 'youtube_dl.extractor.ninegag'


class OnDemandKoreaIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?ondemandkorea\\.com/(?P<id>[^/]+)\\.html'
    _module = 'youtube_dl.extractor.ondemandkorea'


class ESPNArticleIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:espn\\.go|(?:www\\.)?espn)\\.com/(?:[^/]+/)*(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.espn'

    @classmethod
    def suitable(cls, url):
        return False if ESPNIE.suitable(url) else super(ESPNArticleIE, cls).suitable(url)


class XTubeIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                        (?:\n                            xtube:|\n                            https?://(?:www\\.)?xtube\\.com/(?:watch\\.php\\?.*\\bv=|video-watch/(?:embedded/)?(?P<display_id>[^/]+)-)\n                        )\n                        (?P<id>[^/?&#]+)\n                    '
    _module = 'youtube_dl.extractor.xtube'


class SmotriUserIE(LazyLoadExtractor):
    _VALID_URL = u"https?://(?:www\\.)?smotri\\.com/user/(?P<id>[0-9A-Za-z_\\'-]+)"
    _module = 'youtube_dl.extractor.smotri'


class KhanAcademyIE(LazyLoadExtractor):
    _VALID_URL = u'^https?://(?:(?:www|api)\\.)?khanacademy\\.org/(?P<key>[^/]+)/(?:[^/]+/){,2}(?P<id>[^?#/]+)(?:$|[?#])'
    _module = 'youtube_dl.extractor.khanacademy'


class BiliBiliBangumiIE(LazyLoadExtractor):
    _VALID_URL = u'https?://bangumi\\.bilibili\\.com/anime/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.bilibili'

    @classmethod
    def suitable(cls, url):
        return False if BiliBiliIE.suitable(url) else super(BiliBiliBangumiIE, cls).suitable(url)


class MotherlessGroupIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?motherless\\.com/gv?/(?P<id>[a-z0-9_]+)'
    _module = 'youtube_dl.extractor.motherless'

    @classmethod
    def suitable(cls, url):
        return (False if MotherlessIE.suitable(url)
                else super(MotherlessGroupIE, cls).suitable(url))


class Canalc2IE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:www\\.)?canalc2\\.tv/video/|archives-canalc2\\.u-strasbg\\.fr/video\\.asp\\?.*\\bidVideo=)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.canalc2'


class JWPlatformIE(LazyLoadExtractor):
    _VALID_URL = u'(?:https?://(?:content\\.jwplatform|cdn\\.jwplayer)\\.com/(?:(?:feed|player|thumb|preview|video)s|jw6|v2/media)/|jwplatform:)(?P<id>[a-zA-Z0-9]{8})'
    _module = 'youtube_dl.extractor.jwplatform'


class NPOBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.npo'


class NPOLiveIE(NPOBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?npo(?:start)?\\.nl/live(?:/(?P<id>[^/?#&]+))?'
    _module = 'youtube_dl.extractor.npo'


class SpankwireIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?P<url>spankwire\\.com/[^/]*/video(?P<id>[0-9]+)/?)'
    _module = 'youtube_dl.extractor.spankwire'


class JojIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    (?:\n                        joj:|\n                        https?://media\\.joj\\.sk/embed/\n                    )\n                    (?P<id>[^/?#^]+)\n                '
    _module = 'youtube_dl.extractor.joj'


class APAIE(LazyLoadExtractor):
    _VALID_URL = u'https?://[^/]+\\.apa\\.at/embed/(?P<id>[\\da-f]{8}-[\\da-f]{4}-[\\da-f]{4}-[\\da-f]{4}-[\\da-f]{12})'
    _module = 'youtube_dl.extractor.apa'


class NTVCoJpCUIE(LazyLoadExtractor):
    _VALID_URL = u'https?://cu\\.ntv\\.co\\.jp/(?!program)(?P<id>[^/?&#]+)'
    _module = 'youtube_dl.extractor.ntvcojp'


class RutubeBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.rutube'


class RutubePlaylistBaseIE(RutubeBaseIE):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.rutube'


class RutubePlaylistIE(RutubePlaylistBaseIE):
    _VALID_URL = u'https?://rutube\\.ru/(?:video|(?:play/)?embed)/[\\da-z]{32}/\\?.*?\\bpl_id=(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.rutube'

    @classmethod
    def suitable(cls, url):
        if not super(RutubePlaylistIE, cls).suitable(url):
            return False
        params = compat_parse_qs(compat_urllib_parse_urlparse(url).query)
        return params.get('pl_type', [None])[0] and int_or_none(params.get('pl_id', [None])[0])


class TechTVMITIE(LazyLoadExtractor):
    _VALID_URL = u'https?://techtv\\.mit\\.edu/(?:videos|embeds)/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.mit'


class XimalayaBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.ximalaya'


class XimalayaIE(XimalayaBaseIE):
    _VALID_URL = u'https?://(?:www\\.|m\\.)?ximalaya\\.com/(?P<uid>[0-9]+)/sound/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.ximalaya'


class EroProfileIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?eroprofile\\.com/m/videos/view/(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.eroprofile'


class HKETVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?hkedcity\\.net/etv/resource/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.hketv'


class TurnerBaseIE(AdobePassIE):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.turner'


class CNNIE(TurnerBaseIE):
    _VALID_URL = u'(?x)https?://(?:(?P<sub_domain>edition|www|money)\\.)?cnn\\.com/(?:video/(?:data/.+?|\\?)/)?videos?/\n        (?P<path>.+?/(?P<title>[^/]+?)(?:\\.(?:[a-z\\-]+)|(?=&)))'
    _module = 'youtube_dl.extractor.cnn'


class BildIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?bild\\.de/(?:[^/]+/)+(?P<display_id>[^/]+)-(?P<id>\\d+)(?:,auto=true)?\\.bild\\.html'
    _module = 'youtube_dl.extractor.bild'


class CrooksAndLiarsIE(LazyLoadExtractor):
    _VALID_URL = u'https?://embed\\.crooksandliars\\.com/(?:embed|v)/(?P<id>[A-Za-z0-9]+)'
    _module = 'youtube_dl.extractor.crooksandliars'


class MakerTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:www\\.)?maker\\.tv/(?:[^/]+/)*video|makerplayer\\.com/embed/maker)/(?P<id>[a-zA-Z0-9]{12})'
    _module = 'youtube_dl.extractor.makertv'


class SportBoxIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:news\\.sportbox|matchtv)\\.ru/vdl/player(?:/[^/]+/|\\?.*?\\bn?id=)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.sportbox'


class ViafreeIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:www\\.)?\n                        viafree\\.\n                        (?:\n                            (?:dk|no)/programmer|\n                            se/program\n                        )\n                        /(?:[^/]+/)+(?P<id>[^/?#&]+)\n                    '
    _module = 'youtube_dl.extractor.tvplay'

    @classmethod
    def suitable(cls, url):
        return False if TVPlayIE.suitable(url) else super(ViafreeIE, cls).suitable(url)


class QuicklineBaseIE(ZattooPlatformBaseIE):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.zattoo'


class QuicklineIE(QuicklineBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?mobiltv\\.quickline\\.com/watch/(?P<channel>[^/]+)/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.zattoo'


class AparatIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?aparat\\.com/(?:v/|video/video/embed/videohash/)(?P<id>[a-zA-Z0-9]+)'
    _module = 'youtube_dl.extractor.aparat'


class CCTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:[^/]+)\\.(?:cntv|cctv)\\.(?:com|cn)|(?:www\\.)?ncpa-classic\\.com)/(?:[^/]+/)*?(?P<id>[^/?#&]+?)(?:/index)?(?:\\.s?html|[?#&]|$)'
    _module = 'youtube_dl.extractor.cctv'


class VRVBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.vrv'


class VRVSeriesIE(VRVBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?vrv\\.co/series/(?P<id>[A-Z0-9]+)'
    _module = 'youtube_dl.extractor.vrv'


class AmericasTestKitchenIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?americastestkitchen\\.com/(?:episode|videos)/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.americastestkitchen'


class DigitekaIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n        https?://(?:www\\.)?(?:digiteka\\.net|ultimedia\\.com)/\n        (?:\n            deliver/\n            (?P<embed_type>\n                generic|\n                musique\n            )\n            (?:/[^/]+)*/\n            (?:\n                src|\n                article\n            )|\n            default/index/video\n            (?P<site_type>\n                generic|\n                music\n            )\n            /id\n        )/(?P<id>[\\d+a-z]+)'
    _module = 'youtube_dl.extractor.digiteka'


class GaskrankIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?gaskrank\\.tv/tv/(?P<categories>[^/]+)/(?P<id>[^/]+)\\.htm'
    _module = 'youtube_dl.extractor.gaskrank'


class MotorsportIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?motorsport\\.com/[^/?#]+/video/(?:[^/?#]+/)(?P<id>[^/]+)/?(?:$|[?#])'
    _module = 'youtube_dl.extractor.motorsport'


class SRGSSRPlayIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:www|play)\\.)?(?P<bu>srf|rts|rsi|rtr|swissinfo)\\.ch/play/(?:tv|radio)/[^/]+/(?P<type>video|audio)/[^?]+\\?id=(?P<id>[0-9a-f\\-]{36}|\\d+)'
    _module = 'youtube_dl.extractor.srgssr'


class BehindKinkIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?behindkink\\.com/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<id>[^/#?_]+)'
    _module = 'youtube_dl.extractor.behindkink'


class BBCCoUkPlaylistBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.bbc'


class BBCCoUkPlaylistIE(BBCCoUkPlaylistBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?bbc\\.co\\.uk/programmes/(?P<id>(?:[pbm][\\da-z]{7}|w[\\da-z]{7,14}))/(?:episodes|broadcasts|clips)'
    _module = 'youtube_dl.extractor.bbc'


class LeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.le\\.com/ptv/vplay|(?:sports\\.le|(?:www\\.)?lesports)\\.com/(?:match|video))/(?P<id>\\d+)\\.html'
    _module = 'youtube_dl.extractor.leeco'


class ABCOTVSIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:abc(?:7(?:news|ny|chicago)?|11|13|30)|6abc)\\.com(?:/[^/]+/(?P<display_id>[^/]+))?/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.abcotvs'


class DreiSatIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?3sat\\.de/mediathek/(?:(?:index|mediathek)\\.php)?\\?(?:(?:mode|display)=[^&]+&)*obj=(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.dreisat'


class FOXIE(AdobePassIE):
    _VALID_URL = u'https?://(?:www\\.)?fox\\.com/watch/(?P<id>[\\da-fA-F]+)'
    _module = 'youtube_dl.extractor.fox'


class CamdemyFolderIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?camdemy\\.com/folder/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.camdemy'


class RayWenderlichIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:\n                            videos\\.raywenderlich\\.com/courses|\n                            (?:www\\.)?raywenderlich\\.com\n                        )/\n                        (?P<course_id>[^/]+)/lessons/(?P<id>\\d+)\n                    '
    _module = 'youtube_dl.extractor.raywenderlich'


class GigaIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?giga\\.de/(?:[^/]+/)*(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.giga'


class KonserthusetPlayIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?:konserthusetplay|rspoplay)\\.se/\\?.*\\bm=(?P<id>[^&]+)'
    _module = 'youtube_dl.extractor.konserthusetplay'


class CrackleIE(LazyLoadExtractor):
    _VALID_URL = u'(?:crackle:|https?://(?:(?:www|m)\\.)?(?:sony)?crackle\\.com/(?:playlist/\\d+/|(?:[^/]+/)+))(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.crackle'


class BetIE(MTVServicesInfoExtractor):
    _VALID_URL = u'https?://(?:www\\.)?bet\\.com/(?:[^/]+/)+(?P<id>.+?)\\.html'
    _module = 'youtube_dl.extractor.bet'


class KeezMoviesIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?keezmovies\\.com/video/(?:(?P<display_id>[^/]+)-)?(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.keezmovies'


class ExtremeTubeIE(KeezMoviesIE):
    _VALID_URL = u'https?://(?:www\\.)?extremetube\\.com/(?:[^/]+/)?video/(?P<id>[^/#?&]+)'
    _module = 'youtube_dl.extractor.extremetube'


class Tube8IE(KeezMoviesIE):
    _VALID_URL = u'https?://(?:www\\.)?tube8\\.com/(?:[^/]+/)+(?P<display_id>[^/]+)/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.tube8'


class KarriereVideosIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?karrierevideos\\.at(?:/[^/]+)+/(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.karrierevideos'


class VidziIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?vidzi\\.(?:tv|cc|si|nu)/(?:embed-)?(?P<id>[0-9a-zA-Z]+)'
    _module = 'youtube_dl.extractor.vidzi'


class SnotrIE(LazyLoadExtractor):
    _VALID_URL = u'http?://(?:www\\.)?snotr\\.com/video/(?P<id>\\d+)/([\\w]+)'
    _module = 'youtube_dl.extractor.snotr'


class LemondeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:.+?\\.)?lemonde\\.fr/(?:[^/]+/)*(?P<id>[^/]+)\\.html'
    _module = 'youtube_dl.extractor.lemonde'


class PornComIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:[a-zA-Z]+\\.)?porn\\.com/videos/(?:(?P<display_id>[^/]+)-)?(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.porncom'


class IncIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?inc\\.com/(?:[^/]+/)+(?P<id>[^.]+).html'
    _module = 'youtube_dl.extractor.inc'


class NRKPlaylistBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.nrk'


class NRKPlaylistIE(NRKPlaylistBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?nrk\\.no/(?!video|skole)(?:[^/]+/)+(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.nrk'


class SkylineWebcamsIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?skylinewebcams\\.com/[^/]+/webcam/(?:[^/]+/)+(?P<id>[^/]+)\\.html'
    _module = 'youtube_dl.extractor.skylinewebcams'


class ZypeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://player\\.zype\\.com/embed/(?P<id>[\\da-fA-F]+)\\.js\\?.*?api_key=[^&]+'
    _module = 'youtube_dl.extractor.zype'


class EggheadCourseIE(LazyLoadExtractor):
    _VALID_URL = u'https://egghead\\.io/courses/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.egghead'


class AnvatoIE(LazyLoadExtractor):
    _VALID_URL = u'anvato:(?P<access_key_or_mcp>[^:]+):(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.anvato'


class FOX9IE(AnvatoIE):
    _VALID_URL = u'https?://(?:www\\.)?fox9\\.com/(?:[^/]+/)+(?P<id>\\d+)-story'
    _module = 'youtube_dl.extractor.fox9'


class C56IE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:www|player)\\.)?56\\.com/(?:.+?/)?(?:v_|(?:play_album.+-))(?P<textid>.+?)\\.(?:html|swf)'
    _module = 'youtube_dl.extractor.c56'


class VideomoreSeasonIE(LazyLoadExtractor):
    _VALID_URL = u'https?://videomore\\.ru/(?!embed)(?P<id>[^/]+/[^/?#&]+)(?:/*|[?#&].*?)$'
    _module = 'youtube_dl.extractor.videomore'

    @classmethod
    def suitable(cls, url):
        return (False if (VideomoreIE.suitable(url) or VideomoreVideoIE.suitable(url))
                else super(VideomoreSeasonIE, cls).suitable(url))


class AtresPlayerIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?atresplayer\\.com/television/[^/]+/[^/]+/[^/]+/(?P<id>.+?)_\\d+\\.html'
    _module = 'youtube_dl.extractor.atresplayer'


class AudiMediaIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?audi-mediacenter\\.com/(?:en|de)/audimediatv/(?:video/)?(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.audimedia'


class EyedoTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?eyedo\\.tv/[^/]+/(?:#!/)?Live/Detail/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.eyedotv'


class AolIE(LazyLoadExtractor):
    _VALID_URL = u'(?:aol-video:|https?://(?:www\\.)?aol\\.(?:com|ca|co\\.uk|de|jp)/video/(?:[^/]+/)*)(?P<id>[0-9a-f]+)'
    _module = 'youtube_dl.extractor.aol'


class ATVAtIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?atv\\.at/(?:[^/]+/){2}(?P<id>[dv]\\d+)'
    _module = 'youtube_dl.extractor.atvat'


class VODPlIE(OnetBaseIE):
    _VALID_URL = u'https?://vod\\.pl/(?:[^/]+/)+(?P<id>[0-9a-zA-Z]+)'
    _module = 'youtube_dl.extractor.vodpl'


class ABCIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?abc\\.net\\.au/news/(?:[^/]+/){1,2}(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.abc'


class LiveLeakIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:\\w+\\.)?liveleak\\.com/view\\?.*?\\b[it]=(?P<id>[\\w_]+)'
    _module = 'youtube_dl.extractor.liveleak'


class IndavideoEmbedIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:embed\\.)?indavideo\\.hu/player/video/|assets\\.indavideo\\.hu/swf/player\\.swf\\?.*\\b(?:v(?:ID|id))=)(?P<id>[\\da-f]+)'
    _module = 'youtube_dl.extractor.indavideo'


class ComedyCentralIE(MTVServicesInfoExtractor):
    _VALID_URL = u'(?x)https?://(?:www\\.)?cc\\.com/\n        (video-clips|episodes|cc-studios|video-collections|shows(?=/[^/]+/(?!full-episodes)))\n        /(?P<title>.*)'
    _module = 'youtube_dl.extractor.comedycentral'


class SkyNewsArabiaBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.skynewsarabia'


class SkyNewsArabiaArticleIE(SkyNewsArabiaBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?skynewsarabia\\.com/web/article/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.skynewsarabia'


class ParliamentLiveUKIE(LazyLoadExtractor):
    _VALID_URL = u'(?i)https?://(?:www\\.)?parliamentlive\\.tv/Event/Index/(?P<id>[\\da-f]{8}-[\\da-f]{4}-[\\da-f]{4}-[\\da-f]{4}-[\\da-f]{12})'
    _module = 'youtube_dl.extractor.parliamentliveuk'


class Tele13IE(LazyLoadExtractor):
    _VALID_URL = u'^https?://(?:www\\.)?t13\\.cl/videos(?:/[^/]+)+/(?P<id>[\\w-]+)'
    _module = 'youtube_dl.extractor.tele13'


class InstagramUserIE(InstagramPlaylistIE):
    _VALID_URL = u'https?://(?:www\\.)?instagram\\.com/(?P<id>[^/]{2,})/?(?:$|[?#])'
    _module = 'youtube_dl.extractor.instagram'


class MITIE(TechTVMITIE):
    _VALID_URL = u'https?://video\\.mit\\.edu/watch/(?P<title>[^/]+)'
    _module = 'youtube_dl.extractor.mit'


class SafariCourseIE(SafariBaseIE):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:\n                            (?:www\\.)?(?:safaribooksonline|learning\\.oreilly)\\.com/\n                            (?:\n                                library/view/[^/]+|\n                                api/v1/book|\n                                videos/[^/]+\n                            )|\n                            techbus\\.safaribooksonline\\.com\n                        )\n                        /(?P<id>[^/]+)\n                    '
    _module = 'youtube_dl.extractor.safari'

    @classmethod
    def suitable(cls, url):
        return (False if SafariIE.suitable(url) or SafariApiIE.suitable(url)
                else super(SafariCourseIE, cls).suitable(url))


class CamdemyIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?camdemy\\.com/media/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.camdemy'


class WDRIE(LazyLoadExtractor):
    _VALID_URL = u'https?://deviceids-medp\\.wdr\\.de/ondemand/\\d+/(?P<id>\\d+)\\.js'
    _module = 'youtube_dl.extractor.wdr'


class PlatziCourseIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:\n                            platzi\\.com/clases|           # es version\n                            courses\\.platzi\\.com/classes  # en version\n                        )/(?P<id>[^/?\\#&]+)\n                    '
    _module = 'youtube_dl.extractor.platzi'

    @classmethod
    def suitable(cls, url):
        return False if PlatziIE.suitable(url) else super(PlatziCourseIE, cls).suitable(url)


class BandcampWeeklyIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?bandcamp\\.com/?\\?(?:.*?&)?show=(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.bandcamp'


class NewstubeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?newstube\\.ru/media/(?P<id>.+)'
    _module = 'youtube_dl.extractor.newstube'


class SVTBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.svt'


class SVTPlayBaseIE(SVTBaseIE):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.svt'


class SVTSeriesIE(SVTPlayBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?svtplay\\.se/(?P<id>[^/?&#]+)'
    _module = 'youtube_dl.extractor.svt'

    @classmethod
    def suitable(cls, url):
        return False if SVTIE.suitable(url) or SVTPlayIE.suitable(url) else super(SVTSeriesIE, cls).suitable(url)


class BokeCCBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.bokecc'


class BokeCCIE(BokeCCBaseIE):
    _VALID_URL = u'https?://union\\.bokecc\\.com/playvideo\\.bo\\?(?P<query>.*)'
    _module = 'youtube_dl.extractor.bokecc'


class Zaq1IE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?zaq1\\.pl/video/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.zaq1'


class MoviezineIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?moviezine\\.se/video/(?P<id>[^?#]+)'
    _module = 'youtube_dl.extractor.moviezine'


class VideoWeedIE(NovaMovIE):
    _VALID_URL = u'(?x)\n                            http://\n                                (?:\n                                    (?:www\\.)?videoweed\\.(?:es|com)/(?:file|video|mobile/\\#/videos)/|\n                                    (?:(?:embed|www)\\.)videoweed\\.(?:es|com)/embed(?:\\.php|/)?\\?(?:.*?&)?\\bv=\n                                )\n                                (?P<id>[a-z\\d]{13})\n                            '
    _module = 'youtube_dl.extractor.novamov'


class TVNetIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:[^/]+)\\.tvnet\\.gov\\.vn/[^/]+/(?:\\d+/)?(?P<id>\\d+)(?:/|$)'
    _module = 'youtube_dl.extractor.tvnet'


class MusicPlayOnIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:.+?\\.)?musicplayon\\.com/play(?:-touch)?\\?(?:v|pl=\\d+&play)=(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.musicplayon'


class BandcampIE(LazyLoadExtractor):
    _VALID_URL = u'https?://[^/]+\\.bandcamp\\.com/track/(?P<title>[^/?#&]+)'
    _module = 'youtube_dl.extractor.bandcamp'


class BBCCoUkIPlayerPlaylistIE(BBCCoUkPlaylistBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?bbc\\.co\\.uk/iplayer/(?:episodes|group)/(?P<id>(?:[pbm][\\da-z]{7}|w[\\da-z]{7,14}))'
    _module = 'youtube_dl.extractor.bbc'


class Ku6IE(LazyLoadExtractor):
    _VALID_URL = u'https?://v\\.ku6\\.com/show/(?P<id>[a-zA-Z0-9\\-\\_]+)(?:\\.)*html'
    _module = 'youtube_dl.extractor.ku6'


class NFBIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?:nfb|onf)\\.ca/film/(?P<id>[\\da-z_-]+)'
    _module = 'youtube_dl.extractor.nfb'


class GameStarIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?game(?P<site>pro|star)\\.de/videos/.*,(?P<id>[0-9]+)\\.html'
    _module = 'youtube_dl.extractor.gamestar'


class ViceArticleIE(LazyLoadExtractor):
    _VALID_URL = u'https://www\\.vice\\.com/[^/]+/article/(?P<id>[^?#]+)'
    _module = 'youtube_dl.extractor.vice'


class FacebookIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                (?:\n                    https?://\n                        (?:[\\w-]+\\.)?(?:facebook\\.com|facebookcorewwwi\\.onion)/\n                        (?:[^#]*?\\#!/)?\n                        (?:\n                            (?:\n                                video/video\\.php|\n                                photo\\.php|\n                                video\\.php|\n                                video/embed|\n                                story\\.php\n                            )\\?(?:.*?)(?:v|video_id|story_fbid)=|\n                            [^/]+/videos/(?:[^/]+/)?|\n                            [^/]+/posts/|\n                            groups/[^/]+/permalink/\n                        )|\n                    facebook:\n                )\n                (?P<id>[0-9]+)\n                '
    _module = 'youtube_dl.extractor.facebook'


class CeskaTelevizePoradyIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?ceskatelevize\\.cz/porady/(?:[^/?#&]+/)*(?P<id>[^/#?]+)'
    _module = 'youtube_dl.extractor.ceskatelevize'


class CSpanIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?c-span\\.org/video/\\?(?P<id>[0-9a-f]+)'
    _module = 'youtube_dl.extractor.cspan'


class ManyVidsIE(LazyLoadExtractor):
    _VALID_URL = u'(?i)https?://(?:www\\.)?manyvids\\.com/video/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.manyvids'


class RTBFIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n        https?://(?:www\\.)?rtbf\\.be/\n        (?:\n            video/[^?]+\\?.*\\bid=|\n            ouftivi/(?:[^/]+/)*[^?]+\\?.*\\bvideoId=|\n            auvio/[^/]+\\?.*\\b(?P<live>l)?id=\n        )(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.rtbf'


class TinyPicIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:.+?\\.)?tinypic\\.com/player\\.php\\?v=(?P<id>[^&]+)&s=\\d+'
    _module = 'youtube_dl.extractor.tinypic'


class TVNowAnnualIE(TVNowListBaseIE):
    _VALID_URL = u'(?x)\n                    (?P<base_url>\n                        https?://\n                            (?:www\\.)?tvnow\\.(?:de|at|ch)/(?:shows|serien)/\n                            [^/?#&]+-(?P<show_id>\\d+)\n                    )\n                    /(?P<year>\\d{4})-(?P<month>\\d{2})'
    _module = 'youtube_dl.extractor.tvnow'

    @classmethod
    def suitable(cls, url):
        return (False if TVNowNewIE.suitable(url)
                else super(TVNowListBaseIE, cls).suitable(url))


class PandaTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?panda\\.tv/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.pandatv'


class PopcornTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://[^/]+\\.popcorntv\\.it/guarda/(?P<display_id>[^/]+)/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.popcorntv'


class PornFlipIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?pornflip\\.com/(?:v|embed)/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.pornflip'


class BeamProBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.beampro'


class BeamProVodIE(BeamProBaseIE):
    _VALID_URL = u'https?://(?:\\w+\\.)?(?:beam\\.pro|mixer\\.com)/[^/?#&]+\\?.*?\\bvod=(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.beampro'


class TeleQuebecBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.telequebec'


class TeleQuebecEmissionIE(TeleQuebecBaseIE):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:\n                            [^/]+\\.telequebec\\.tv/emissions/|\n                            (?:www\\.)?telequebec\\.tv/\n                        )\n                        (?P<id>[^?#&]+)\n                    '
    _module = 'youtube_dl.extractor.telequebec'


class VLivePlaylistIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:www|m)\\.)?vlive\\.tv/video/(?P<video_id>[0-9]+)/playlist/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.vlive'


class LivestreamOriginalIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)https?://original\\.livestream\\.com/\n        (?P<user>[^/\\?#]+)(?:/(?P<type>video|folder)\n        (?:(?:\\?.*?Id=|/)(?P<id>.*?)(&|$))?)?\n        '
    _module = 'youtube_dl.extractor.livestream'


class CloserToTruthIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?closertotruth\\.com/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.closertotruth'


class AdobeTVIE(AdobeTVBaseIE):
    _VALID_URL = u'https?://tv\\.adobe\\.com/(?:(?P<language>fr|de|es|jp)/)?watch/(?P<show_urlname>[^/]+)/(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.adobetv'


class RBMARadioIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?:rbmaradio|redbullradio)\\.com/shows/(?P<show_id>[^/]+)/episodes/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.rbmaradio'


class OraTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?:ora\\.tv|unsafespeech\\.com)/([^/]+/)*(?P<id>[^/\\?#]+)'
    _module = 'youtube_dl.extractor.ora'


class UKTVPlayIE(LazyLoadExtractor):
    _VALID_URL = u'https?://uktvplay\\.uktv\\.co\\.uk/.+?\\?.*?\\bvideo=(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.uktvplay'


class WDRPageIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\d?\\.)?(?:wdr\\d?|sportschau)\\.de/(?:mediathek/)?(?:[^/]+/)*(?P<display_id>[^/]+)\\.html|https?://(?:www\\.)wdrmaus.de/(?:[^/]+/){1,2}[^/?#]+\\.php5'
    _module = 'youtube_dl.extractor.wdr'


class PBSIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)https?://\n        (?:\n           # Direct video URL\n           (?:(?:video|www|player)\\.pbs\\.org|video\\.aptv\\.org|video\\.gpb\\.org|video\\.mpbonline\\.org|video\\.wnpt\\.org|video\\.wfsu\\.org|video\\.wsre\\.org|video\\.wtcitv\\.org|video\\.pba\\.org|video\\.alaskapublic\\.org|video\\.azpbs\\.org|portal\\.knme\\.org|video\\.vegaspbs\\.org|watch\\.aetn\\.org|video\\.ket\\.org|video\\.wkno\\.org|video\\.lpb\\.org|videos\\.oeta\\.tv|video\\.optv\\.org|watch\\.wsiu\\.org|video\\.keet\\.org|pbs\\.kixe\\.org|video\\.kpbs\\.org|video\\.kqed\\.org|vids\\.kvie\\.org|video\\.pbssocal\\.org|video\\.valleypbs\\.org|video\\.cptv\\.org|watch\\.knpb\\.org|video\\.soptv\\.org|video\\.rmpbs\\.org|video\\.kenw\\.org|video\\.kued\\.org|video\\.wyomingpbs\\.org|video\\.cpt12\\.org|video\\.kbyueleven\\.org|video\\.thirteen\\.org|video\\.wgbh\\.org|video\\.wgby\\.org|watch\\.njtvonline\\.org|watch\\.wliw\\.org|video\\.mpt\\.tv|watch\\.weta\\.org|video\\.whyy\\.org|video\\.wlvt\\.org|video\\.wvpt\\.net|video\\.whut\\.org|video\\.wedu\\.org|video\\.wgcu\\.org|video\\.wpbt2\\.org|video\\.wucftv\\.org|video\\.wuft\\.org|watch\\.wxel\\.org|video\\.wlrn\\.org|video\\.wusf\\.usf\\.edu|video\\.scetv\\.org|video\\.unctv\\.org|video\\.pbshawaii\\.org|video\\.idahoptv\\.org|video\\.ksps\\.org|watch\\.opb\\.org|watch\\.nwptv\\.org|video\\.will\\.illinois\\.edu|video\\.networkknowledge\\.tv|video\\.wttw\\.com|video\\.iptv\\.org|video\\.ninenet\\.org|video\\.wfwa\\.org|video\\.wfyi\\.org|video\\.mptv\\.org|video\\.wnin\\.org|video\\.wnit\\.org|video\\.wpt\\.org|video\\.wvut\\.org|video\\.weiu\\.net|video\\.wqpt\\.org|video\\.wycc\\.org|video\\.wipb\\.org|video\\.indianapublicmedia\\.org|watch\\.cetconnect\\.org|video\\.thinktv\\.org|video\\.wbgu\\.org|video\\.wgvu\\.org|video\\.netnebraska\\.org|video\\.pioneer\\.org|watch\\.sdpb\\.org|video\\.tpt\\.org|watch\\.ksmq\\.org|watch\\.kpts\\.org|watch\\.ktwu\\.org|watch\\.easttennesseepbs\\.org|video\\.wcte\\.tv|video\\.wljt\\.org|video\\.wosu\\.org|video\\.woub\\.org|video\\.wvpublic\\.org|video\\.wkyupbs\\.org|video\\.kera\\.org|video\\.mpbn\\.net|video\\.mountainlake\\.org|video\\.nhptv\\.org|video\\.vpt\\.org|video\\.witf\\.org|watch\\.wqed\\.org|video\\.wmht\\.org|video\\.deltabroadcasting\\.org|video\\.dptv\\.org|video\\.wcmu\\.org|video\\.wkar\\.org|wnmuvideo\\.nmu\\.edu|video\\.wdse\\.org|video\\.wgte\\.org|video\\.lptv\\.org|video\\.kmos\\.org|watch\\.montanapbs\\.org|video\\.krwg\\.org|video\\.kacvtv\\.org|video\\.kcostv\\.org|video\\.wcny\\.org|video\\.wned\\.org|watch\\.wpbstv\\.org|video\\.wskg\\.org|video\\.wxxi\\.org|video\\.wpsu\\.org|on-demand\\.wvia\\.org|video\\.wtvi\\.org|video\\.westernreservepublicmedia\\.org|video\\.ideastream\\.org|video\\.kcts9\\.org|video\\.basinpbs\\.org|video\\.houstonpbs\\.org|video\\.klrn\\.org|video\\.klru\\.tv|video\\.wtjx\\.org|video\\.ideastations\\.org|video\\.kbtc\\.org)/(?:(?:vir|port)alplayer|video)/(?P<id>[0-9]+)(?:[?/]|$) |\n           # Article with embedded player (or direct video)\n           (?:www\\.)?pbs\\.org/(?:[^/]+/){1,5}(?P<presumptive_id>[^/]+?)(?:\\.html)?/?(?:$|[?\\#]) |\n           # Player\n           (?:video|player)\\.pbs\\.org/(?:widget/)?partnerplayer/(?P<player_id>[^/]+)/\n        )\n    '
    _module = 'youtube_dl.extractor.pbs'


class ProSiebenSat1BaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.prosiebensat1'


class ProSiebenSat1IE(ProSiebenSat1BaseIE):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:www\\.)?\n                        (?:\n                            (?:beta\\.)?\n                            (?:\n                                prosieben(?:maxx)?|sixx|sat1(?:gold)?|kabeleins(?:doku)?|the-voice-of-germany|7tv|advopedia\n                            )\\.(?:de|at|ch)|\n                            ran\\.de|fem\\.com|advopedia\\.de|galileo\\.tv/video\n                        )\n                        /(?P<id>.+)\n                    '
    _module = 'youtube_dl.extractor.prosiebensat1'


class LimelightBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.limelight'


class LimelightChannelListIE(LimelightBaseIE):
    _VALID_URL = u'(?x)\n                        (?:\n                            limelight:channel_list:|\n                            https?://\n                                (?:\n                                    link\\.videoplatform\\.limelight\\.com/media/|\n                                    assets\\.delvenetworks\\.com/player/loader\\.swf\n                                )\n                                \\?.*?\\bchannelListId=\n                        )\n                        (?P<id>[a-z0-9]{32})\n                    '
    _module = 'youtube_dl.extractor.limelight'


class GooglePlusIE(LazyLoadExtractor):
    _VALID_URL = u'https?://plus\\.google\\.com/(?:[^/]+/)*?posts/(?P<id>\\w+)'
    _module = 'youtube_dl.extractor.googleplus'


class YandexDiskIE(LazyLoadExtractor):
    _VALID_URL = u'https?://yadi\\.sk/[di]/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.yandexdisk'


class BTVestlendingenIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?bt\\.no/spesial/vestlendingen/#!/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.vgtv'


class CiscoLiveBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.ciscolive'


class CiscoLiveSessionIE(CiscoLiveBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?ciscolive(?:\\.cisco)?\\.com/[^#]*#/session/(?P<id>[^/?&]+)'
    _module = 'youtube_dl.extractor.ciscolive'


class HelsinkiIE(LazyLoadExtractor):
    _VALID_URL = u'https?://video\\.helsinki\\.fi/Arkisto/flash\\.php\\?id=(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.helsinki'


class NBCIE(AdobePassIE):
    _VALID_URL = u'https?(?P<permalink>://(?:www\\.)?nbc\\.com/(?:classic-tv/)?[^/]+/video/[^/]+/(?P<id>n?\\d+))'
    _module = 'youtube_dl.extractor.nbc'


class EinthusanIE(LazyLoadExtractor):
    _VALID_URL = u'https?://einthusan\\.tv/movie/watch/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.einthusan'


class LifeNewsIE(LazyLoadExtractor):
    _VALID_URL = u'https?://life\\.ru/t/[^/]+/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.lifenews'


class RTL2YouBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.rtl2'


class RTL2YouIE(RTL2YouBaseIE):
    _VALID_URL = u'http?://you\\.rtl2\\.de/(?:video/\\d+/|youplayer/index\\.html\\?.*?\\bvid=)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.rtl2'


class PyvideoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?pyvideo\\.org/(?P<category>[^/]+)/(?P<id>[^/?#&.]+)'
    _module = 'youtube_dl.extractor.pyvideo'


class LyndaIE(LyndaBaseIE):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:www\\.)?(?:lynda\\.com|educourse\\.ga)/\n                        (?:\n                            (?:[^/]+/){2,3}(?P<course_id>\\d+)|\n                            player/embed\n                        )/\n                        (?P<id>\\d+)\n                    '
    _module = 'youtube_dl.extractor.lynda'


class HearThisAtIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?hearthis\\.at/(?P<artist>[^/]+)/(?P<title>[A-Za-z0-9\\-]+)/?$'
    _module = 'youtube_dl.extractor.hearthisat'


class GPUTechConfIE(LazyLoadExtractor):
    _VALID_URL = u'https?://on-demand\\.gputechconf\\.com/gtc/2015/video/S(?P<id>\\d+)\\.html'
    _module = 'youtube_dl.extractor.gputechconf'


class NBAIE(TurnerBaseIE):
    _VALID_URL = u'https?://(?:watch\\.|www\\.)?nba\\.com/(?P<path>(?:[^/]+/)+(?P<id>[^?]*?))/?(?:/index\\.html)?(?:\\?.*)?$'
    _module = 'youtube_dl.extractor.nba'


class TVAIE(LazyLoadExtractor):
    _VALID_URL = u'https?://videos\\.tva\\.ca/details/_(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.tva'


class ZapiksIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?zapiks\\.(?:fr|com)/(?:(?:[a-z]{2}/)?(?P<display_id>.+?)\\.html|index\\.php\\?.*\\bmedia_id=(?P<id>\\d+))'
    _module = 'youtube_dl.extractor.zapiks'


class ZDFChannelIE(ZDFBaseIE):
    _VALID_URL = u'https?://www\\.zdf\\.de/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.zdf'

    @classmethod
    def suitable(cls, url):
        return False if ZDFIE.suitable(url) else super(ZDFChannelIE, cls).suitable(url)


class PornTubeIE(FourTubeBaseIE):
    _VALID_URL = u'https?://(?:(?P<kind>www|m)\\.)?porntube\\.com/(?:videos/(?P<display_id>[^/]+)_|embed/)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.fourtube'


class TVNowNewIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    (?P<base_url>https?://\n                        (?:www\\.)?tvnow\\.(?:de|at|ch)/\n                        (?:shows|serien))/\n                        (?P<show>[^/]+)-\\d+/\n                        [^/]+/\n                        episode-\\d+-(?P<episode>[^/?$&]+)-(?P<id>\\d+)\n                    '
    _module = 'youtube_dl.extractor.tvnow'


class RUHDIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?ruhd\\.ru/play\\.php\\?vid=(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.ruhd'


class NBCOlympicsIE(LazyLoadExtractor):
    _VALID_URL = u'https?://www\\.nbcolympics\\.com/video/(?P<id>[a-z-]+)'
    _module = 'youtube_dl.extractor.nbc'


class TwitchChapterIE(TwitchItemBaseIE):
    _VALID_URL = u'https?://(?:(?:www|go|m)\\.)?twitch\\.tv/[^/]+/c/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.twitch'


class AMPIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.amp'


class BleacherReportCMSIE(AMPIE):
    _VALID_URL = u'https?://(?:www\\.)?bleacherreport\\.com/video_embed\\?id=(?P<id>[0-9a-f-]{36})'
    _module = 'youtube_dl.extractor.bleacherreport'


class NRKTVSerieBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.nrk'


class NRKTVSeriesIE(NRKTVSerieBaseIE):
    _VALID_URL = u'https?://(?:tv|radio)\\.nrk(?:super)?\\.no/serie/(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.nrk'

    @classmethod
    def suitable(cls, url):
        return (
            False if any(ie.suitable(url)
                         for ie in (NRKTVIE, NRKTVEpisodeIE, NRKTVSeasonIE))
            else super(NRKTVSeriesIE, cls).suitable(url))


class DouyuShowIE(LazyLoadExtractor):
    _VALID_URL = u'https?://v(?:mobile)?\\.douyu\\.com/show/(?P<id>[0-9a-zA-Z]+)'
    _module = 'youtube_dl.extractor.douyutv'


class TwitchUploadsIE(TwitchVideosBaseIE):
    _VALID_URL = u'https?://(?:(?:www|go|m)\\.)?twitch\\.tv/(?P<id>[^/]+)/videos/uploads'
    _module = 'youtube_dl.extractor.twitch'


class NosVideoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?nosvideo\\.com/(?:embed/|\\?v=)(?P<id>[A-Za-z0-9]{12})/?'
    _module = 'youtube_dl.extractor.nosvideo'


class IzleseneIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n        https?://(?:(?:www|m)\\.)?izlesene\\.com/\n        (?:video|embedplayer)/(?:[^/]+/)?(?P<id>[0-9]+)\n        '
    _module = 'youtube_dl.extractor.izlesene'


class VideomoreVideoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://videomore\\.ru/(?:(?:[^/]+/){2})?(?P<id>[^/?#&]+)(?:/*|[?#&].*?)$'
    _module = 'youtube_dl.extractor.videomore'

    @classmethod
    def suitable(cls, url):
        return False if VideomoreIE.suitable(url) else super(VideomoreVideoIE, cls).suitable(url)


class SWRMediathekIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?swrmediathek\\.de/(?:content/)?player\\.htm\\?show=(?P<id>[\\da-f]{8}-[\\da-f]{4}-[\\da-f]{4}-[\\da-f]{4}-[\\da-f]{12})'
    _module = 'youtube_dl.extractor.swrmediathek'


class CanvasEenIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?P<site_id>canvas|een)\\.be/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.canvas'


class FacebookPluginsVideoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:[\\w-]+\\.)?facebook\\.com/plugins/video\\.php\\?.*?\\bhref=(?P<id>https.+)'
    _module = 'youtube_dl.extractor.facebook'


class AlphaPornoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?alphaporno\\.com/videos/(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.alphaporno'


class FiveTVIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    http://\n                        (?:www\\.)?5-tv\\.ru/\n                        (?:\n                            (?:[^/]+/)+(?P<id>\\d+)|\n                            (?P<path>[^/?#]+)(?:[/?#])?\n                        )\n                    '
    _module = 'youtube_dl.extractor.fivetv'


class YouNowLiveIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?younow\\.com/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.younow'

    @classmethod
    def suitable(cls, url):
        return (False
                if YouNowChannelIE.suitable(url) or YouNowMomentIE.suitable(url)
                else super(YouNowLiveIE, cls).suitable(url))


class LEGOIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?lego\\.com/(?P<locale>[^/]+)/(?:[^/]+/)*videos/(?:[^/]+/)*[^/?#]+-(?P<id>[0-9a-f]+)'
    _module = 'youtube_dl.extractor.lego'


class SoundgasmProfileIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?soundgasm\\.net/u/(?P<id>[^/]+)/?(?:\\#.*)?$'
    _module = 'youtube_dl.extractor.soundgasm'


class RENTVIE(LazyLoadExtractor):
    _VALID_URL = u'(?:rentv:|https?://(?:www\\.)?ren\\.tv/(?:player|video/epizod)/)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.rentv'


class GoshgayIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?goshgay\\.com/video(?P<id>\\d+?)($|/)'
    _module = 'youtube_dl.extractor.goshgay'


class BleacherReportIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?bleacherreport\\.com/articles/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.bleacherreport'


class BYUtvIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?byutv\\.org/(?:watch|player)/(?!event/)(?P<id>[0-9a-f-]+)(?:/(?P<display_id>[^/?#&]+))?'
    _module = 'youtube_dl.extractor.byutv'


class MicrosoftVirtualAcademyIE(MicrosoftVirtualAcademyBaseIE):
    _VALID_URL = u'(?:mva:|https?://(?:mva\\.microsoft|(?:www\\.)?microsoftvirtualacademy)\\.com/[^/]+/training-courses/[^/?#&]+-)(?P<course_id>\\d+)(?::|\\?l=)(?P<id>[\\da-zA-Z]+_\\d+)'
    _module = 'youtube_dl.extractor.microsoftvirtualacademy'


class LCIIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?lci\\.fr/[^/]+/[\\w-]+-(?P<id>\\d+)\\.html'
    _module = 'youtube_dl.extractor.lci'


class NuvidIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www|m)\\.nuvid\\.com/video/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.nuvid'


class NRKBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.nrk'


class NRKIE(NRKBaseIE):
    _VALID_URL = u'(?x)\n                        (?:\n                            nrk:|\n                            https?://\n                                (?:\n                                    (?:www\\.)?nrk\\.no/video/PS\\*|\n                                    v8[-.]psapi\\.nrk\\.no/mediaelement/\n                                )\n                            )\n                            (?P<id>[^?#&]+)\n                        '
    _module = 'youtube_dl.extractor.nrk'


class PornHubBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.pornhub'


class PornHubPlaylistBaseIE(PornHubBaseIE):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.pornhub'


class PornHubPlaylistIE(PornHubPlaylistBaseIE):
    _VALID_URL = u'https?://(?:[^/]+\\.)?(?P<host>pornhub\\.(?:com|net))/playlist/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.pornhub'


class Ro220IE(LazyLoadExtractor):
    _VALID_URL = u'(?x)(?:https?://)?(?:www\\.)?220\\.ro/(?P<category>[^/]+)/(?P<shorttitle>[^/]+)/(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.ro220'


class VoiceRepublicIE(LazyLoadExtractor):
    _VALID_URL = u'https?://voicerepublic\\.com/(?:talks|embed)/(?P<id>[0-9a-z-]+)'
    _module = 'youtube_dl.extractor.voicerepublic'


class ArteTVBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.arte'


class ArteTVPlus7IE(ArteTVBaseIE):
    _VALID_URL = u'https?://(?:(?:www|sites)\\.)?arte\\.tv/(?:[^/]+/)?(?P<lang>fr|de|en|es)/(?:videos/)?(?:[^/]+/)*(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.arte'

    @classmethod
    def suitable(cls, url):
        return False if ArteTVPlaylistIE.suitable(url) else super(ArteTVPlus7IE, cls).suitable(url)


class ArteTVConcertIE(ArteTVPlus7IE):
    _VALID_URL = u'https?://concert\\.arte\\.tv/(?P<lang>fr|de|en|es)/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.arte'

    @classmethod
    def suitable(cls, url):
        return False if ArteTVPlaylistIE.suitable(url) else super(ArteTVPlus7IE, cls).suitable(url)


class ArteTVCreativeIE(ArteTVPlus7IE):
    _VALID_URL = u'https?://creative\\.arte\\.tv/(?P<lang>fr|de|en|es)/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.arte'

    @classmethod
    def suitable(cls, url):
        return False if ArteTVPlaylistIE.suitable(url) else super(ArteTVPlus7IE, cls).suitable(url)


class TheOperaPlatformIE(ArteTVPlus7IE):
    _VALID_URL = u'https?://(?:www\\.)?theoperaplatform\\.eu/(?P<lang>fr|de|en|es)/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.arte'

    @classmethod
    def suitable(cls, url):
        return False if ArteTVPlaylistIE.suitable(url) else super(ArteTVPlus7IE, cls).suitable(url)


class ArteTVEmbedIE(ArteTVPlus7IE):
    _VALID_URL = u'(?x)\n        http://www\\.arte\\.tv\n        /(?:playerv2/embed|arte_vp/index)\\.php\\?json_url=\n        (?P<json_url>\n            http://arte\\.tv/papi/tvguide/videos/stream/player/\n            (?P<lang>[^/]+)/(?P<id>[^/]+)[^&]*\n        )\n    '
    _module = 'youtube_dl.extractor.arte'

    @classmethod
    def suitable(cls, url):
        return False if ArteTVPlaylistIE.suitable(url) else super(ArteTVPlus7IE, cls).suitable(url)


class ArteTVDDCIE(ArteTVPlus7IE):
    _VALID_URL = u'https?://ddc\\.arte\\.tv/(?P<lang>emission|folge)/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.arte'

    @classmethod
    def suitable(cls, url):
        return False if ArteTVPlaylistIE.suitable(url) else super(ArteTVPlus7IE, cls).suitable(url)


class AudiomackIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?audiomack\\.com/song/(?P<id>[\\w/-]+)'
    _module = 'youtube_dl.extractor.audiomack'


class BeegIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?beeg\\.(?:com|porn(?:/video)?)/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.beeg'


class YoutubeChannelIE(YoutubePlaylistBaseInfoExtractor):
    _VALID_URL = u'https?://(?:youtu\\.be|(?:\\w+\\.)?youtube(?:-nocookie)?\\.com|(?:www\\.)?invidio\\.us)/channel/(?P<id>[0-9A-Za-z_-]+)'
    _module = 'youtube_dl.extractor.youtube'

    @classmethod
    def suitable(cls, url):
        return (False if YoutubePlaylistsIE.suitable(url) or YoutubeLiveIE.suitable(url)
                else super(YoutubeChannelIE, cls).suitable(url))


class TeleQuebecIE(TeleQuebecBaseIE):
    _VALID_URL = u'https?://zonevideo\\.telequebec\\.tv/media/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.telequebec'


class YouJizzIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:\\w+\\.)?youjizz\\.com/videos/(?:[^/#?]*-(?P<id>\\d+)\\.html|embed/(?P<embed_id>\\d+))'
    _module = 'youtube_dl.extractor.youjizz'


class NRKSkoleIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?nrk\\.no/skole/?\\?.*\\bmediaId=(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.nrk'


class TuneInTopicIE(TuneInBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?tunein\\.com/(?:topic/.*?TopicId=|embed/player/t)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.tunein'


class ABCIViewIE(LazyLoadExtractor):
    _VALID_URL = u'https?://iview\\.abc\\.net\\.au/(?:[^/]+/)*video/(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.abc'


class SixPlayIE(LazyLoadExtractor):
    _VALID_URL = u'(?:6play:|https?://(?:www\\.)?(?P<domain>6play\\.fr|rtlplay\\.be|play\\.rtl\\.hr)/.+?-c_)(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.sixplay'


class VimeoChannelIE(VimeoBaseInfoExtractor):
    _VALID_URL = u'https://vimeo\\.com/channels/(?P<id>[^/?#]+)/?(?:$|[?#])'
    _module = 'youtube_dl.extractor.vimeo'


class FreespeechIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?freespeech\\.org/stories/(?P<id>.+)'
    _module = 'youtube_dl.extractor.freespeech'


class FiveMinIE(LazyLoadExtractor):
    _VALID_URL = u'(?:5min:|https?://(?:[^/]*?5min\\.com/|delivery\\.vidible\\.tv/aol)(?:(?:Scripts/PlayerSeed\\.js|playerseed/?)?\\?.*?playList=)?)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.fivemin'


class FranceTVSiteIE(FranceTVBaseInfoExtractor):
    _VALID_URL = u'https?://(?:(?:www\\.)?france\\.tv|mobile\\.france\\.tv)/(?:[^/]+/)*(?P<id>[^/]+)\\.html'
    _module = 'youtube_dl.extractor.francetv'


class ZingMp3BaseInfoExtractor(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.zingmp3'


class ZingMp3IE(ZingMp3BaseInfoExtractor):
    _VALID_URL = u'https?://mp3\\.zing\\.vn/(?:bai-hat|album|playlist|video-clip)/[^/]+/(?P<id>\\w+)\\.html'
    _module = 'youtube_dl.extractor.zingmp3'


class MTVVideoIE(MTVServicesInfoExtractor):
    _VALID_URL = u'(?x)^https?://\n        (?:(?:www\\.)?mtv\\.com/videos/.+?/(?P<videoid>[0-9]+)/[^/]+$|\n           m\\.mtv\\.com/videos/video\\.rbml\\?.*?id=(?P<mgid>[^&]+))'
    _module = 'youtube_dl.extractor.mtv'


class VestiIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:.+?\\.)?vesti\\.ru/(?P<id>.+)'
    _module = 'youtube_dl.extractor.vesti'


class IqiyiIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:[^.]+\\.)?iqiyi\\.com|www\\.pps\\.tv)/.+\\.html'
    _module = 'youtube_dl.extractor.iqiyi'


class VoxMediaIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?:(?:theverge|vox|sbnation|eater|polygon|curbed|racked)\\.com|recode\\.net)/(?:[^/]+/)*(?P<id>[^/?]+)'
    _module = 'youtube_dl.extractor.voxmedia'


class AsianCrushPlaylistIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?asiancrush\\.com/series/0+(?P<id>\\d+)s\\b'
    _module = 'youtube_dl.extractor.asiancrush'


class HowStuffWorksIE(LazyLoadExtractor):
    _VALID_URL = u'https?://[\\da-z-]+\\.(?:howstuffworks|stuff(?:(?:youshould|theydontwantyouto)know|toblowyourmind|momnevertoldyou)|(?:brain|car)stuffshow|fwthinking|geniusstuff)\\.com/(?:[^/]+/)*(?:\\d+-)?(?P<id>.+?)-video\\.htm'
    _module = 'youtube_dl.extractor.howstuffworks'


class NhkVodIE(LazyLoadExtractor):
    _VALID_URL = u'https?://www3\\.nhk\\.or\\.jp/nhkworld/(?P<lang>[a-z]{2})/ondemand/(?P<type>video|audio)/(?P<id>\\d{7}|[a-z]+-\\d{8}-\\d+)'
    _module = 'youtube_dl.extractor.nhk'


class NetEaseMusicBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.neteasemusic'


class NetEaseMusicSingerIE(NetEaseMusicBaseIE):
    _VALID_URL = u'https?://music\\.163\\.com/(#/)?artist\\?id=(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.neteasemusic'


class NZZIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?nzz\\.ch/(?:[^/]+/)*[^/?#]+-ld\\.(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.nzz'


class FC2EmbedIE(LazyLoadExtractor):
    _VALID_URL = u'https?://video\\.fc2\\.com/flv2\\.swf\\?(?P<query>.+)'
    _module = 'youtube_dl.extractor.fc2'


class XNXXIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:video|www)\\.xnxx\\.com/video-?(?P<id>[0-9a-z]+)/'
    _module = 'youtube_dl.extractor.xnxx'


class WebcasterFeedIE(LazyLoadExtractor):
    _VALID_URL = u'https?://bl\\.webcaster\\.pro/feed/start/free_(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.webcaster'


class YoutubeLiveIE(YoutubeBaseInfoExtractor):
    _VALID_URL = u'(?P<base_url>https?://(?:\\w+\\.)?youtube\\.com/(?:(?:user|channel|c)/)?(?P<id>[^/]+))/live'
    _module = 'youtube_dl.extractor.youtube'


class MDRIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?:mdr|kika)\\.de/(?:.*)/[a-z-]+-?(?P<id>\\d+)(?:_.+?)?\\.html'
    _module = 'youtube_dl.extractor.mdr'


class CNBCVideoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?cnbc\\.com/video/(?:[^/]+/)+(?P<id>[^./?#&]+)'
    _module = 'youtube_dl.extractor.cnbc'


class CDAIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:www\\.)?cda\\.pl/video|ebd\\.cda\\.pl/[0-9]+x[0-9]+)/(?P<id>[0-9a-z]+)'
    _module = 'youtube_dl.extractor.cda'


class WSJIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                        (?:\n                            https?://video-api\\.wsj\\.com/api-video/player/iframe\\.html\\?.*?\\bguid=|\n                            https?://(?:www\\.)?(?:wsj|barrons)\\.com/video/(?:[^/]+/)+|\n                            wsj:\n                        )\n                        (?P<id>[a-fA-F0-9-]{36})\n                    '
    _module = 'youtube_dl.extractor.wsj'


class PladformIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:\n                            (?:\n                                out\\.pladform\\.ru/player|\n                                static\\.pladform\\.ru/player\\.swf\n                            )\n                            \\?.*\\bvideoid=|\n                            video\\.pladform\\.ru/catalog/video/videoid/\n                        )\n                        (?P<id>\\d+)\n                    '
    _module = 'youtube_dl.extractor.pladform'


class VierIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:www\\.)?(?P<site>vier|vijf)\\.be/\n                        (?:\n                            (?:\n                                [^/]+/videos|\n                                video(?:/[^/]+)*\n                            )/\n                            (?P<display_id>[^/]+)(?:/(?P<id>\\d+))?|\n                            (?:\n                                video/v3/embed|\n                                embed/video/public\n                            )/(?P<embed_id>\\d+)\n                        )\n                    '
    _module = 'youtube_dl.extractor.vier'


class VimeoIE(VimeoBaseInfoExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:\n                            (?:\n                                www|\n                                (?P<player>player)\n                            )\n                            \\.\n                        )?\n                        vimeo(?P<pro>pro)?\\.com/\n                        (?!(?:channels|album)/[^/?#]+/?(?:$|[?#])|[^/]+/review/|ondemand/)\n                        (?:.*?/)?\n                        (?:\n                            (?:\n                                play_redirect_hls|\n                                moogaloop\\.swf)\\?clip_id=\n                            )?\n                        (?:videos?/)?\n                        (?P<id>[0-9]+)\n                        (?:/[\\da-f]+)?\n                        /?(?:[?&].*)?(?:[#].*)?$\n                    '
    _module = 'youtube_dl.extractor.vimeo'


class BambuserChannelIE(LazyLoadExtractor):
    _VALID_URL = u'https?://bambuser\\.com/channel/(?P<user>.*?)(?:/|#|\\?|$)'
    _module = 'youtube_dl.extractor.bambuser'


class PornotubeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:\\w+\\.)?pornotube\\.com/(?:[^?#]*?)/video/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.pornotube'


class FunkBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.funk'


class FunkChannelIE(FunkBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?funk\\.net/channel/(?P<id>[^/]+)/(?P<alias>[^/?#&]+)'
    _module = 'youtube_dl.extractor.funk'


class HGTVComShowIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?hgtv\\.com/shows/[^/]+/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.hgtv'


class RoosterTeethIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:.+?\\.)?roosterteeth\\.com/episode/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.roosterteeth'


class TelegraafIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?telegraaf\\.nl/tv/(?:[^/]+/)+(?P<id>\\d+)/[^/]+\\.html'
    _module = 'youtube_dl.extractor.telegraaf'


class DRTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?dr\\.dk/(?:tv/se|nyheder|radio/ondemand)/(?:[^/]+/)*(?P<id>[\\da-z-]+)(?:[/#?]|$)'
    _module = 'youtube_dl.extractor.drtv'


class YoutubeTruncatedIDIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?youtube\\.com/watch\\?v=(?P<id>[0-9A-Za-z_-]{1,10})$'
    _module = 'youtube_dl.extractor.youtube'


class CNNArticleIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:edition|www)\\.)?cnn\\.com/(?!videos?/)'
    _module = 'youtube_dl.extractor.cnn'


class JpopsukiIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?jpopsuki\\.tv/(?:category/)?video/[^/]+/(?P<id>\\S+)'
    _module = 'youtube_dl.extractor.jpopsukitv'


class UstreamChannelIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?ustream\\.tv/channel/(?P<slug>.+)'
    _module = 'youtube_dl.extractor.ustream'


class DBTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?dbtv\\.no/(?:[^/]+/)?(?P<id>[0-9]+)(?:#(?P<display_id>.+))?'
    _module = 'youtube_dl.extractor.dbtv'


class MTV81IE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?mtv81\\.com/videos/(?P<id>[^/?#.]+)'
    _module = 'youtube_dl.extractor.mtv'


class ToypicsUserIE(LazyLoadExtractor):
    _VALID_URL = u'https?://videos\\.toypics\\.net/(?!view)(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.toypics'


class TwentyMinutenIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:www\\.)?20min\\.ch/\n                        (?:\n                            videotv/*\\?.*?\\bvid=|\n                            videoplayer/videoplayer\\.html\\?.*?\\bvideoId@\n                        )\n                        (?P<id>\\d+)\n                    '
    _module = 'youtube_dl.extractor.twentymin'


class PromptFileIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?promptfile\\.com/l/(?P<id>[0-9A-Z\\-]+)'
    _module = 'youtube_dl.extractor.promptfile'


class AliExpressLiveIE(LazyLoadExtractor):
    _VALID_URL = u'https?://live\\.aliexpress\\.com/live/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.aliexpress'


class ThisAmericanLifeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?thisamericanlife\\.org/(?:radio-archives/episode/|play_full\\.php\\?play=)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.thisamericanlife'


class BFIPlayerIE(LazyLoadExtractor):
    _VALID_URL = u'https?://player\\.bfi\\.org\\.uk/[^/]+/film/watch-(?P<id>[\\w-]+)-online'
    _module = 'youtube_dl.extractor.bfi'


class HiDiveIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?hidive\\.com/stream/(?P<title>[^/]+)/(?P<key>[^/?#&]+)'
    _module = 'youtube_dl.extractor.hidive'


class RtmpIE(LazyLoadExtractor):
    _VALID_URL = u'(?i)rtmp[est]?://.+'
    _module = 'youtube_dl.extractor.commonprotocols'


class TubiTvIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?tubitv\\.com/(?:video|movies|tv-shows)/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.tubitv'


class VikiChannelIE(VikiBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?viki\\.(?:com|net|mx|jp|fr)/(?:tv|news|movies|artists)/(?P<id>[0-9]+c)'
    _module = 'youtube_dl.extractor.viki'


class AirMozillaIE(LazyLoadExtractor):
    _VALID_URL = u'https?://air\\.mozilla\\.org/(?P<id>[0-9a-z-]+)/?'
    _module = 'youtube_dl.extractor.airmozilla'


class DPlayItIE(LazyLoadExtractor):
    _VALID_URL = u'https?://it\\.dplay\\.com/[^/]+/[^/]+/(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.dplay'


class XHamsterEmbedIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:.+?\\.)?xhamster\\.com/xembed\\.php\\?video=(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.xhamster'


class SportDeutschlandIE(LazyLoadExtractor):
    _VALID_URL = u'https?://sportdeutschland\\.tv/(?P<sport>[^/?#]+)/(?P<id>[^?#/]+)(?:$|[?#])'
    _module = 'youtube_dl.extractor.sportdeutschland'


class WorldStarHipHopIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www|m)\\.worldstar(?:candy|hiphop)\\.com/(?:videos|android)/video\\.php\\?.*?\\bv=(?P<id>[^&]+)'
    _module = 'youtube_dl.extractor.worldstarhiphop'


class R7ArticleIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:[a-zA-Z]+)\\.r7\\.com/(?:[^/]+/)+[^/?#&]+-(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.r7'

    @classmethod
    def suitable(cls, url):
        return False if R7IE.suitable(url) else super(R7ArticleIE, cls).suitable(url)


class NozIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?noz\\.de/video/(?P<id>[0-9]+)/'
    _module = 'youtube_dl.extractor.noz'


class BellMediaIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)https?://(?:www\\.)?\n        (?P<domain>\n            (?:\n                ctv|\n                tsn|\n                bnn(?:bloomberg)?|\n                thecomedynetwork|\n                discovery|\n                discoveryvelocity|\n                sciencechannel|\n                investigationdiscovery|\n                animalplanet|\n                bravo|\n                mtv|\n                space|\n                etalk\n            )\\.ca|\n            much\\.com\n        )/.*?(?:\\bvid(?:eoid)?=|-vid|~|%7E|/(?:episode)?)(?P<id>[0-9]{6,})'
    _module = 'youtube_dl.extractor.bellmedia'


class RutubeMovieIE(RutubePlaylistBaseIE):
    _VALID_URL = u'https?://rutube\\.ru/metainfo/tv/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.rutube'


class DaisukiMottoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://motto\\.daisuki\\.net/framewatch/embed/[^/]+/(?P<id>[0-9a-zA-Z]{3})'
    _module = 'youtube_dl.extractor.daisuki'


class MovieFapIE(TNAFlixNetworkBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?moviefap\\.com/videos/(?P<id>[0-9a-f]+)/(?P<display_id>[^/]+)\\.html'
    _module = 'youtube_dl.extractor.tnaflix'


class CBCIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?cbc\\.ca/(?!player/)(?:[^/]+/)+(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.cbc'

    @classmethod
    def suitable(cls, url):
        return False if CBCPlayerIE.suitable(url) else super(CBCIE, cls).suitable(url)


class XiamiBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.xiami'


class XiamiPlaylistBaseIE(XiamiBaseIE):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.xiami'


class XiamiArtistIE(XiamiPlaylistBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?xiami\\.com/artist/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.xiami'


class WebOfStoriesPlaylistIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?webofstories\\.com/playAll/(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.webofstories'


class UMGDeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?universal-music\\.de/[^/]+/videos/[^/?#]+-(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.umg'


class QQMusicSingerIE(QQPlaylistBaseIE):
    _VALID_URL = u'https?://y\\.qq\\.com/n/yqq/singer/(?P<id>[0-9A-Za-z]+)\\.html'
    _module = 'youtube_dl.extractor.qqmusic'


class ParamountNetworkIE(MTVServicesInfoExtractor):
    _VALID_URL = u'https?://(?:www\\.)?paramountnetwork\\.com/[^/]+/[\\da-z]{6}(?:[/?#&]|$)'
    _module = 'youtube_dl.extractor.spike'


class RedBullTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?redbull(?:\\.tv|\\.com/(?:[^/]+/)?tv)/video/(?P<id>AP-\\w+)'
    _module = 'youtube_dl.extractor.redbulltv'


class ESPNIE(OnceIE):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:\n                            (?:\n                                (?:\n                                    (?:(?:\\w+\\.)+)?espn\\.go|\n                                    (?:www\\.)?espn\n                                )\\.com/\n                                (?:\n                                    (?:\n                                        video/(?:clip|iframe/twitter)|\n                                        watch/player\n                                    )\n                                    (?:\n                                        .*?\\?.*?\\bid=|\n                                        /_/id/\n                                    )|\n                                    [^/]+/video/\n                                )\n                            )|\n                            (?:www\\.)espnfc\\.(?:com|us)/(?:video/)?[^/]+/\\d+/video/\n                        )\n                        (?P<id>\\d+)\n                    '
    _module = 'youtube_dl.extractor.espn'


class DiscoveryGoPlaylistIE(DiscoveryGoBaseIE):
    _VALID_URL = u'(?x)https?://(?:www\\.)?(?:\n            discovery|\n            investigationdiscovery|\n            discoverylife|\n            animalplanet|\n            ahctv|\n            destinationamerica|\n            sciencechannel|\n            tlc|\n            velocitychannel\n        )go\\.com/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.discoverygo'

    @classmethod
    def suitable(cls, url):
        return False if DiscoveryGoIE.suitable(url) else super(
            DiscoveryGoPlaylistIE, cls).suitable(url)


class AppleConnectIE(LazyLoadExtractor):
    _VALID_URL = u'https?://itunes\\.apple\\.com/\\w{0,2}/?post/idsa\\.(?P<id>[\\w-]+)'
    _module = 'youtube_dl.extractor.appleconnect'


class CarambaTVPageIE(LazyLoadExtractor):
    _VALID_URL = u'https?://carambatv\\.ru/(?:[^/]+/)+(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.carambatv'


class HotNewHipHopIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?hotnewhiphop\\.com/.*\\.(?P<id>.*)\\.html'
    _module = 'youtube_dl.extractor.hotnewhiphop'


class GlattvisionTVIE(ZattooIE):
    _VALID_URL = u'https?://(?:www\\.)?iptv\\.glattvision\\.ch/watch/(?P<channel>[^/]+?)/(?P<id>[0-9]+)[^/]+(?:/(?P<recid>[0-9]+))?'
    _module = 'youtube_dl.extractor.zattoo'


class ORFRadioIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.orf'


class ORFOE1IE(ORFRadioIE):
    _VALID_URL = u'https?://(?P<station>oe1)\\.orf\\.at/player/(?P<date>[0-9]+)/(?P<show>\\w+)'
    _module = 'youtube_dl.extractor.orf'


class YoutubePlaylistsIE(YoutubePlaylistsBaseInfoExtractor):
    _VALID_URL = u'https?://(?:\\w+\\.)?youtube\\.com/(?:user|channel)/(?P<id>[^/]+)/playlists'
    _module = 'youtube_dl.extractor.youtube'


class Porn91IE(LazyLoadExtractor):
    _VALID_URL = u'(?:https?://)(?:www\\.|)91porn\\.com/.+?\\?viewkey=(?P<id>[\\w\\d]+)'
    _module = 'youtube_dl.extractor.porn91'


class VzaarIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:www|view)\\.)?vzaar\\.com/(?:videos/)?(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.vzaar'


class CiscoLiveSearchIE(CiscoLiveBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?ciscolive(?:\\.cisco)?\\.com/(?:global/)?on-demand-library(?:\\.html|/)'
    _module = 'youtube_dl.extractor.ciscolive'

    @classmethod
    def suitable(cls, url):
        return False if CiscoLiveSessionIE.suitable(url) else super(CiscoLiveSearchIE, cls).suitable(url)


class GoogleSearchIE(LazyLoadSearchExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.googlesearch'

    @classmethod
    def suitable(cls, url):
        return re.match(cls._make_valid_url(), url) is not None

    @classmethod
    def _make_valid_url(cls):
        return u'gvsearch(?P<prefix>|[1-9][0-9]*|all):(?P<query>[\\s\\S]+)'


class TeacherTubeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?teachertube\\.com/(viewVideo\\.php\\?video_id=|music\\.php\\?music_id=|video/(?:[\\da-z-]+-)?|audio/)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.teachertube'


class AppleTrailersSectionIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?trailers\\.apple\\.com/#section=(?P<id>justhd|exclusive|justadded|moviestudios|mostpopular)'
    _module = 'youtube_dl.extractor.appletrailers'


class VubeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://vube\\.com/(?:[^/]+/)+(?P<id>[\\da-zA-Z]{10})\\b'
    _module = 'youtube_dl.extractor.vube'


class PacktPubBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.packtpub'


class PacktPubCourseIE(PacktPubBaseIE):
    _VALID_URL = u'(?P<url>https?://(?:(?:www\\.)?packtpub\\.com/mapt|subscription\\.packtpub\\.com)/video/[^/]+/(?P<id>\\d+))'
    _module = 'youtube_dl.extractor.packtpub'

    @classmethod
    def suitable(cls, url):
        return False if PacktPubIE.suitable(url) else super(
            PacktPubCourseIE, cls).suitable(url)


class ViideaIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)https?://(?:www\\.)?(?:\n            videolectures\\.net|\n            flexilearn\\.viidea\\.net|\n            presentations\\.ocwconsortium\\.org|\n            video\\.travel-zoom\\.si|\n            video\\.pomp-forum\\.si|\n            tv\\.nil\\.si|\n            video\\.hekovnik.com|\n            video\\.szko\\.si|\n            kpk\\.viidea\\.com|\n            inside\\.viidea\\.net|\n            video\\.kiberpipa\\.org|\n            bvvideo\\.si|\n            kongres\\.viidea\\.net|\n            edemokracija\\.viidea\\.com\n        )(?:/lecture)?/(?P<id>[^/]+)(?:/video/(?P<part>\\d+))?/*(?:[#?].*)?$'
    _module = 'youtube_dl.extractor.viidea'


class ToonGogglesIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?toongoggles\\.com/shows/(?P<show_id>\\d+)(?:/[^/]+/episodes/(?P<episode_id>\\d+))?'
    _module = 'youtube_dl.extractor.toongoggles'


class LnkGoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?lnkgo\\.(?:alfa\\.)?lt/visi-video/(?P<show>[^/]+)/ziurek-(?P<id>[A-Za-z0-9-]+)'
    _module = 'youtube_dl.extractor.lnkgo'


class ArchiveOrgIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?archive\\.org/(?:details|embed)/(?P<id>[^/?#]+)(?:[?].*)?$'
    _module = 'youtube_dl.extractor.archiveorg'


class WWEBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.wwe'


class WWEIE(WWEBaseIE):
    _VALID_URL = u'https?://(?:[^/]+\\.)?wwe\\.com/(?:[^/]+/)*videos/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.wwe'


class AdobeConnectIE(LazyLoadExtractor):
    _VALID_URL = u'https?://\\w+\\.adobeconnect\\.com/(?P<id>[\\w-]+)'
    _module = 'youtube_dl.extractor.adobeconnect'


class FilmOnChannelIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?filmon\\.com/(?:tv|channel)/(?P<id>[a-z0-9-]+)'
    _module = 'youtube_dl.extractor.filmon'


class PerformGroupIE(LazyLoadExtractor):
    _VALID_URL = u'https?://player\\.performgroup\\.com/eplayer(?:/eplayer\\.html|\\.js)#/?(?P<id>[0-9a-f]{26})\\.(?P<auth_token>[0-9a-z]{26})'
    _module = 'youtube_dl.extractor.performgroup'


class CBSLocalIE(AnvatoIE):
    _VALID_URL = u'https?://[a-z]+\\.cbslocal\\.com/(?:\\d+/\\d+/\\d+|video)/(?P<id>[0-9a-z-]+)'
    _module = 'youtube_dl.extractor.cbslocal'


class TrailerAddictIE(LazyLoadExtractor):
    _VALID_URL = u'(?:https?://)?(?:www\\.)?traileraddict\\.com/(?:trailer|clip)/(?P<movie>.+?)/(?P<trailer_name>.+)'
    _module = 'youtube_dl.extractor.traileraddict'


class HRTiPlaylistIE(HRTiBaseIE):
    _VALID_URL = u'https?://hrti\\.hrt\\.hr/(?:#/)?video/list/category/(?P<id>[0-9]+)/(?P<display_id>[^/]+)?'
    _module = 'youtube_dl.extractor.hrti'


class VimeoWatchLaterIE(VimeoChannelIE):
    _VALID_URL = u'https://vimeo\\.com/(?:home/)?watchlater|:vimeowatchlater'
    _module = 'youtube_dl.extractor.vimeo'


class AWSIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.aws'


class ShahidBaseIE(AWSIE):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.shahid'


class ShahidShowIE(ShahidBaseIE):
    _VALID_URL = u'https?://shahid\\.mbc\\.net/ar/(?:show|serie)s/[^/]+/(?:show|series)-(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.shahid'


class MGTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?mgtv\\.com/(v|b)/(?:[^/]+/)*(?P<id>\\d+)\\.html'
    _module = 'youtube_dl.extractor.mgtv'


class Formula1IE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?formula1\\.com/(?:content/fom-website/)?en/video/\\d{4}/\\d{1,2}/(?P<id>.+?)\\.html'
    _module = 'youtube_dl.extractor.formula1'


class FreshLiveIE(LazyLoadExtractor):
    _VALID_URL = u'https?://freshlive\\.tv/[^/]+/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.freshlive'


class CondeNastIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)https?://(?:video|www|player(?:-backend)?)\\.(?:architecturaldigest|newyorker|arstechnica|gq|teenvogue|wmagazine|brides|self|cnevids|glamour|epicurious|golfdigest|allure|wired|details|vanityfair|bonappetit|cntraveler|vogue)\\.com/\n        (?:\n            (?:\n                embed(?:js)?|\n                (?:script|inline)/video\n            )/(?P<id>[0-9a-f]{24})(?:/(?P<player_id>[0-9a-f]{24}))?(?:.+?\\btarget=(?P<target>[^&]+))?|\n            (?P<type>watch|series|video)/(?P<display_id>[^/?#]+)\n        )'
    _module = 'youtube_dl.extractor.condenast'


class NetzkinoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?netzkino\\.de/\\#!/(?P<category>[^/]+)/(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.netzkino'


class BandcampAlbumIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?P<subdomain>[^.]+)\\.)?bandcamp\\.com(?:/album/(?P<album_id>[^/?#&]+))?'
    _module = 'youtube_dl.extractor.bandcamp'

    @classmethod
    def suitable(cls, url):
        return (False
                if BandcampWeeklyIE.suitable(url) or BandcampIE.suitable(url)
                else super(BandcampAlbumIE, cls).suitable(url))


class BrightcoveNewIE(AdobePassIE):
    _VALID_URL = u'https?://players\\.brightcove\\.net/(?P<account_id>\\d+)/(?P<player_id>[^/]+)_(?P<embed>[^/]+)/index\\.html\\?.*videoId=(?P<video_id>\\d+|ref:[^&]+)'
    _module = 'youtube_dl.extractor.brightcove'


class SevenPlusIE(BrightcoveNewIE):
    _VALID_URL = u'https?://(?:www\\.)?7plus\\.com\\.au/(?P<path>[^?]+\\?.*?\\bepisode-id=(?P<id>[^&#]+))'
    _module = 'youtube_dl.extractor.sevenplus'


class MyVisionTVIE(ZattooIE):
    _VALID_URL = u'https?://(?:www\\.)?myvisiontv\\.ch/watch/(?P<channel>[^/]+?)/(?P<id>[0-9]+)[^/]+(?:/(?P<recid>[0-9]+))?'
    _module = 'youtube_dl.extractor.zattoo'


class TelecincoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?:telecinco\\.es|cuatro\\.com|mediaset\\.es)/(?:[^/]+/)+(?P<id>.+?)\\.html'
    _module = 'youtube_dl.extractor.telecinco'


class DPlayIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?P<domain>www\\.(?P<host>dplay\\.(?P<country>dk|se|no)))/(?:video(?:er|s)/)?(?P<id>[^/]+/[^/?#]+)'
    _module = 'youtube_dl.extractor.dplay'


class DiscoveryNetworksDeIE(DPlayIE):
    _VALID_URL = u'(?x)https?://(?:www\\.)?(?P<site>discovery|tlc|animalplanet|dmax)\\.de/\n                        (?:\n                           .*\\#(?P<id>\\d+)|\n                           (?:[^/]+/)*videos/(?P<display_id>[^/?#]+)|\n                           programme/(?P<programme>[^/]+)/video/(?P<alternate_id>[^/]+)\n                        )'
    _module = 'youtube_dl.extractor.discoverynetworks'


class AZMedienIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:www\\.)?\n                        (?P<host>\n                            telezueri\\.ch|\n                            telebaern\\.tv|\n                            telem1\\.ch\n                        )/\n                        [^/]+/\n                        (?P<id>\n                            [^/]+-(?P<article_id>\\d+)\n                        )\n                        (?:\n                            \\#video=\n                            (?P<kaltura_id>\n                                [_0-9a-z]+\n                            )\n                        )?\n                    '
    _module = 'youtube_dl.extractor.azmedien'


class AWAANSeasonIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?:awaan|dcndigital)\\.ae/(?:#/)?program/(?:(?P<show_id>\\d+)|season/(?P<season_id>\\d+))'
    _module = 'youtube_dl.extractor.awaan'


class SeekerIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?seeker\\.com/(?P<display_id>.*)-(?P<article_id>\\d+)\\.html'
    _module = 'youtube_dl.extractor.seeker'


class NRKTVEpisodeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://tv\\.nrk\\.no/serie/(?P<id>[^/]+/sesong/\\d+/episode/\\d+)'
    _module = 'youtube_dl.extractor.nrk'


class PolskieRadioIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?polskieradio\\.pl/\\d+/\\d+/Artykul/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.polskieradio'


class CultureUnpluggedIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?cultureunplugged\\.com/documentary/watch-online/play/(?P<id>\\d+)(?:/(?P<display_id>[^/]+))?'
    _module = 'youtube_dl.extractor.cultureunplugged'


class BuzzFeedIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?buzzfeed\\.com/[^?#]*?/(?P<id>[^?#]+)'
    _module = 'youtube_dl.extractor.buzzfeed'


class TV5MondePlusIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?tv5mondeplus\\.com/toutes-les-videos/[^/]+/(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.tv5mondeplus'


class MetacriticIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?metacritic\\.com/.+?/trailers/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.metacritic'


class XTubeUserIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?xtube\\.com/profile/(?P<id>[^/]+-\\d+)'
    _module = 'youtube_dl.extractor.xtube'


class KakaoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://tv\\.kakao\\.com/channel/(?P<channel>\\d+)/cliplink/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.kakao'


class EggheadLessonIE(LazyLoadExtractor):
    _VALID_URL = u'https://egghead\\.io/(?:api/v1/)?lessons/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.egghead'


class IviCompilationIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?ivi\\.ru/watch/(?!\\d+)(?P<compilationid>[a-z\\d_-]+)(?:/season(?P<seasonid>\\d+))?$'
    _module = 'youtube_dl.extractor.ivi'


class LinkedInLearningBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.linkedin'


class LinkedInLearningCourseIE(LinkedInLearningBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?linkedin\\.com/learning/(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.linkedin'

    @classmethod
    def suitable(cls, url):
        return False if LinkedInLearningIE.suitable(url) else super(LinkedInLearningCourseIE, cls).suitable(url)


class ACastIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:\n                            (?:(?:embed|www)\\.)?acast\\.com/|\n                            play\\.acast\\.com/s/\n                        )\n                        (?P<channel>[^/]+)/(?P<id>[^/#?]+)\n                    '
    _module = 'youtube_dl.extractor.acast'


class TeamTreeHouseIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?teamtreehouse\\.com/library/(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.teamtreehouse'


class FczenitIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?fc-zenit\\.ru/video/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.fczenit'


class OnetMVPIE(OnetBaseIE):
    _VALID_URL = u'onetmvp:(?P<id>\\d+\\.\\d+)'
    _module = 'youtube_dl.extractor.onet'


class YandexVideoIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:\n                            yandex\\.ru(?:/portal/(?:video|efir))?/?\\?.*?stream_id=|\n                            frontend\\.vh\\.yandex\\.ru/player/\n                        )\n                        (?P<id>[\\da-f]+)\n                    '
    _module = 'youtube_dl.extractor.yandexvideo'


class HistoricFilmsIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?historicfilms\\.com/(?:tapes/|play)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.historicfilms'


class AudioBoomIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?audioboom\\.com/(?:boos|posts)/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.audioboom'


class RutubeEmbedIE(RutubeBaseIE):
    _VALID_URL = u'https?://rutube\\.ru/(?:video|play)/embed/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.rutube'


class MojvideoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?mojvideo\\.com/video-(?P<display_id>[^/]+)/(?P<id>[a-f0-9]+)'
    _module = 'youtube_dl.extractor.mojvideo'


class VimeoAlbumIE(VimeoChannelIE):
    _VALID_URL = u'https://vimeo\\.com/album/(?P<id>\\d+)(?:$|[?#]|/(?!video))'
    _module = 'youtube_dl.extractor.vimeo'


class VimeoGroupsIE(VimeoAlbumIE):
    _VALID_URL = u'https://vimeo\\.com/groups/(?P<name>[^/]+)(?:/(?!videos?/\\d+)|$)'
    _module = 'youtube_dl.extractor.vimeo'


class DigitallySpeakingIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:s?evt\\.dispeak|events\\.digitallyspeaking)\\.com/(?:[^/]+/)+xml/(?P<id>[^.]+)\\.xml'
    _module = 'youtube_dl.extractor.dispeak'


class SapoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:v2|www)\\.)?videos\\.sapo\\.(?:pt|cv|ao|mz|tl)/(?P<id>[\\da-zA-Z]{20})'
    _module = 'youtube_dl.extractor.sapo'


class RadioJavanIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?radiojavan\\.com/videos/video/(?P<id>[^/]+)/?'
    _module = 'youtube_dl.extractor.radiojavan'


class VRVIE(VRVBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?vrv\\.co/watch/(?P<id>[A-Z0-9]+)'
    _module = 'youtube_dl.extractor.vrv'


class WebcasterIE(LazyLoadExtractor):
    _VALID_URL = u'https?://bl\\.webcaster\\.pro/(?:quote|media)/start/free_(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.webcaster'


class MySpassIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?myspass\\.de/.*'
    _module = 'youtube_dl.extractor.myspass'


class ORFFM4IE(ORFRadioIE):
    _VALID_URL = u'https?://(?P<station>fm4)\\.orf\\.at/player/(?P<date>[0-9]+)/(?P<show>\\w+)'
    _module = 'youtube_dl.extractor.orf'


class MiTeleIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?mitele\\.es/(?:[^/]+/)+(?P<id>[^/]+)/player'
    _module = 'youtube_dl.extractor.mitele'


class FrontendMastersCourseIE(FrontendMastersPageBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?frontendmasters\\.com/courses/(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.frontendmasters'

    @classmethod
    def suitable(cls, url):
        return False if FrontendMastersLessonIE.suitable(url) else super(
            FrontendMastersBaseIE, cls).suitable(url)


class OsnatelTVIE(ZattooIE):
    _VALID_URL = u'https?://(?:www\\.)?tvonline\\.osnatel\\.de/watch/(?P<channel>[^/]+?)/(?P<id>[0-9]+)[^/]+(?:/(?P<recid>[0-9]+))?'
    _module = 'youtube_dl.extractor.zattoo'


class GoIE(AdobePassIE):
    _VALID_URL = u'https?://(?:(?P<sub_domain>freeform|watchdisneychannel|abc|watchdisneyxd|watchdisneyjunior|disneynow)\\.)?go\\.com/(?:(?:[^/]+/)*(?P<id>vdka\\w+)|(?:[^/]+/)*(?P<display_id>[^/?#]+))'
    _module = 'youtube_dl.extractor.go'


class UFCTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?ufc\\.tv/video/(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.ufctv'


class LRTIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?lrt\\.lt/mediateka/irasas/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.lrt'


class OnetIE(OnetBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?onet\\.tv/[a-z]/[a-z]+/(?P<display_id>[0-9a-z-]+)/(?P<id>[0-9a-z]+)'
    _module = 'youtube_dl.extractor.onet'


class VineUserIE(LazyLoadExtractor):
    _VALID_URL = u'https?://vine\\.co/(?P<u>u/)?(?P<user>[^/]+)'
    _module = 'youtube_dl.extractor.vine'

    @classmethod
    def suitable(cls, url):
        return False if VineIE.suitable(url) else super(VineUserIE, cls).suitable(url)


class MediciIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?medici\\.tv/#!/(?P<id>[^?#&]+)'
    _module = 'youtube_dl.extractor.medici'


class WebOfStoriesIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?webofstories\\.com/play/(?:[^/]+/)?(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.webofstories'


class NDREmbedBaseIE(LazyLoadExtractor):
    _VALID_URL = u'(?:ndr:(?P<id_s>[\\da-z]+)|https?://www\\.ndr\\.de/(?P<id>[\\da-z]+)-ppjson\\.json)'
    _module = 'youtube_dl.extractor.ndr'


class LimelightChannelIE(LimelightBaseIE):
    _VALID_URL = u'(?x)\n                        (?:\n                            limelight:channel:|\n                            https?://\n                                (?:\n                                    link\\.videoplatform\\.limelight\\.com/media/|\n                                    assets\\.delvenetworks\\.com/player/loader\\.swf\n                                )\n                                \\?.*?\\bchannelId=\n                        )\n                        (?P<id>[a-z0-9]{32})\n                    '
    _module = 'youtube_dl.extractor.limelight'


class RICEIE(LazyLoadExtractor):
    _VALID_URL = u'https?://mediahub\\.rice\\.edu/app/[Pp]ortal/video\\.aspx\\?(?P<query>.+)'
    _module = 'youtube_dl.extractor.rice'


class DouyuTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?douyu(?:tv)?\\.com/(?:[^/]+/)*(?P<id>[A-Za-z0-9]+)'
    _module = 'youtube_dl.extractor.douyutv'


class JamendoIE(JamendoBaseIE):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:\n                            licensing\\.jamendo\\.com/[^/]+|\n                            (?:www\\.)?jamendo\\.com\n                        )\n                        /track/(?P<id>[0-9]+)/(?P<display_id>[^/?#&]+)\n                    '
    _module = 'youtube_dl.extractor.jamendo'


class CanalplusIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?P<site>mycanal|piwiplus)\\.fr/(?:[^/]+/)*(?P<display_id>[^?/]+)(?:\\.html\\?.*\\bvid=|/p/)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.canalplus'


class QQMusicPlaylistIE(QQPlaylistBaseIE):
    _VALID_URL = u'https?://y\\.qq\\.com/n/yqq/playlist/(?P<id>[0-9]+)\\.html'
    _module = 'youtube_dl.extractor.qqmusic'


class MangomoloVideoIE(MangomoloBaseIE):
    _VALID_URL = u'https?://admin\\.mangomolo\\.com/analytics/index\\.php/customers/embed/video\\?.*?\\bid=(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.mangomolo'


class Go90IE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?go90\\.com/(?:videos|embed)/(?P<id>[0-9a-zA-Z]+)'
    _module = 'youtube_dl.extractor.go90'


class BigflixIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?bigflix\\.com/.+/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.bigflix'


class YoutubeSearchDateIE(YoutubeSearchIE):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.youtube'

    @classmethod
    def suitable(cls, url):
        return re.match(cls._make_valid_url(), url) is not None

    @classmethod
    def _make_valid_url(cls):
        return u'ytsearchdate(?P<prefix>|[1-9][0-9]*|all):(?P<query>[\\s\\S]+)'


class TruNewsIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?trunews\\.com/stream/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.trunews'


class RteBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.rte'


class RteRadioIE(RteBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?rte\\.ie/radio/utils/radioplayer/rteradioweb\\.html#!rii=(?:b?[0-9]*)(?:%3A|:|%5F|_)(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.rte'


class TutvIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?tu\\.tv/videos/(?P<id>[^/?]+)'
    _module = 'youtube_dl.extractor.tutv'


class ThePlatformIE(ThePlatformBaseIE, AdobePassIE):
    _VALID_URL = u'(?x)\n        (?:https?://(?:link|player)\\.theplatform\\.com/[sp]/(?P<provider_id>[^/]+)/\n           (?:(?:(?:[^/]+/)+select/)?(?P<media>media/(?:guid/\\d+/)?)?|(?P<config>(?:[^/\\?]+/(?:swf|config)|onsite)/select/))?\n         |theplatform:)(?P<id>[^/\\?&]+)'
    _module = 'youtube_dl.extractor.theplatform'


class TheWeatherChannelIE(ThePlatformIE):
    _VALID_URL = u'https?://(?:www\\.)?weather\\.com/(?:[^/]+/)*video/(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.theweatherchannel'


class SkyNewsArabiaIE(SkyNewsArabiaBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?skynewsarabia\\.com/web/video/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.skynewsarabia'


class ArteTVInfoIE(ArteTVPlus7IE):
    _VALID_URL = u'https?://info\\.arte\\.tv/(?P<lang>fr|de|en|es)/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.arte'

    @classmethod
    def suitable(cls, url):
        return False if ArteTVPlaylistIE.suitable(url) else super(ArteTVPlus7IE, cls).suitable(url)


class TVPlayIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    (?:\n                        mtg:|\n                        https?://\n                            (?:www\\.)?\n                            (?:\n                                tvplay(?:\\.skaties)?\\.lv(?:/parraides)?|\n                                (?:tv3play|play\\.tv3)\\.lt(?:/programos)?|\n                                tv3play(?:\\.tv3)?\\.ee/sisu|\n                                (?:tv(?:3|6|8|10)play|viafree)\\.se/program|\n                                (?:(?:tv3play|viasat4play|tv6play|viafree)\\.no|(?:tv3play|viafree)\\.dk)/programmer|\n                                play\\.nova(?:tv)?\\.bg/programi\n                            )\n                            /(?:[^/]+/)+\n                        )\n                        (?P<id>\\d+)\n                    '
    _module = 'youtube_dl.extractor.tvplay'


class FranceCultureIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?franceculture\\.fr/emissions/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.franceculture'


class TNAFlixIE(TNAEMPFlixBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?tnaflix\\.com/[^/]+/(?P<display_id>[^/]+)/video(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.tnaflix'


class ARDBetaMediathekIE(LazyLoadExtractor):
    _VALID_URL = u'https://(?:beta|www)\\.ardmediathek\\.de/[^/]+/(?:player|live)/(?P<video_id>[a-zA-Z0-9]+)(?:/(?P<display_id>[^/?#]+))?'
    _module = 'youtube_dl.extractor.ard'


class DaumClipIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:m\\.)?tvpot\\.daum\\.net/(?:clip/ClipView.(?:do|tv)|mypot/View.do)\\?.*?clipid=(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.daum'

    @classmethod
    def suitable(cls, url):
        return False if DaumPlaylistIE.suitable(url) or DaumUserIE.suitable(url) else super(DaumClipIE, cls).suitable(url)


class ScreencastIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?screencast\\.com/t/(?P<id>[a-zA-Z0-9]+)'
    _module = 'youtube_dl.extractor.screencast'


class FranceTVIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    (?:\n                        https?://\n                            sivideo\\.webservices\\.francetelevisions\\.fr/tools/getInfosOeuvre/v2/\\?\n                            .*?\\bidDiffusion=[^&]+|\n                        (?:\n                            https?://videos\\.francetv\\.fr/video/|\n                            francetv:\n                        )\n                        (?P<id>[^@]+)(?:@(?P<catalog>.+))?\n                    )\n                    '
    _module = 'youtube_dl.extractor.francetv'


class VRTIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:deredactie|sporza|cobra(?:\\.canvas)?)\\.be/cm/(?:[^/]+/)+(?P<id>[^/]+)/*'
    _module = 'youtube_dl.extractor.vrt'


class ARDMediathekIE(LazyLoadExtractor):
    _VALID_URL = u'^https?://(?:(?:(?:www|classic)\\.)?ardmediathek\\.de|mediathek\\.(?:daserste|rbb-online)\\.de|one\\.ard\\.de)/(?:.*/)(?P<video_id>[0-9]+|[^0-9][^/\\?]+)[^/\\?]*(?:\\?.*)?'
    _module = 'youtube_dl.extractor.ard'

    @classmethod
    def suitable(cls, url):
        return False if ARDBetaMediathekIE.suitable(url) else super(ARDMediathekIE, cls).suitable(url)


class SRMediathekIE(ARDMediathekIE):
    _VALID_URL = u'https?://sr-mediathek(?:\\.sr-online)?\\.de/index\\.php\\?.*?&id=(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.srmediathek'

    @classmethod
    def suitable(cls, url):
        return False if ARDBetaMediathekIE.suitable(url) else super(ARDMediathekIE, cls).suitable(url)


class PornHubIE(PornHubBaseIE):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:\n                            (?:[^/]+\\.)?(?P<host>pornhub\\.(?:com|net))/(?:(?:view_video\\.php|video/show)\\?viewkey=|embed/)|\n                            (?:www\\.)?thumbzilla\\.com/video/\n                        )\n                        (?P<id>[\\da-z]+)\n                    '
    _module = 'youtube_dl.extractor.pornhub'


class AENetworksBaseIE(ThePlatformIE):
    _VALID_URL = u'(?x)\n        (?:https?://(?:link|player)\\.theplatform\\.com/[sp]/(?P<provider_id>[^/]+)/\n           (?:(?:(?:[^/]+/)+select/)?(?P<media>media/(?:guid/\\d+/)?)?|(?P<config>(?:[^/\\?]+/(?:swf|config)|onsite)/select/))?\n         |theplatform:)(?P<id>[^/\\?&]+)'
    _module = 'youtube_dl.extractor.aenetworks'


class HistoryTopicIE(AENetworksBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?history\\.com/topics/[^/]+/(?P<id>[\\w+-]+?)-video'
    _module = 'youtube_dl.extractor.aenetworks'


class InternazionaleIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?internazionale\\.it/video/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.internazionale'


class NetEaseMusicProgramIE(NetEaseMusicBaseIE):
    _VALID_URL = u'https?://music\\.163\\.com/(#/?)program\\?id=(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.neteasemusic'


class SunPornoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:www\\.)?sunporno\\.com/videos|embeds\\.sunporno\\.com/embed)/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.sunporno'


class NJoyEmbedIE(NDREmbedBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?n-joy\\.de/(?:[^/]+/)*(?P<id>[\\da-z]+)-(?:player|externalPlayer)_[^/]+\\.html'
    _module = 'youtube_dl.extractor.ndr'


class NPORadioFragmentIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?npo\\.nl/radio/[^/]+/fragment/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.npo'


class JoveIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?jove\\.com/video/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.jove'


class GDCVaultIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?gdcvault\\.com/play/(?P<id>\\d+)(?:/(?P<name>[\\w-]+))?'
    _module = 'youtube_dl.extractor.gdcvault'


class TVNowSeasonIE(TVNowListBaseIE):
    _VALID_URL = u'(?x)\n                    (?P<base_url>\n                        https?://\n                            (?:www\\.)?tvnow\\.(?:de|at|ch)/(?:shows|serien)/\n                            [^/?#&]+-(?P<show_id>\\d+)\n                    )\n                    /staffel-(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.tvnow'

    @classmethod
    def suitable(cls, url):
        return (False if TVNowNewIE.suitable(url)
                else super(TVNowListBaseIE, cls).suitable(url))


class TeleMBIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?telemb\\.be/(?P<display_id>.+?)_d_(?P<id>\\d+)\\.html'
    _module = 'youtube_dl.extractor.telemb'


class NBCSportsStreamIE(AdobePassIE):
    _VALID_URL = u'https?://stream\\.nbcsports\\.com/.+?\\bpid=(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.nbc'


class GenerationWhatIE(LazyLoadExtractor):
    _VALID_URL = u'https?://generation-what\\.francetv\\.fr/[^/]+/video/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.francetv'


class NJoyIE(NDRBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?n-joy\\.de/(?:[^/]+/)*(?:(?P<display_id>[^/?#]+),)?(?P<id>[\\da-z]+)\\.html'
    _module = 'youtube_dl.extractor.ndr'


class TeachableCourseIE(TeachableBaseIE):
    _VALID_URL = u'(?x)\n                        (?:\n                            teachable:https?://(?P<site_t>[^/]+)|\n                            https?://(?:www\\.)?(?P<site>edurila\\.com|upskillcourses\\.com|learnability\\.org|courses\\.workitdaily\\.com|academyhacker\\.com|stackskills\\.com|market\\.saleshacker\\.com|academy\\.gns3\\.com)\n                        )\n                        /(?:courses|p)/(?:enrolled/)?(?P<id>[^/?#&]+)\n                    '
    _module = 'youtube_dl.extractor.teachable'

    @classmethod
    def suitable(cls, url):
        return False if TeachableIE.suitable(url) else super(
            TeachableCourseIE, cls).suitable(url)


class FazIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?faz\\.net/(?:[^/]+/)*.*?-(?P<id>\\d+)\\.html'
    _module = 'youtube_dl.extractor.faz'


class HentaiStigmaIE(LazyLoadExtractor):
    _VALID_URL = u'^https?://hentai\\.animestigma\\.com/(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.hentaistigma'


class AuroraVidIE(NovaMovIE):
    _VALID_URL = u'(?x)\n                            http://\n                                (?:\n                                    (?:www\\.)?auroravid\\.to/(?:file|video|mobile/\\#/videos)/|\n                                    (?:(?:embed|www)\\.)auroravid\\.to/embed(?:\\.php|/)?\\?(?:.*?&)?\\bv=\n                                )\n                                (?P<id>[a-z\\d]{13})\n                            '
    _module = 'youtube_dl.extractor.novamov'


class ThisOldHouseIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?thisoldhouse\\.com/(?:watch|how-to|tv-episode)/(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.thisoldhouse'


class MSNIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?msn\\.com/(?:[^/]+/)+(?P<display_id>[^/]+)/[a-z]{2}-(?P<id>[\\da-zA-Z]+)'
    _module = 'youtube_dl.extractor.msn'


class NetEaseMusicIE(NetEaseMusicBaseIE):
    _VALID_URL = u'https?://music\\.163\\.com/(#/)?song\\?id=(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.neteasemusic'


class NovaIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:[^.]+\\.)?(?P<site>tv(?:noviny)?|tn|novaplus|vymena|fanda|krasna|doma|prask)\\.nova\\.cz/(?:[^/]+/)+(?P<id>[^/]+?)(?:\\.html|/|$)'
    _module = 'youtube_dl.extractor.nova'


class MTVIE(MTVServicesInfoExtractor):
    _VALID_URL = u'https?://(?:www\\.)?mtv\\.com/(?:video-clips|(?:full-)?episodes)/(?P<id>[^/?#.]+)'
    _module = 'youtube_dl.extractor.mtv'


class CMTIE(MTVIE):
    _VALID_URL = u'https?://(?:www\\.)?cmt\\.com/(?:videos|shows|(?:full-)?episodes|video-clips)/(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.cmt'


class BitChuteIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?bitchute\\.com/(?:video|embed|torrent/[^/]+)/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.bitchute'


class OoyalaExternalIE(OoyalaBaseIE):
    _VALID_URL = u'(?x)\n                    (?:\n                        ooyalaexternal:|\n                        https?://.+?\\.ooyala\\.com/.*?\\bexternalId=\n                    )\n                    (?P<partner_id>[^:]+)\n                    :\n                    (?P<id>.+)\n                    (?:\n                        :|\n                        .*?&pcode=\n                    )\n                    (?P<pcode>.+?)\n                    (?:&|$)\n                    '
    _module = 'youtube_dl.extractor.ooyala'


class XBefIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?xbef\\.com/video/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.xbef'


class NBCOlympicsStreamIE(AdobePassIE):
    _VALID_URL = u'https?://stream\\.nbcolympics\\.com/(?P<id>[0-9a-z-]+)'
    _module = 'youtube_dl.extractor.nbc'


class PhilharmonieDeParisIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:\n                            live\\.philharmoniedeparis\\.fr/(?:[Cc]oncert/|misc/Playlist\\.ashx\\?id=)|\n                            pad\\.philharmoniedeparis\\.fr/doc/CIMU/\n                        )\n                        (?P<id>\\d+)\n                    '
    _module = 'youtube_dl.extractor.philharmoniedeparis'


class ChirbitIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?chirb\\.it/(?:(?:wp|pl)/|fb_chirbit_player\\.swf\\?key=)?(?P<id>[\\da-zA-Z]+)'
    _module = 'youtube_dl.extractor.chirbit'


class RutubeChannelIE(RutubePlaylistBaseIE):
    _VALID_URL = u'https?://rutube\\.ru/tags/video/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.rutube'


class FirstTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?1tv\\.ru/(?:[^/]+/)+(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.firsttv'


class AMCNetworksIE(ThePlatformIE):
    _VALID_URL = u'https?://(?:www\\.)?(?:amc|bbcamerica|ifc|(?:we|sundance)tv)\\.com/(?:movies|shows(?:/[^/]+)+)/(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.amcnetworks'


class ServingSysIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:[^.]+\\.)?serving-sys\\.com/BurstingPipe/adServer\\.bs\\?.*?&pli=(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.servingsys'


class VuClipIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:m\\.)?vuclip\\.com/w\\?.*?cid=(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.vuclip'


class YoutubeSubscriptionsIE(YoutubeFeedsInfoExtractor):
    _VALID_URL = u'https?://(?:www\\.)?youtube\\.com/feed/subscriptions|:ytsubs(?:criptions)?'
    _module = 'youtube_dl.extractor.youtube'


class VeeHDIE(LazyLoadExtractor):
    _VALID_URL = u'https?://veehd\\.com/video/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.veehd'


class VodlockerIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?vodlocker\\.(?:com|city)/(?:embed-)?(?P<id>[0-9a-zA-Z]+)(?:\\..*?)?'
    _module = 'youtube_dl.extractor.vodlocker'


class UdemyIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:[^/]+\\.)?udemy\\.com/\n                        (?:\n                            [^#]+\\#/lecture/|\n                            lecture/view/?\\?lectureId=|\n                            [^/]+/learn/v4/t/lecture/\n                        )\n                        (?P<id>\\d+)\n                    '
    _module = 'youtube_dl.extractor.udemy'


class MmsIE(LazyLoadExtractor):
    _VALID_URL = u'(?i)mms://.+'
    _module = 'youtube_dl.extractor.commonprotocols'


class BBCIE(BBCCoUkIE):
    _VALID_URL = u'https?://(?:www\\.)?bbc\\.(?:com|co\\.uk)/(?:[^/]+/)+(?P<id>[^/#?]+)'
    _module = 'youtube_dl.extractor.bbc'

    @classmethod
    def suitable(cls, url):
        EXCLUDE_IE = (BBCCoUkIE, BBCCoUkArticleIE, BBCCoUkIPlayerPlaylistIE, BBCCoUkPlaylistIE)
        return (False if any(ie.suitable(url) for ie in EXCLUDE_IE)
                else super(BBCIE, cls).suitable(url))


class KuwoAlbumIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?kuwo\\.cn/album/(?P<id>\\d+?)/'
    _module = 'youtube_dl.extractor.kuwo'


class NextTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?nexttv\\.com\\.tw/(?:[^/]+/)+(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.nextmedia'


class RadioCanadaAudioVideoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://ici\\.radio-canada\\.ca/([^/]+/)*media-(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.radiocanada'


class TV2IE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?tv2\\.no/v/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.tv2'


class SprutoBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.vimple'


class VimpleIE(SprutoBaseIE):
    _VALID_URL = u'https?://(?:player\\.vimple\\.(?:ru|co)/iframe|vimple\\.(?:ru|co))/(?P<id>[\\da-f-]{32,36})'
    _module = 'youtube_dl.extractor.vimple'


class YinYueTaiIE(LazyLoadExtractor):
    _VALID_URL = u'https?://v\\.yinyuetai\\.com/video(?:/h5)?/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.yinyuetai'


class TennisTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?tennistv\\.com/videos/(?P<id>[-a-z0-9]+)'
    _module = 'youtube_dl.extractor.tennistv'


class RaiPlayLiveIE(RaiBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?raiplay\\.it/dirette/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.rai'


class AlJazeeraIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?aljazeera\\.com/(?:programmes|video)/.*?/(?P<id>[^/]+)\\.html'
    _module = 'youtube_dl.extractor.aljazeera'


class CBCWatchVideoIE(CBCWatchBaseIE):
    _VALID_URL = u'https?://api-cbc\\.cloud\\.clearleap\\.com/cloffice/client/web/play/?\\?.*?\\bcontentId=(?P<id>[\\da-f]{8}-[\\da-f]{4}-[\\da-f]{4}-[\\da-f]{4}-[\\da-f]{12})'
    _module = 'youtube_dl.extractor.cbc'


class SAKTVIE(ZattooIE):
    _VALID_URL = u'https?://(?:www\\.)?saktv\\.ch/watch/(?P<channel>[^/]+?)/(?P<id>[0-9]+)[^/]+(?:/(?P<recid>[0-9]+))?'
    _module = 'youtube_dl.extractor.zattoo'


class SpringboardPlatformIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        cms\\.springboardplatform\\.com/\n                        (?:\n                            (?:previews|embed_iframe)/(?P<index>\\d+)/video/(?P<id>\\d+)|\n                            xml_feeds_advanced/index/(?P<index_2>\\d+)/rss3/(?P<id_2>\\d+)\n                        )\n                    '
    _module = 'youtube_dl.extractor.springboardplatform'


class OdnoklassnikiIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                https?://\n                    (?:(?:www|m|mobile)\\.)?\n                    (?:odnoklassniki|ok)\\.ru/\n                    (?:\n                        video(?:embed)?/|\n                        web-api/video/moviePlayer/|\n                        live/|\n                        dk\\?.*?st\\.mvId=\n                    )\n                    (?P<id>[\\d-]+)\n                '
    _module = 'youtube_dl.extractor.odnoklassniki'


class TV2HuIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?tv2\\.hu/(?:[^/]+/)+(?P<id>\\d+)_[^/?#]+?\\.html'
    _module = 'youtube_dl.extractor.tv2hu'


class PornoXOIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?pornoxo\\.com/videos/(?P<id>\\d+)/(?P<display_id>[^/]+)\\.html'
    _module = 'youtube_dl.extractor.pornoxo'


class RedditRIE(LazyLoadExtractor):
    _VALID_URL = u'(?P<url>https?://(?:[^/]+\\.)?reddit\\.com/r/[^/]+/comments/(?P<id>[^/?#&]+))'
    _module = 'youtube_dl.extractor.reddit'


class EightTracksIE(LazyLoadExtractor):
    _VALID_URL = u'https?://8tracks\\.com/(?P<user>[^/]+)/(?P<id>[^/#]+)(?:#.*)?$'
    _module = 'youtube_dl.extractor.eighttracks'


class WakanimIE(LazyLoadExtractor):
    _VALID_URL = u'https://(?:www\\.)?wakanim\\.tv/[^/]+/v2/catalogue/episode/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.wakanim'


class BIQLEIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?biqle\\.(?:com|org|ru)/watch/(?P<id>-?\\d+_\\d+)'
    _module = 'youtube_dl.extractor.biqle'


class SouthParkIE(MTVServicesInfoExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?P<url>southpark\\.cc\\.com/(?:clips|(?:full-)?episodes|collections)/(?P<id>.+?)(\\?|#|$))'
    _module = 'youtube_dl.extractor.southpark'


class SouthParkDeIE(SouthParkIE):
    _VALID_URL = u'https?://(?:www\\.)?(?P<url>southpark\\.de/(?:clips|alle-episoden|collections)/(?P<id>.+?)(\\?|#|$))'
    _module = 'youtube_dl.extractor.southpark'


class SouthParkNlIE(SouthParkIE):
    _VALID_URL = u'https?://(?:www\\.)?(?P<url>southpark\\.nl/(?:clips|(?:full-)?episodes|collections)/(?P<id>.+?)(\\?|#|$))'
    _module = 'youtube_dl.extractor.southpark'


class SouthParkEsIE(SouthParkIE):
    _VALID_URL = u'https?://(?:www\\.)?(?P<url>southpark\\.cc\\.com/episodios-en-espanol/(?P<id>.+?)(\\?|#|$))'
    _module = 'youtube_dl.extractor.southpark'


class SouthParkDkIE(SouthParkIE):
    _VALID_URL = u'https?://(?:www\\.)?(?P<url>southparkstudios\\.(?:dk|nu)/(?:clips|full-episodes|collections)/(?P<id>.+?)(\\?|#|$))'
    _module = 'youtube_dl.extractor.southpark'


class LcpIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?lcp\\.fr/(?:[^/]+/)*(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.lcp'


class ViceShowIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:.+?\\.)?vice\\.com/(?:[^/]+/)?show/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.vice'


class AbcNewsIE(LazyLoadExtractor):
    _VALID_URL = u'https?://abcnews\\.go\\.com/(?:[^/]+/)+(?P<display_id>[0-9a-z-]+)/story\\?id=(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.abcnews'


class TheStarIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?thestar\\.com/(?:[^/]+/)*(?P<id>.+)\\.html'
    _module = 'youtube_dl.extractor.thestar'


class NewgroundsPlaylistIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?newgrounds\\.com/(?:collection|[^/]+/search/[^/]+)/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.newgrounds'


class TweakersIE(LazyLoadExtractor):
    _VALID_URL = u'https?://tweakers\\.net/video/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.tweakers'


class FunimationIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?funimation(?:\\.com|now\\.uk)/shows/[^/]+/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.funimation'


class RadioCanadaIE(LazyLoadExtractor):
    _VALID_URL = u'(?:radiocanada:|https?://ici\\.radio-canada\\.ca/widgets/mediaconsole/)(?P<app_code>[^:/]+)[:/](?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.radiocanada'


class TouTvIE(RadioCanadaIE):
    _VALID_URL = u'https?://ici\\.tou\\.tv/(?P<id>[a-zA-Z0-9_-]+(?:/S[0-9]+[EC][0-9]+)?)'
    _module = 'youtube_dl.extractor.toutv'


class RTVNHIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?rtvnh\\.nl/video/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.rtvnh'


class VoxMediaVolumeIE(OnceIE):
    _VALID_URL = u'https?://volume\\.vox-cdn\\.com/embed/(?P<id>[0-9a-f]{9})'
    _module = 'youtube_dl.extractor.voxmedia'


class CamModelsIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?cammodels\\.com/cam/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.cammodels'


class KalturaIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                (?:\n                    kaltura:(?P<partner_id>\\d+):(?P<id>[0-9a-z_]+)|\n                    https?://\n                        (:?(?:www|cdnapi(?:sec)?)\\.)?kaltura\\.com(?::\\d+)?/\n                        (?:\n                            (?:\n                                # flash player\n                                index\\.php/(?:kwidget|extwidget/preview)|\n                                # html5 player\n                                html5/html5lib/[^/]+/mwEmbedFrame\\.php\n                            )\n                        )(?:/(?P<path>[^?]+))?(?:\\?(?P<query>.*))?\n                )\n                '
    _module = 'youtube_dl.extractor.kaltura'


class SteamIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n        https?://store\\.steampowered\\.com/\n            (agecheck/)?\n            (?P<urltype>video|app)/ #If the page is only for videos or for a game\n            (?P<gameID>\\d+)/?\n            (?P<videoID>\\d*)(?P<extra>\\??) # For urltype == video we sometimes get the videoID\n        |\n        https?://(?:www\\.)?steamcommunity\\.com/sharedfiles/filedetails/\\?id=(?P<fileID>[0-9]+)\n    '
    _module = 'youtube_dl.extractor.steam'


class RTVEALaCartaIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?rtve\\.es/(m/)?(alacarta/videos|filmoteca)/[^/]+/[^/]+/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.rtve'


class ComCarCoffIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?comediansincarsgettingcoffee\\.com/(?P<id>[a-z0-9\\-]*)'
    _module = 'youtube_dl.extractor.comcarcoff'


class MgoonIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)https?://(?:www\\.)?\n    (?:(:?m\\.)?mgoon\\.com/(?:ch/(?:.+)/v|play/view)|\n        video\\.mgoon\\.com)/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.mgoon'


class TVCIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?tvc\\.ru/video/iframe/id/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.tvc'


class ToshIE(MTVServicesInfoExtractor):
    _VALID_URL = u'^https?://tosh\\.cc\\.com/video-(?:clips|collections)/[^/]+/(?P<videotitle>[^/?#]+)'
    _module = 'youtube_dl.extractor.comedycentral'


class RTL2IE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?rtl2\\.de/sendung/[^/]+/(?:video/(?P<vico_id>\\d+)[^/]+/(?P<vivi_id>\\d+)-|folge/)(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.rtl2'


class EHowIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?ehow\\.com/[^/_?]*_(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.ehow'


class GiantBombIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?giantbomb\\.com/videos/(?P<display_id>[^/]+)/(?P<id>\\d+-\\d+)'
    _module = 'youtube_dl.extractor.giantbomb'


class HornBunnyIE(LazyLoadExtractor):
    _VALID_URL = u'http?://(?:www\\.)?hornbunny\\.com/videos/(?P<title_dash>[a-z-]+)-(?P<id>\\d+)\\.html'
    _module = 'youtube_dl.extractor.hornbunny'


class VShareIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?vshare\\.io/[dv]/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.vshare'


class MyviEmbedIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?myvi\\.tv/(?:[^?]+\\?.*?\\bv=|embed/)(?P<id>[\\da-z]+)'
    _module = 'youtube_dl.extractor.myvi'

    @classmethod
    def suitable(cls, url):
        return False if MyviIE.suitable(url) else super(MyviEmbedIE, cls).suitable(url)


class KinoPoiskIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?kinopoisk\\.ru/film/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.kinopoisk'


class FranceTVEmbedIE(FranceTVBaseInfoExtractor):
    _VALID_URL = u'https?://embed\\.francetv\\.fr/*\\?.*?\\bue=(?P<id>[^&]+)'
    _module = 'youtube_dl.extractor.francetv'


class PlaysTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?plays\\.tv/(?:video|embeds)/(?P<id>[0-9a-f]{18})'
    _module = 'youtube_dl.extractor.plays'


class DotsubIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?dotsub\\.com/view/(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.dotsub'


class TastyTradeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?tastytrade\\.com/tt/shows/[^/]+/episodes/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.tastytrade'


class MnetIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?mnet\\.(?:com|interest\\.me)/tv/vod/(?:.*?\\bclip_id=)?(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.mnet'


class NextMediaIE(LazyLoadExtractor):
    _VALID_URL = u'https?://hk\\.apple\\.nextmedia\\.com/[^/]+/[^/]+/(?P<date>\\d+)/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.nextmedia'


class NextMediaActionNewsIE(NextMediaIE):
    _VALID_URL = u'https?://hk\\.dv\\.nextmedia\\.com/actionnews/[^/]+/(?P<date>\\d+)/(?P<id>\\d+)/\\d+'
    _module = 'youtube_dl.extractor.nextmedia'


class CeskaTelevizeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?ceskatelevize\\.cz/ivysilani/(?:[^/?#&]+/)*(?P<id>[^/#?]+)'
    _module = 'youtube_dl.extractor.ceskatelevize'


class PeopleIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?people\\.com/people/videos/0,,(?P<id>\\d+),00\\.html'
    _module = 'youtube_dl.extractor.people'


class FoxNewsIE(AMPIE):
    _VALID_URL = u'https?://(?P<host>video\\.(?:insider\\.)?fox(?:news|business)\\.com)/v/(?:video-embed\\.html\\?video_id=)?(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.foxnews'


class RedTubeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:www\\.)?redtube\\.com/|embed\\.redtube\\.com/\\?.*?\\bid=)(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.redtube'


class TV4IE(LazyLoadExtractor):
    _VALID_URL = u'(?x)https?://(?:www\\.)?\n        (?:\n            tv4\\.se/(?:[^/]+)/klipp/(?:.*)-|\n            tv4play\\.se/\n            (?:\n                (?:program|barn)/(?:[^/]+/|(?:[^\\?]+)\\?video_id=)|\n                iframe/video/|\n                film/|\n                sport/|\n            )\n        )(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.tv4'


class VidmeListBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.vidme'


class VidmeUserLikesIE(VidmeListBaseIE):
    _VALID_URL = u'https?://vid\\.me/(?:e/)?(?P<id>[\\da-zA-Z_-]{6,})/likes'
    _module = 'youtube_dl.extractor.vidme'


class PicartoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www.)?picarto\\.tv/(?P<id>[a-zA-Z0-9]+)(?:/(?P<token>[a-zA-Z0-9]+))?'
    _module = 'youtube_dl.extractor.picarto'

    @classmethod
    def suitable(cls, url):
        return False if PicartoVodIE.suitable(url) else super(PicartoIE, cls).suitable(url)


class NetEaseMusicAlbumIE(NetEaseMusicBaseIE):
    _VALID_URL = u'https?://music\\.163\\.com/(#/)?album\\?id=(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.neteasemusic'


class DWArticleIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?dw\\.com/(?:[^/]+/)+a-(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.dw'


class VideomoreIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    videomore:(?P<sid>\\d+)$|\n                    https?://(?:player\\.)?videomore\\.ru/\n                        (?:\n                            (?:\n                                embed|\n                                [^/]+/[^/]+\n                            )/|\n                            [^/]*\\?.*?\\btrack_id=\n                        )\n                        (?P<id>\\d+)\n                        (?:[/?#&]|\\.(?:xml|json)|$)\n                    '
    _module = 'youtube_dl.extractor.videomore'


class MofosexIE(KeezMoviesIE):
    _VALID_URL = u'https?://(?:www\\.)?mofosex\\.com/videos/(?P<id>\\d+)/(?P<display_id>[^/?#&.]+)\\.html'
    _module = 'youtube_dl.extractor.mofosex'


class XXXYMoviesIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?xxxymovies\\.com/videos/(?P<id>\\d+)/(?P<display_id>[^/]+)'
    _module = 'youtube_dl.extractor.xxxymovies'


class KaraoketvIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?karaoketv\\.co\\.il/[^/]+/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.karaoketv'


class StreamableIE(LazyLoadExtractor):
    _VALID_URL = u'https?://streamable\\.com/(?:[es]/)?(?P<id>\\w+)'
    _module = 'youtube_dl.extractor.streamable'


class NaverIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:m\\.)?tv(?:cast)?\\.naver\\.com/v/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.naver'


class NRKTVSeasonIE(NRKTVSerieBaseIE):
    _VALID_URL = u'https?://tv\\.nrk\\.no/serie/[^/]+/sesong/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.nrk'

    @classmethod
    def suitable(cls, url):
        return (False if NRKTVIE.suitable(url) or NRKTVEpisodeIE.suitable(url)
                else super(NRKTVSeasonIE, cls).suitable(url))


class RTSIE(SRGSSRIE):
    _VALID_URL = u'rts:(?P<rts_id>\\d+)|https?://(?:.+?\\.)?rts\\.ch/(?:[^/]+/){2,}(?P<id>[0-9]+)-(?P<display_id>.+?)\\.html'
    _module = 'youtube_dl.extractor.rts'


class SpankBangPlaylistIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:[^/]+\\.)?spankbang\\.com/(?P<id>[\\da-z]+)/playlist/[^/]+'
    _module = 'youtube_dl.extractor.spankbang'


class MediasiteIE(LazyLoadExtractor):
    _VALID_URL = u'(?xi)https?://[^/]+/Mediasite/(?:Play|Showcase/(?:default|livebroadcast)/Presentation)/(?P<id>(?:[0-9a-f]{32,34}|[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12,14}))(?P<query>\\?[^#]+|)'
    _module = 'youtube_dl.extractor.mediasite'


class BRMediathekIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?br\\.de/mediathek/video/[^/?&#]*?-(?P<id>av:[0-9a-f]{24})'
    _module = 'youtube_dl.extractor.br'


class TeleBruxellesIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?:telebruxelles|bx1)\\.be/(?:[^/]+/)*(?P<id>[^/#?]+)'
    _module = 'youtube_dl.extractor.telebruxelles'


class LimelightMediaIE(LimelightBaseIE):
    _VALID_URL = u'(?x)\n                        (?:\n                            limelight:media:|\n                            https?://\n                                (?:\n                                    link\\.videoplatform\\.limelight\\.com/media/|\n                                    assets\\.delvenetworks\\.com/player/loader\\.swf\n                                )\n                                \\?.*?\\bmediaId=\n                        )\n                        (?P<id>[a-z0-9]{32})\n                    '
    _module = 'youtube_dl.extractor.limelight'


class FilmwebIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?filmweb\\.no/(?P<type>trailere|filmnytt)/article(?P<id>\\d+)\\.ece'
    _module = 'youtube_dl.extractor.filmweb'


class YoukuIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n        (?:\n            https?://(\n                (?:v|player)\\.youku\\.com/(?:v_show/id_|player\\.php/sid/)|\n                video\\.tudou\\.com/v/)|\n            youku:)\n        (?P<id>[A-Za-z0-9]+)(?:\\.html|/v\\.swf|)\n    '
    _module = 'youtube_dl.extractor.youku'


class LinkedInLearningIE(LinkedInLearningBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?linkedin\\.com/learning/(?P<course_slug>[^/]+)/(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.linkedin'


class PlayPlusTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?playplus\\.(?:com|tv)/VOD/(?P<project_id>[0-9]+)/(?P<id>[0-9a-f]{32})'
    _module = 'youtube_dl.extractor.playplustv'


class YnetIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:.+?\\.)?ynet\\.co\\.il/(?:.+?/)?0,7340,(?P<id>L(?:-[0-9]+)+),00\\.html'
    _module = 'youtube_dl.extractor.ynet'


class RaiPlayPlaylistIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?raiplay\\.it/programmi/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.rai'


class FusionIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?fusion\\.(?:net|tv)/video/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.fusion'


class RoxwelIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?roxwel\\.com/player/(?P<filename>.+?)(\\.|\\?|$)'
    _module = 'youtube_dl.extractor.roxwel'


class WeiboMobileIE(LazyLoadExtractor):
    _VALID_URL = u'https?://m\\.weibo\\.cn/status/(?P<id>[0-9]+)(\\?.+)?'
    _module = 'youtube_dl.extractor.weibo'


class Puls4IE(ProSiebenSat1BaseIE):
    _VALID_URL = u'https?://(?:www\\.)?puls4\\.com/(?P<id>[^?#&]+)'
    _module = 'youtube_dl.extractor.puls4'


class PlaywireIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:config|cdn)\\.playwire\\.com(?:/v2)?/(?P<publisher_id>\\d+)/(?:videos/v2|embed|config)/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.playwire'


class LcpPlayIE(ArkenaIE):
    _VALID_URL = u'https?://play\\.lcp\\.fr/embed/(?P<id>[^/]+)/(?P<account_id>[^/]+)/[^/]+/[^/]+'
    _module = 'youtube_dl.extractor.lcp'


class TeleQuebecLiveIE(LazyLoadExtractor):
    _VALID_URL = u'https?://zonevideo\\.telequebec\\.tv/(?P<id>endirect)'
    _module = 'youtube_dl.extractor.telequebec'


class CJSWIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?cjsw\\.com/program/(?P<program>[^/]+)/episode/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.cjsw'


class TOnlineIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?t-online\\.de/tv/(?:[^/]+/)*id_(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.tonline'


class VideofyMeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.videofy\\.me/.+?|p\\.videofy\\.me/v)/(?P<id>\\d+)(&|#|$)'
    _module = 'youtube_dl.extractor.videofyme'


class NetPlusIE(ZattooIE):
    _VALID_URL = u'https?://(?:www\\.)?netplus\\.tv/watch/(?P<channel>[^/]+?)/(?P<id>[0-9]+)[^/]+(?:/(?P<recid>[0-9]+))?'
    _module = 'youtube_dl.extractor.zattoo'


class NBCSportsVPlayerIE(LazyLoadExtractor):
    _VALID_URL = u'https?://vplayer\\.nbcsports\\.com/(?:[^/]+/)+(?P<id>[0-9a-zA-Z_]+)'
    _module = 'youtube_dl.extractor.nbc'


class SVTPlayIE(SVTPlayBaseIE):
    _VALID_URL = u'(?x)\n                    (?:\n                        svt:(?P<svt_id>[^/?#&]+)|\n                        https?://(?:www\\.)?(?:svtplay|oppetarkiv)\\.se/(?:video|klipp|kanaler)/(?P<id>[^/?#&]+)\n                    )\n                    '
    _module = 'youtube_dl.extractor.svt'


class HitboxLiveIE(HitboxIE):
    _VALID_URL = u'https?://(?:www\\.)?(?:hitbox|smashcast)\\.tv/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.hitbox'

    @classmethod
    def suitable(cls, url):
        return False if HitboxIE.suitable(url) else super(HitboxLiveIE, cls).suitable(url)


class KankanIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:.*?\\.)?kankan\\.com/.+?/(?P<id>\\d+)\\.shtml'
    _module = 'youtube_dl.extractor.kankan'


class NPORadioIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?npo\\.nl/radio/(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.npo'

    @classmethod
    def suitable(cls, url):
        return False if NPORadioFragmentIE.suitable(url) else super(NPORadioIE, cls).suitable(url)


class YoutubeRecommendedIE(YoutubeFeedsInfoExtractor):
    _VALID_URL = u'https?://(?:www\\.)?youtube\\.com/feed/recommended|:ytrec(?:ommended)?'
    _module = 'youtube_dl.extractor.youtube'


class VimeoLikesIE(LazyLoadExtractor):
    _VALID_URL = u'https://(?:www\\.)?vimeo\\.com/(?P<id>[^/]+)/likes/?(?:$|[?#]|sort:)'
    _module = 'youtube_dl.extractor.vimeo'


class BreakIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?break\\.com/video/(?P<display_id>[^/]+?)(?:-(?P<id>\\d+))?(?:[/?#&]|$)'
    _module = 'youtube_dl.extractor.breakcom'


class VidmeUserIE(VidmeListBaseIE):
    _VALID_URL = u'https?://vid\\.me/(?:e/)?(?P<id>[\\da-zA-Z_-]{6,})(?!/likes)(?:[^\\da-zA-Z_-]|$)'
    _module = 'youtube_dl.extractor.vidme'


class PlaytvakIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:.+?\\.)?(?:playtvak|idnes|lidovky|metro)\\.cz/.*\\?(?:c|idvideo)=(?P<id>[^&]+)'
    _module = 'youtube_dl.extractor.playtvak'


class WashingtonPostIE(LazyLoadExtractor):
    _VALID_URL = u'(?:washingtonpost:|https?://(?:www\\.)?washingtonpost\\.com/video/(?:[^/]+/)*)(?P<id>[\\da-f]{8}-[\\da-f]{4}-[\\da-f]{4}-[\\da-f]{4}-[\\da-f]{12})'
    _module = 'youtube_dl.extractor.washingtonpost'


class WalyTVIE(ZattooIE):
    _VALID_URL = u'https?://(?:www\\.)?player\\.waly\\.tv/watch/(?P<channel>[^/]+?)/(?P<id>[0-9]+)[^/]+(?:/(?P<recid>[0-9]+))?'
    _module = 'youtube_dl.extractor.zattoo'


class RadioBremenIE(LazyLoadExtractor):
    _VALID_URL = u'http?://(?:www\\.)?radiobremen\\.de/mediathek/(?:index\\.html)?\\?id=(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.radiobremen'


class VeohIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?veoh\\.com/(?:watch|embed|iphone/#_Watch)/(?P<id>(?:v|e|yapi-)[\\da-zA-Z]+)'
    _module = 'youtube_dl.extractor.veoh'


class PlayvidIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?playvid\\.com/watch(\\?v=|/)(?P<id>.+?)(?:#|$)'
    _module = 'youtube_dl.extractor.playvid'


class TMZArticleIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?tmz\\.com/\\d{4}/\\d{2}/\\d{2}/(?P<id>[^/]+)/?'
    _module = 'youtube_dl.extractor.tmz'


class LearnrIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?learnr\\.pro/view/video/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.learnr'


class RockstarGamesIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?rockstargames\\.com/videos(?:/video/|#?/?\\?.*\\bvideo=)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.rockstargames'


class VineIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?vine\\.co/(?:v|oembed)/(?P<id>\\w+)'
    _module = 'youtube_dl.extractor.vine'


class CBCOlympicsIE(LazyLoadExtractor):
    _VALID_URL = u'https?://olympics\\.cbc\\.ca/video/[^/]+/(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.cbc'


class FootyRoomIE(LazyLoadExtractor):
    _VALID_URL = u'https?://footyroom\\.com/matches/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.footyroom'


class NYTimesIE(NYTimesBaseIE):
    _VALID_URL = u'https?://(?:(?:www\\.)?nytimes\\.com/video/(?:[^/]+/)+?|graphics8\\.nytimes\\.com/bcvideo/\\d+(?:\\.\\d+)?/iframe/embed\\.html\\?videoId=)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.nytimes'


class XVideosIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:\n                            (?:www\\.)?xvideos\\.com/video|\n                            flashservice\\.xvideos\\.com/embedframe/|\n                            static-hw\\.xvideos\\.com/swf/xv-player\\.swf\\?.*?\\bid_video=\n                        )\n                        (?P<id>[0-9]+)\n                    '
    _module = 'youtube_dl.extractor.xvideos'


class VideoDetectiveIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?videodetective\\.com/[^/]+/[^/]+/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.videodetective'


class ViewsterIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?viewster\\.com/(?:serie|movie)/(?P<id>\\d+-\\d+-\\d+)'
    _module = 'youtube_dl.extractor.viewster'


class ArteTVFutureIE(ArteTVPlus7IE):
    _VALID_URL = u'https?://future\\.arte\\.tv/(?P<lang>fr|de|en|es)/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.arte'

    @classmethod
    def suitable(cls, url):
        return False if ArteTVPlaylistIE.suitable(url) else super(ArteTVPlus7IE, cls).suitable(url)


class NDTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:[^/]+\\.)?ndtv\\.com/(?:[^/]+/)*videos?/?(?:[^/]+/)*[^/?^&]+-(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.ndtv'


class MarkizaPageIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?:(?:[^/]+\\.)?markiza|tvnoviny)\\.sk/(?:[^/]+/)*(?P<id>\\d+)_'
    _module = 'youtube_dl.extractor.markiza'

    @classmethod
    def suitable(cls, url):
        return False if MarkizaIE.suitable(url) else super(MarkizaPageIE, cls).suitable(url)


class BiliBiliIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.|bangumi\\.|)bilibili\\.(?:tv|com)/(?:video/av|anime/(?P<anime_id>\\d+)/play#)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.bilibili'


class KanalPlayIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?kanal(?P<channel_id>5|9|11)play\\.se/(?:#!/)?(?:play/)?program/\\d+/video/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.kanalplay'


class CtsNewsIE(LazyLoadExtractor):
    _VALID_URL = u'https?://news\\.cts\\.com\\.tw/[a-z]+/[a-z]+/\\d+/(?P<id>\\d+)\\.html'
    _module = 'youtube_dl.extractor.ctsnews'


class FunnyOrDieIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?funnyordie\\.com/(?P<type>embed|articles|videos)/(?P<id>[0-9a-f]+)(?:$|[?#/])'
    _module = 'youtube_dl.extractor.funnyordie'


class RozhlasIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?prehravac\\.rozhlas\\.cz/audio/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.rozhlas'


class CCCPlaylistIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?media\\.ccc\\.de/c/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.ccc'


class USANetworkIE(AdobePassIE):
    _VALID_URL = u'https?://(?:www\\.)?usanetwork\\.com/(?:[^/]+/videos|movies)/(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.usanetwork'


class NerdCubedFeedIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?nerdcubed\\.co\\.uk/feed\\.json'
    _module = 'youtube_dl.extractor.nerdcubed'


class FranceTVInfoIE(FranceTVBaseInfoExtractor):
    _VALID_URL = u'https?://(?:www|mobile|france3-regions)\\.francetvinfo\\.fr/(?:[^/]+/)*(?P<id>[^/?#&.]+)'
    _module = 'youtube_dl.extractor.francetv'


class ViuBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.viu'


class ViuIE(ViuBaseIE):
    _VALID_URL = u'(?:viu:|https?://[^/]+\\.viu\\.com/[a-z]{2}/media/)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.viu'


class MailRuMusicSearchIE(MailRuMusicSearchBaseIE):
    _VALID_URL = u'https?://my\\.mail\\.ru/music/search/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.mailru'


class GolemIE(LazyLoadExtractor):
    _VALID_URL = u'^https?://video\\.golem\\.de/.+?/(?P<id>.+?)/'
    _module = 'youtube_dl.extractor.golem'


class WDRElefantIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)wdrmaus\\.de/elefantenseite/#(?P<id>.+)'
    _module = 'youtube_dl.extractor.wdr'


class BBCCoUkArticleIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?bbc\\.co\\.uk/programmes/articles/(?P<id>[a-zA-Z0-9]+)'
    _module = 'youtube_dl.extractor.bbc'


class MwaveMeetGreetIE(LazyLoadExtractor):
    _VALID_URL = u'https?://mwave\\.interest\\.me/(?:[^/]+/)?meetgreet/view/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.mwave'


class SinaIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)https?://(?:.*?\\.)?video\\.sina\\.com\\.cn/\n                        (?:\n                            (?:view/|.*\\#)(?P<video_id>\\d+)|\n                            .+?/(?P<pseudo_id>[^/?#]+)(?:\\.s?html)|\n                            # This is used by external sites like Weibo\n                            api/sinawebApi/outplay.php/(?P<token>.+?)\\.swf\n                        )\n                  '
    _module = 'youtube_dl.extractor.sina'


class SohuIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?P<mytv>my\\.)?tv\\.sohu\\.com/.+?/(?(mytv)|n)(?P<id>\\d+)\\.shtml.*?'
    _module = 'youtube_dl.extractor.sohu'


class BravoTVIE(AdobePassIE):
    _VALID_URL = u'https?://(?:www\\.)?bravotv\\.com/(?:[^/]+/)+(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.bravotv'


class CinchcastIE(LazyLoadExtractor):
    _VALID_URL = u'https?://player\\.cinchcast\\.com/.*?(?:assetId|show_id)=(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.cinchcast'


class YoutubePlaylistIE(YoutubePlaylistBaseInfoExtractor):
    _VALID_URL = u'(?x)(?:\n                        (?:https?://)?\n                        (?:\\w+\\.)?\n                        (?:\n                            (?:\n                                youtube\\.com|\n                                invidio\\.us\n                            )\n                            /\n                            (?:\n                               (?:course|view_play_list|my_playlists|artist|playlist|watch|embed/(?:videoseries|[0-9A-Za-z_-]{11}))\n                               \\? (?:.*?[&;])*? (?:p|a|list)=\n                            |  p/\n                            )|\n                            youtu\\.be/[0-9A-Za-z_-]{11}\\?.*?\\blist=\n                        )\n                        (\n                            (?:PL|LL|EC|UU|FL|RD|UL|TL|OLAK5uy_)?[0-9A-Za-z-_]{10,}\n                            # Top tracks, they can also include dots\n                            |(?:MC)[\\w\\.]*\n                        )\n                        .*\n                     |\n                        ((?:PL|LL|EC|UU|FL|RD|UL|TL|OLAK5uy_)[0-9A-Za-z-_]{10,})\n                     )'
    _module = 'youtube_dl.extractor.youtube'


class YoutubeWatchLaterIE(YoutubePlaylistIE):
    _VALID_URL = u'https?://(?:www\\.)?youtube\\.com/(?:feed/watch_later|(?:playlist|watch)\\?(?:.+&)?list=WL)|:ytwatchlater'
    _module = 'youtube_dl.extractor.youtube'


class LibsynIE(LazyLoadExtractor):
    _VALID_URL = u'(?P<mainurl>https?://html5-player\\.libsyn\\.com/embed/episode/id/(?P<id>[0-9]+))'
    _module = 'youtube_dl.extractor.libsyn'


class KrasViewIE(LazyLoadExtractor):
    _VALID_URL = u'https?://krasview\\.ru/(?:video|embed)/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.krasview'


class MediasiteCatalogIE(LazyLoadExtractor):
    _VALID_URL = u'(?xi)\n                        (?P<url>https?://[^/]+/Mediasite)\n                        /Catalog/Full/\n                        (?P<catalog_id>(?:[0-9a-f]{32,34}|[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12,14}))\n                        (?:\n                            /(?P<current_folder_id>(?:[0-9a-f]{32,34}|[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12,14}))\n                            /(?P<root_dynamic_folder_id>(?:[0-9a-f]{32,34}|[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12,14}))\n                        )?\n                    '
    _module = 'youtube_dl.extractor.mediasite'


class KickStarterIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?kickstarter\\.com/projects/(?P<id>[^/]*)/.*'
    _module = 'youtube_dl.extractor.kickstarter'


class EngadgetIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?engadget\\.com/video/(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.engadget'


class LocalNews8IE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?localnews8\\.com/(?:[^/]+/)*(?P<display_id>[^/]+)/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.localnews8'


class DailymotionUserIE(DailymotionBaseInfoExtractor):
    _VALID_URL = u'https?://(?:www\\.)?dailymotion\\.[a-z]{2,3}/(?!(?:embed|swf|#|video|playlist)/)(?:(?:old/)?user/)?(?P<user>[^/]+)'
    _module = 'youtube_dl.extractor.dailymotion'


class InfoQIE(BokeCCBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?infoq\\.com/(?:[^/]+/)+(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.infoq'


class OdaTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?odatv\\.com/(?:mob|vid)_video\\.php\\?.*\\bid=(?P<id>[^&]+)'
    _module = 'youtube_dl.extractor.odatv'


class YoutubeIE(YoutubeBaseInfoExtractor):
    _VALID_URL = u'(?x)^\n                     (\n                         (?:https?://|//)                                    # http(s):// or protocol-independent URL\n                         (?:(?:(?:(?:\\w+\\.)?[yY][oO][uU][tT][uU][bB][eE](?:-nocookie)?\\.com/|\n                            (?:www\\.)?deturl\\.com/www\\.youtube\\.com/|\n                            (?:www\\.)?pwnyoutube\\.com/|\n                            (?:www\\.)?hooktube\\.com/|\n                            (?:www\\.)?yourepeat\\.com/|\n                            tube\\.majestyc\\.net/|\n                            (?:(?:www|dev)\\.)?invidio\\.us/|\n                            (?:www\\.)?invidiou\\.sh/|\n                            (?:www\\.)?invidious\\.snopyta\\.org/|\n                            (?:www\\.)?invidious\\.kabi\\.tk/|\n                            (?:www\\.)?vid\\.wxzm\\.sx/|\n                            youtube\\.googleapis\\.com/)                        # the various hostnames, with wildcard subdomains\n                         (?:.*?\\#/)?                                          # handle anchor (#/) redirect urls\n                         (?:                                                  # the various things that can precede the ID:\n                             (?:(?:v|embed|e)/(?!videoseries))                # v/ or embed/ or e/\n                             |(?:                                             # or the v= param in all its forms\n                                 (?:(?:watch|movie)(?:_popup)?(?:\\.php)?/?)?  # preceding watch(_popup|.php) or nothing (like /?v=xxxx)\n                                 (?:\\?|\\#!?)                                  # the params delimiter ? or # or #!\n                                 (?:.*?[&;])??                                # any other preceding param (like /?s=tuff&v=xxxx or ?s=tuff&amp;v=V36LpHqtcDY)\n                                 v=\n                             )\n                         ))\n                         |(?:\n                            youtu\\.be|                                        # just youtu.be/xxxx\n                            vid\\.plus|                                        # or vid.plus/xxxx\n                            zwearz\\.com/watch|                                # or zwearz.com/watch/xxxx\n                         )/\n                         |(?:www\\.)?cleanvideosearch\\.com/media/action/yt/watch\\?videoId=\n                         )\n                     )?                                                       # all until now is optional -> you can pass the naked ID\n                     ([0-9A-Za-z_-]{11})                                      # here is it! the YouTube video ID\n                     (?!.*?\\blist=\n                        (?:\n                            (?:PL|LL|EC|UU|FL|RD|UL|TL|OLAK5uy_)[0-9A-Za-z-_]{10,}|                                  # combined list/video URLs are handled by the playlist IE\n                            WL                                                # WL are handled by the watch later IE\n                        )\n                     )\n                     (?(1).+)?                                                # if we found the ID, everything can follow\n                     $'
    _module = 'youtube_dl.extractor.youtube'


class UstudioEmbedIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:app|embed)\\.)?ustudio\\.com/embed/(?P<uid>[^/]+)/(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.ustudio'


class UplynkIE(LazyLoadExtractor):
    _VALID_URL = u'https?://.*?\\.uplynk\\.com/(?P<path>ext/[0-9a-f]{32}/(?P<external_id>[^/?&]+)|(?P<id>[0-9a-f]{32}))\\.(?:m3u8|json)(?:.*?\\bpbs=(?P<session_id>[^&]+))?'
    _module = 'youtube_dl.extractor.uplynk'


class UplynkPreplayIE(UplynkIE):
    _VALID_URL = u'https?://.*?\\.uplynk\\.com/preplay2?/(?P<path>ext/[0-9a-f]{32}/(?P<external_id>[^/?&]+)|(?P<id>[0-9a-f]{32}))\\.json'
    _module = 'youtube_dl.extractor.uplynk'


class YoutubeFavouritesIE(YoutubeBaseInfoExtractor):
    _VALID_URL = u'https?://(?:www\\.)?youtube\\.com/my_favorites|:ytfav(?:ou?rites)?'
    _module = 'youtube_dl.extractor.youtube'


class VGTVIE(XstreamIE):
    _VALID_URL = u'(?x)\n                    (?:https?://(?:www\\.)?\n                    (?P<host>\n                        aftenposten.no/webtv|www.aftonbladet.se/tv|fvn.no/fvntv|vgtv.no|aftenbladet.no/tv|bt.no/tv|ap.vgtv.no/webtv|tv.aftonbladet.se/abtv\n                    )\n                    /?\n                    (?:\n                        (?:\\#!/)?(?:video|live)/|\n                        embed?.*id=|\n                        a(?:rticles)?/\n                    )|\n                    (?P<appname>\n                        vgtv|fvntv|satv|bttv|aptv|abtv\n                    ):)\n                    (?P<id>\\d+)\n                    '
    _module = 'youtube_dl.extractor.vgtv'


class AcademicEarthCourseIE(LazyLoadExtractor):
    _VALID_URL = u'^https?://(?:www\\.)?academicearth\\.org/playlists/(?P<id>[^?#/]+)'
    _module = 'youtube_dl.extractor.academicearth'


class VVVVIDIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?vvvvid\\.it/#!(?:show|anime|film|series)/(?P<show_id>\\d+)/[^/]+/(?P<season_id>\\d+)/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.vvvvid'


class MassengeschmackTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?massengeschmack\\.tv/play/(?P<id>[^?&#]+)'
    _module = 'youtube_dl.extractor.massengeschmacktv'


class TruTVIE(TurnerBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?trutv\\.com/(?:shows|full-episodes)/(?P<series_slug>[0-9A-Za-z-]+)/(?:videos/(?P<clip_slug>[0-9A-Za-z-]+)|(?P<id>\\d+))'
    _module = 'youtube_dl.extractor.trutv'


class XuiteIE(LazyLoadExtractor):
    _VALID_URL = u'https?://vlog\\.xuite\\.net/(?:play|embed)/(?P<id>(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?)'
    _module = 'youtube_dl.extractor.xuite'


class FranceInterIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?franceinter\\.fr/emissions/(?P<id>[^?#]+)'
    _module = 'youtube_dl.extractor.franceinter'


class CrunchyrollIE(CrunchyrollBaseIE, VRVIE):
    _VALID_URL = u'https?://(?:(?P<prefix>www|m)\\.)?(?P<url>crunchyroll\\.(?:com|fr)/(?:media(?:-|/\\?id=)|(?:[^/]*/){1,2}[^/?&]*?)(?P<video_id>[0-9]+))(?:[/?&]|$)'
    _module = 'youtube_dl.extractor.crunchyroll'


class NetEaseMusicMvIE(NetEaseMusicBaseIE):
    _VALID_URL = u'https?://music\\.163\\.com/(#/)?mv\\?id=(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.neteasemusic'


class RTVEInfantilIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?rtve\\.es/infantil/serie/(?P<show>[^/]*)/video/(?P<short_title>[^/]*)/(?P<id>[0-9]+)/'
    _module = 'youtube_dl.extractor.rtve'


class SmotriCommunityIE(LazyLoadExtractor):
    _VALID_URL = u"https?://(?:www\\.)?smotri\\.com/community/video/(?P<id>[0-9A-Za-z_\\'-]+)"
    _module = 'youtube_dl.extractor.smotri'


class FunkMixIE(FunkBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?funk\\.net/mix/(?P<id>[^/]+)/(?P<alias>[^/?#&]+)'
    _module = 'youtube_dl.extractor.funk'


class CamWithHerIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?camwithher\\.tv/view_video\\.php\\?.*\\bviewkey=(?P<id>\\w+)'
    _module = 'youtube_dl.extractor.camwithher'


class ORFIPTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://iptv\\.orf\\.at/(?:#/)?stories/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.orf'


class FilmOnIE(LazyLoadExtractor):
    _VALID_URL = u'(?:https?://(?:www\\.)?filmon\\.com/vod/view/|filmon:)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.filmon'


class NickRuIE(MTVServicesInfoExtractor):
    _VALID_URL = u'https?://(?:www\\.)nickelodeon\\.(?:ru|fr|es|pt|ro|hu|com\\.tr)/[^/]+/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.nick'


class RDSIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?rds\\.ca/vid(?:[e\xe9]|%C3%A9)os/(?:[^/]+/)*(?P<id>[^/]+)-\\d+\\.\\d+'
    _module = 'youtube_dl.extractor.rds'


class SonyLIVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?sonyliv\\.com/details/[^/]+/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.sonyliv'


class ScrippsNetworksWatchIE(AWSIE):
    _VALID_URL = u'(?x)\n                    https?://\n                        watch\\.\n                        (?P<site>geniuskitchen)\\.com/\n                        (?:\n                            player\\.[A-Z0-9]+\\.html\\#|\n                            show/(?:[^/]+/){2}|\n                            player/\n                        )\n                        (?P<id>\\d+)\n                    '
    _module = 'youtube_dl.extractor.scrippsnetworks'


class FC2IE(LazyLoadExtractor):
    _VALID_URL = u'^(?:https?://video\\.fc2\\.com/(?:[^/]+/)*content/|fc2:)(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.fc2'


class TwitchProfileIE(TwitchPlaylistBaseIE):
    _VALID_URL = u'https?://(?:(?:www|go|m)\\.)?twitch\\.tv/(?P<id>[^/]+)/profile/?(?:\\#.*)?$'
    _module = 'youtube_dl.extractor.twitch'


class CTVNewsIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:.+?\\.)?ctvnews\\.ca/(?:video\\?(?:clip|playlist|bin)Id=|.*?)(?P<id>[0-9.]+)'
    _module = 'youtube_dl.extractor.ctvnews'


class MyVidsterIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?myvidster\\.com/video/(?P<id>\\d+)/'
    _module = 'youtube_dl.extractor.myvidster'


class BBVTVIE(ZattooIE):
    _VALID_URL = u'https?://(?:www\\.)?bbv\\-tv\\.net/watch/(?P<channel>[^/]+?)/(?P<id>[0-9]+)[^/]+(?:/(?P<recid>[0-9]+))?'
    _module = 'youtube_dl.extractor.zattoo'


class ImgurGalleryIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:i\\.)?imgur\\.com/(?:gallery|(?:t(?:opic)?|r)/[^/]+)/(?P<id>[a-zA-Z0-9]+)'
    _module = 'youtube_dl.extractor.imgur'


class ImgurAlbumIE(ImgurGalleryIE):
    _VALID_URL = u'https?://(?:i\\.)?imgur\\.com/a/(?P<id>[a-zA-Z0-9]+)'
    _module = 'youtube_dl.extractor.imgur'


class HuffPostIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n        https?://(embed\\.)?live\\.huffingtonpost\\.com/\n        (?:\n            r/segment/[^/]+/|\n            HPLEmbedPlayer/\\?segmentId=\n        )\n        (?P<id>[0-9a-f]+)'
    _module = 'youtube_dl.extractor.huffpost'


class HungamaIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:www\\.)?hungama\\.com/\n                        (?:\n                            (?:video|movie)/[^/]+/|\n                            tv-show/(?:[^/]+/){2}\\d+/episode/[^/]+/\n                        )\n                        (?P<id>\\d+)\n                    '
    _module = 'youtube_dl.extractor.hungama'


class CloudTimeIE(NovaMovIE):
    _VALID_URL = u'(?x)\n                            http://\n                                (?:\n                                    (?:www\\.)?cloudtime\\.to/(?:file|video|mobile/\\#/videos)/|\n                                    (?:(?:embed|www)\\.)cloudtime\\.to/embed(?:\\.php|/)?\\?(?:.*?&)?\\bv=\n                                )\n                                (?P<id>[a-z\\d]{13})\n                            '
    _module = 'youtube_dl.extractor.novamov'


class BloombergIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?bloomberg\\.com/(?:[^/]+/)*(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.bloomberg'


class KuwoChartIE(LazyLoadExtractor):
    _VALID_URL = u'https?://yinyue\\.kuwo\\.cn/billboard_(?P<id>[^.]+).htm'
    _module = 'youtube_dl.extractor.kuwo'


class YoutubeTruncatedURLIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n        (?:https?://)?\n        (?:\\w+\\.)?[yY][oO][uU][tT][uU][bB][eE](?:-nocookie)?\\.com/\n        (?:watch\\?(?:\n            feature=[a-z_]+|\n            annotation_id=annotation_[^&]+|\n            x-yt-cl=[0-9]+|\n            hl=[^&]*|\n            t=[0-9]+\n        )?\n        |\n            attribution_link\\?a=[^&]+\n        )\n        $\n    '
    _module = 'youtube_dl.extractor.youtube'


class TeacherTubeUserIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?teachertube\\.com/(user/profile|collection)/(?P<user>[0-9a-zA-Z]+)/?'
    _module = 'youtube_dl.extractor.teachertube'


class KetnetIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?ketnet\\.be/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.ketnet'


class NDREmbedIE(NDREmbedBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?ndr\\.de/(?:[^/]+/)*(?P<id>[\\da-z]+)-(?:player|externalPlayer)\\.html'
    _module = 'youtube_dl.extractor.ndr'


class YourPornIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?:yourporn\\.sexy|sxyprn\\.com)/post/(?P<id>[^/?#&.]+)'
    _module = 'youtube_dl.extractor.yourporn'


class ShahidIE(ShahidBaseIE):
    _VALID_URL = u'https?://shahid\\.mbc\\.net/ar/(?:serie|show|movie)s/[^/]+/(?P<type>episode|clip|movie)-(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.shahid'


class ViuPlaylistIE(ViuBaseIE):
    _VALID_URL = u'https?://www\\.viu\\.com/[^/]+/listing/playlist-(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.viu'


class RottenTomatoesIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?rottentomatoes\\.com/m/[^/]+/trailers/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.rottentomatoes'


class BpbIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?bpb\\.de/mediathek/(?P<id>[0-9]+)/'
    _module = 'youtube_dl.extractor.bpb'


class SverigesRadioPublicationIE(SverigesRadioBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?sverigesradio\\.se/sida/(?:artikel|gruppsida)\\.aspx\\?.*?\\bartikel=(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.sverigesradio'


class MoeVideoIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n        https?://(?P<host>(?:www\\.)?\n        (?:(?:moevideo|playreplay|videochart)\\.net|thesame\\.tv))/\n        (?:video|framevideo|embed)/(?P<id>[0-9a-z]+\\.[0-9A-Za-z]+)'
    _module = 'youtube_dl.extractor.moevideo'


class ArteTVPlaylistIE(ArteTVBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?arte\\.tv/guide/(?P<lang>fr|de|en|es)/[^#]*#collection/(?P<id>PL-\\d+)'
    _module = 'youtube_dl.extractor.arte'


class VKIE(VKBaseIE):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:\n                            (?:\n                                (?:(?:m|new)\\.)?vk\\.com/video_|\n                                (?:www\\.)?daxab.com/\n                            )\n                            ext\\.php\\?(?P<embed_query>.*?\\boid=(?P<oid>-?\\d+).*?\\bid=(?P<id>\\d+).*)|\n                            (?:\n                                (?:(?:m|new)\\.)?vk\\.com/(?:.+?\\?.*?z=)?video|\n                                (?:www\\.)?daxab.com/embed/\n                            )\n                            (?P<videoid>-?\\d+_\\d+)(?:.*\\blist=(?P<list_id>[\\da-f]+))?\n                        )\n                    '
    _module = 'youtube_dl.extractor.vk'


class ExpoTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?expotv\\.com/videos/[^?#]*/(?P<id>[0-9]+)($|[?#])'
    _module = 'youtube_dl.extractor.expotv'


class KuwoCategoryIE(LazyLoadExtractor):
    _VALID_URL = u'https?://yinyue\\.kuwo\\.cn/yy/cinfo_(?P<id>\\d+?).htm'
    _module = 'youtube_dl.extractor.kuwo'


class MiaoPaiIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?miaopai\\.com/show/(?P<id>[-A-Za-z0-9~_]+)'
    _module = 'youtube_dl.extractor.miaopai'


class YesJapanIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?yesjapan\\.com/video/(?P<slug>[A-Za-z0-9\\-]*)_(?P<id>[A-Za-z0-9]+)\\.html'
    _module = 'youtube_dl.extractor.yesjapan'


class AENetworksIE(AENetworksBaseIE):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:www\\.)?\n                        (?P<domain>\n                            (?:history(?:vault)?|aetv|mylifetime|lifetimemovieclub)\\.com|\n                            fyi\\.tv\n                        )/\n                        (?:\n                            shows/(?P<show_path>[^/]+(?:/[^/]+){0,2})|\n                            movies/(?P<movie_display_id>[^/]+)(?:/full-movie)?|\n                            specials/(?P<special_display_id>[^/]+)/(?:full-special|preview-)|\n                            collections/[^/]+/(?P<collection_display_id>[^/]+)\n                        )\n                    '
    _module = 'youtube_dl.extractor.aenetworks'


class RayWenderlichCourseIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:\n                            videos\\.raywenderlich\\.com/courses|\n                            (?:www\\.)?raywenderlich\\.com\n                        )/\n                        (?P<id>[^/]+)\n                    '
    _module = 'youtube_dl.extractor.raywenderlich'

    @classmethod
    def suitable(cls, url):
        return False if RayWenderlichIE.suitable(url) else super(
            RayWenderlichCourseIE, cls).suitable(url)


class MegaphoneIE(LazyLoadExtractor):
    _VALID_URL = u'https://player\\.megaphone\\.fm/(?P<id>[A-Z0-9]+)'
    _module = 'youtube_dl.extractor.megaphone'


class VimeoUserIE(VimeoChannelIE):
    _VALID_URL = u'https://vimeo\\.com/(?!(?:[0-9]+|watchlater)(?:$|[?#/]))(?P<name>[^/]+)(?:/videos|[#?]|$)'
    _module = 'youtube_dl.extractor.vimeo'


class SoundcloudIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)^(?:https?://)?\n                    (?:(?:(?:www\\.|m\\.)?soundcloud\\.com/\n                            (?!stations/track)\n                            (?P<uploader>[\\w\\d-]+)/\n                            (?!(?:tracks|albums|sets(?:/.+?)?|reposts|likes|spotlight)/?(?:$|[?#]))\n                            (?P<title>[\\w\\d-]+)/?\n                            (?P<token>[^?]+?)?(?:[?].*)?$)\n                       |(?:api\\.soundcloud\\.com/tracks/(?P<track_id>\\d+)\n                          (?:/?\\?secret_token=(?P<secret_token>[^&]+))?)\n                       |(?P<player>(?:w|player|p.)\\.soundcloud\\.com/player/?.*?url=.*)\n                    )\n                    '
    _module = 'youtube_dl.extractor.soundcloud'


class SoundcloudPlaylistBaseIE(SoundcloudIE):
    _VALID_URL = u'(?x)^(?:https?://)?\n                    (?:(?:(?:www\\.|m\\.)?soundcloud\\.com/\n                            (?!stations/track)\n                            (?P<uploader>[\\w\\d-]+)/\n                            (?!(?:tracks|albums|sets(?:/.+?)?|reposts|likes|spotlight)/?(?:$|[?#]))\n                            (?P<title>[\\w\\d-]+)/?\n                            (?P<token>[^?]+?)?(?:[?].*)?$)\n                       |(?:api\\.soundcloud\\.com/tracks/(?P<track_id>\\d+)\n                          (?:/?\\?secret_token=(?P<secret_token>[^&]+))?)\n                       |(?P<player>(?:w|player|p.)\\.soundcloud\\.com/player/?.*?url=.*)\n                    )\n                    '
    _module = 'youtube_dl.extractor.soundcloud'


class SoundcloudPagedPlaylistBaseIE(SoundcloudPlaylistBaseIE):
    _VALID_URL = u'(?x)^(?:https?://)?\n                    (?:(?:(?:www\\.|m\\.)?soundcloud\\.com/\n                            (?!stations/track)\n                            (?P<uploader>[\\w\\d-]+)/\n                            (?!(?:tracks|albums|sets(?:/.+?)?|reposts|likes|spotlight)/?(?:$|[?#]))\n                            (?P<title>[\\w\\d-]+)/?\n                            (?P<token>[^?]+?)?(?:[?].*)?$)\n                       |(?:api\\.soundcloud\\.com/tracks/(?P<track_id>\\d+)\n                          (?:/?\\?secret_token=(?P<secret_token>[^&]+))?)\n                       |(?P<player>(?:w|player|p.)\\.soundcloud\\.com/player/?.*?url=.*)\n                    )\n                    '
    _module = 'youtube_dl.extractor.soundcloud'


class SoundcloudSearchIE(LazyLoadSearchExtractor, SoundcloudIE):
    _VALID_URL = u'(?x)^(?:https?://)?\n                    (?:(?:(?:www\\.|m\\.)?soundcloud\\.com/\n                            (?!stations/track)\n                            (?P<uploader>[\\w\\d-]+)/\n                            (?!(?:tracks|albums|sets(?:/.+?)?|reposts|likes|spotlight)/?(?:$|[?#]))\n                            (?P<title>[\\w\\d-]+)/?\n                            (?P<token>[^?]+?)?(?:[?].*)?$)\n                       |(?:api\\.soundcloud\\.com/tracks/(?P<track_id>\\d+)\n                          (?:/?\\?secret_token=(?P<secret_token>[^&]+))?)\n                       |(?P<player>(?:w|player|p.)\\.soundcloud\\.com/player/?.*?url=.*)\n                    )\n                    '
    _module = 'youtube_dl.extractor.soundcloud'

    @classmethod
    def suitable(cls, url):
        return re.match(cls._make_valid_url(), url) is not None

    @classmethod
    def _make_valid_url(cls):
        return u'scsearch(?P<prefix>|[1-9][0-9]*|all):(?P<query>[\\s\\S]+)'


class SoundcloudUserIE(SoundcloudPagedPlaylistBaseIE):
    _VALID_URL = u'(?x)\n                        https?://\n                            (?:(?:www|m)\\.)?soundcloud\\.com/\n                            (?P<user>[^/]+)\n                            (?:/\n                                (?P<rsrc>tracks|albums|sets|reposts|likes|spotlight)\n                            )?\n                            /?(?:[?#].*)?$\n                    '
    _module = 'youtube_dl.extractor.soundcloud'


class SoundcloudSetIE(SoundcloudPlaylistBaseIE):
    _VALID_URL = u'https?://(?:(?:www|m)\\.)?soundcloud\\.com/(?P<uploader>[\\w\\d-]+)/sets/(?P<slug_title>[\\w\\d-]+)(?:/(?P<token>[^?/]+))?'
    _module = 'youtube_dl.extractor.soundcloud'


class SoundcloudTrackStationIE(SoundcloudPagedPlaylistBaseIE):
    _VALID_URL = u'https?://(?:(?:www|m)\\.)?soundcloud\\.com/stations/track/[^/]+/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.soundcloud'


class SoundcloudPlaylistIE(SoundcloudPlaylistBaseIE):
    _VALID_URL = u'https?://api\\.soundcloud\\.com/playlists/(?P<id>[0-9]+)(?:/?\\?secret_token=(?P<token>[^&]+?))?$'
    _module = 'youtube_dl.extractor.soundcloud'


class TagesschauPlayerIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?tagesschau\\.de/multimedia/(?P<kind>audio|video)/(?P=kind)-(?P<id>\\d+)~player(?:_[^/?#&]+)?\\.html'
    _module = 'youtube_dl.extractor.tagesschau'


class ATTTechChannelIE(LazyLoadExtractor):
    _VALID_URL = u'https?://techchannel\\.att\\.com/play-video\\.cfm/([^/]+/)*(?P<id>.+)'
    _module = 'youtube_dl.extractor.atttechchannel'


class BellatorIE(MTVServicesInfoExtractor):
    _VALID_URL = u'https?://(?:www\\.)?bellator\\.com/[^/]+/[\\da-z]{6}(?:[/?#&]|$)'
    _module = 'youtube_dl.extractor.spike'


class VLiveIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:www|m)\\.)?vlive\\.tv/video/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.vlive'

    @classmethod
    def suitable(cls, url):
        return False if VLivePlaylistIE.suitable(url) else super(VLiveIE, cls).suitable(url)


class EbaumsWorldIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?ebaumsworld\\.com/videos/[^/]+/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.ebaumsworld'


class TeamcocoIE(TurnerBaseIE):
    _VALID_URL = u'https?://(?:\\w+\\.)?teamcoco\\.com/(?P<id>([^/]+/)*[^/?#]+)'
    _module = 'youtube_dl.extractor.teamcoco'


class NationalGeographicVideoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://video\\.nationalgeographic\\.com/.*?'
    _module = 'youtube_dl.extractor.nationalgeographic'


class CliphunterIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)https?://(?:www\\.)?cliphunter\\.com/w/\n        (?P<id>[0-9]+)/\n        (?P<seo>.+?)(?:$|[#\\?])\n    '
    _module = 'youtube_dl.extractor.cliphunter'


class R7IE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                        https?://\n                        (?:\n                            (?:[a-zA-Z]+)\\.r7\\.com(?:/[^/]+)+/idmedia/|\n                            noticias\\.r7\\.com(?:/[^/]+)+/[^/]+-|\n                            player\\.r7\\.com/video/i/\n                        )\n                        (?P<id>[\\da-f]{24})\n                    '
    _module = 'youtube_dl.extractor.r7'


class UnistraIE(LazyLoadExtractor):
    _VALID_URL = u'https?://utv\\.unistra\\.fr/(?:index|video)\\.php\\?id_video\\=(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.unistra'


class KeekIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?keek\\.com/keek/(?P<id>\\w+)'
    _module = 'youtube_dl.extractor.keek'


class YapFilesIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:www|api)\\.)?yapfiles\\.ru/get_player/*\\?.*?\\bv=(?P<id>\\w+)'
    _module = 'youtube_dl.extractor.yapfiles'


class NPODataMidEmbedIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.npo'


class SchoolTVIE(NPODataMidEmbedIE):
    _VALID_URL = u'https?://(?:www\\.)?schooltv\\.nl/video/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.npo'


class AfreecaTVIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:\n                            (?:(?:live|afbbs|www)\\.)?afreeca(?:tv)?\\.com(?::\\d+)?\n                            (?:\n                                /app/(?:index|read_ucc_bbs)\\.cgi|\n                                /player/[Pp]layer\\.(?:swf|html)\n                            )\\?.*?\\bnTitleNo=|\n                            vod\\.afreecatv\\.com/PLAYER/STATION/\n                        )\n                        (?P<id>\\d+)\n                    '
    _module = 'youtube_dl.extractor.afreecatv'


class NTVRuIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?ntv\\.ru/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.ntvru'


class RMCDecouverteIE(LazyLoadExtractor):
    _VALID_URL = u'https?://rmcdecouverte\\.bfmtv\\.com/(?:(?:[^/]+/)*program_(?P<id>\\d+)|(?P<live_id>mediaplayer-direct))'
    _module = 'youtube_dl.extractor.rmcdecouverte'


class TuneInShortenerIE(LazyLoadExtractor):
    _VALID_URL = u'https?://tun\\.in/(?P<id>[A-Za-z0-9]+)'
    _module = 'youtube_dl.extractor.tunein'


class DaumListIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.daum'


class DaumPlaylistIE(DaumListIE):
    _VALID_URL = u'https?://(?:m\\.)?tvpot\\.daum\\.net/mypot/(?:View\\.do|Top\\.tv)\\?.*?playlistid=(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.daum'

    @classmethod
    def suitable(cls, url):
        return False if DaumUserIE.suitable(url) else super(DaumPlaylistIE, cls).suitable(url)


class QQMusicToplistIE(QQPlaylistBaseIE):
    _VALID_URL = u'https?://y\\.qq\\.com/n/yqq/toplist/(?P<id>[0-9]+)\\.html'
    _module = 'youtube_dl.extractor.qqmusic'


class ORFTVthekIE(LazyLoadExtractor):
    _VALID_URL = u'https?://tvthek\\.orf\\.at/(?:[^/]+/)+(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.orf'


class WistiaIE(LazyLoadExtractor):
    _VALID_URL = u'(?:wistia:|https?://(?:fast\\.)?wistia\\.(?:net|com)/embed/(?:iframe|medias)/)(?P<id>[a-z0-9]+)'
    _module = 'youtube_dl.extractor.wistia'


class GfycatIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?gfycat\\.com/(?:ifr/|gifs/detail/)?(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.gfycat'


class NJPWWorldIE(LazyLoadExtractor):
    _VALID_URL = u'https?://njpwworld\\.com/p/(?P<id>[a-z0-9_]+)'
    _module = 'youtube_dl.extractor.njpwworld'


class MixcloudPlaylistBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.mixcloud'


class MixcloudStreamIE(MixcloudPlaylistBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?mixcloud\\.com/(?P<id>[^/]+)/stream/?$'
    _module = 'youtube_dl.extractor.mixcloud'


class LiveLeakEmbedIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?liveleak\\.com/ll_embed\\?.*?\\b(?P<kind>[ift])=(?P<id>[\\w_]+)'
    _module = 'youtube_dl.extractor.liveleak'


class TwitchClipsIE(TwitchBaseIE):
    _VALID_URL = u'https?://(?:clips\\.twitch\\.tv/(?:[^/]+/)*|(?:www\\.)?twitch\\.tv/[^/]+/clip/)(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.twitch'


class StreetVoiceIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:.+?\\.)?streetvoice\\.com/[^/]+/songs/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.streetvoice'


class SyfyIE(AdobePassIE):
    _VALID_URL = u'https?://(?:www\\.)?syfy\\.com/(?:[^/]+/)?videos/(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.syfy'


class RutubeIE(RutubeBaseIE):
    _VALID_URL = u'https?://rutube\\.ru/(?:video|(?:play/)?embed)/(?P<id>[\\da-z]{32})'
    _module = 'youtube_dl.extractor.rutube'

    @classmethod
    def suitable(cls, url):
        return False if RutubePlaylistIE.suitable(url) else super(RutubeIE, cls).suitable(url)


class YoutubeUserIE(YoutubeChannelIE):
    _VALID_URL = u'(?:(?:https?://(?:\\w+\\.)?youtube\\.com/(?:(?P<user>user|c)/)?(?!(?:attribution_link|watch|results|shared)(?:$|[^a-z_A-Z0-9-])))|ytuser:)(?!feed/)(?P<id>[A-Za-z0-9_-]+)'
    _module = 'youtube_dl.extractor.youtube'

    @classmethod
    def suitable(cls, url):
        # Don't return True if the url can be extracted with other youtube
        # extractor, the regex would is too permissive and it would match.
        other_yt_ies = iter(klass for (name, klass) in globals().items() if name.startswith('Youtube') and name.endswith('IE') and klass is not cls)
        if any(ie.suitable(url) for ie in other_yt_ies):
            return False
        else:
            return super(YoutubeUserIE, cls).suitable(url)


class NickDeIE(MTVServicesInfoExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?P<host>nick\\.(?:de|com\\.pl|ch)|nickelodeon\\.(?:nl|be|at|dk|no|se))/[^/]+/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.nick'


class NintendoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?nintendo\\.com/games/detail/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.nintendo'


class QuicklineLiveIE(QuicklineBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?mobiltv\\.quickline\\.com/watch/(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.zattoo'

    @classmethod
    def suitable(cls, url):
        return False if QuicklineIE.suitable(url) else super(QuicklineLiveIE, cls).suitable(url)


class HBOIE(HBOBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?hbo\\.com/(?:video|embed)(?:/[^/]+)*/(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.hbo'


class UdemyCourseIE(UdemyIE):
    _VALID_URL = u'https?://(?:[^/]+\\.)?udemy\\.com/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.udemy'

    @classmethod
    def suitable(cls, url):
        return False if UdemyIE.suitable(url) else super(UdemyCourseIE, cls).suitable(url)


class ThisAVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?thisav\\.com/video/(?P<id>[0-9]+)/.*'
    _module = 'youtube_dl.extractor.thisav'


class CamTubeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:www|api)\\.)?camtube\\.co/recordings?/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.camtube'


class SeznamZpravyIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?seznamzpravy\\.cz/iframe/player\\?.*\\bsrc='
    _module = 'youtube_dl.extractor.seznamzpravy'


class MailRuIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:(?:www|m)\\.)?my\\.mail\\.ru/\n                        (?:\n                            video/.*\\#video=/?(?P<idv1>(?:[^/]+/){3}\\d+)|\n                            (?:(?P<idv2prefix>(?:[^/]+/){2})video/(?P<idv2suffix>[^/]+/\\d+))\\.html|\n                            (?:video/embed|\\+/video/meta)/(?P<metaid>\\d+)\n                        )\n                    '
    _module = 'youtube_dl.extractor.mailru'


class ThePlatformFeedIE(ThePlatformBaseIE):
    _VALID_URL = u'https?://feed\\.theplatform\\.com/f/(?P<provider_id>[^/]+)/(?P<feed_id>[^?/]+)\\?(?:[^&]+&)*(?P<filter>by(?:Gui|I)d=(?P<id>[^&]+))'
    _module = 'youtube_dl.extractor.theplatform'


class CBSBaseIE(ThePlatformFeedIE):
    _VALID_URL = u'https?://feed\\.theplatform\\.com/f/(?P<provider_id>[^/]+)/(?P<feed_id>[^?/]+)\\?(?:[^&]+&)*(?P<filter>by(?:Gui|I)d=(?P<id>[^&]+))'
    _module = 'youtube_dl.extractor.cbs'


class CBSIE(CBSBaseIE):
    _VALID_URL = u'(?:cbs:|https?://(?:www\\.)?(?:cbs\\.com/shows/[^/]+/video|colbertlateshow\\.com/(?:video|podcasts))/)(?P<id>[\\w-]+)'
    _module = 'youtube_dl.extractor.cbs'


class CBSSportsIE(CBSBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?cbssports\\.com/[^/]+/(?:video|news)/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.cbssports'


class CorusIE(ThePlatformFeedIE):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:www\\.)?\n                        (?P<domain>\n                            (?:globaltv|etcanada)\\.com|\n                            (?:hgtv|foodnetwork|slice|history|showcase|bigbrothercanada)\\.ca\n                        )\n                        /(?:video/(?:[^/]+/)?|(?:[^/]+/)+(?:videos/[a-z0-9-]+-|video\\.html\\?.*?\\bv=))\n                        (?P<id>\\d+)\n                    '
    _module = 'youtube_dl.extractor.corus'


class CBSNewsIE(CBSIE):
    _VALID_URL = u'https?://(?:www\\.)?cbsnews\\.com/(?:news|videos)/(?P<id>[\\da-z_-]+)'
    _module = 'youtube_dl.extractor.cbsnews'


class NRKTVIE(NRKBaseIE):
    _VALID_URL = u'(?x)\n                        https?://\n                            (?:tv|radio)\\.nrk(?:super)?\\.no/\n                            (?:serie(?:/[^/]+){1,2}|program)/\n                            (?![Ee]pisodes)(?P<id>[a-zA-Z]{4}\\d{8})\n                            (?:/\\d{2}-\\d{2}-\\d{4})?\n                            (?:\\#del=(?P<part_id>\\d+))?\n                    '
    _module = 'youtube_dl.extractor.nrk'


class NRKTVDirekteIE(NRKTVIE):
    _VALID_URL = u'https?://(?:tv|radio)\\.nrk\\.no/direkte/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.nrk'


class TassIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:tass\\.ru|itar-tass\\.com)/[^/]+/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.tass'


class PornHubUserVideosIE(PornHubPlaylistBaseIE):
    _VALID_URL = u'https?://(?:[^/]+\\.)?(?P<host>pornhub\\.(?:com|net))/(?:(?:user|channel)s|model|pornstar)/(?P<id>[^/]+)/videos'
    _module = 'youtube_dl.extractor.pornhub'


class PeerTubeIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    (?:\n                        peertube:(?P<host>[^:]+):|\n                        https?://(?P<host_2>(?:\n                            # Taken from https://instances.joinpeertube.org/instances\n                            tube\\.openalgeria\\.org|\n                            peertube\\.pointsecu\\.fr|\n                            peertube\\.nogafa\\.org|\n                            peertube\\.pl|\n                            megatube\\.lilomoino\\.fr|\n                            peertube\\.tamanoir\\.foucry\\.net|\n                            peertube\\.inapurna\\.org|\n                            peertube\\.netzspielplatz\\.de|\n                            video\\.deadsuperhero\\.com|\n                            peertube\\.devosi\\.org|\n                            peertube\\.1312\\.media|\n                            tube\\.worldofhauru\\.xyz|\n                            tube\\.bootlicker\\.party|\n                            skeptikon\\.fr|\n                            peertube\\.geekshell\\.fr|\n                            tube\\.opportunis\\.me|\n                            peertube\\.peshane\\.net|\n                            video\\.blueline\\.mg|\n                            tube\\.homecomputing\\.fr|\n                            videos\\.cloudfrancois\\.fr|\n                            peertube\\.viviers-fibre\\.net|\n                            tube\\.ouahpiti\\.info|\n                            video\\.tedomum\\.net|\n                            video\\.g3l\\.org|\n                            fontube\\.fr|\n                            peertube\\.gaialabs\\.ch|\n                            peertube\\.extremely\\.online|\n                            peertube\\.public-infrastructure\\.eu|\n                            tube\\.kher\\.nl|\n                            peertube\\.qtg\\.fr|\n                            tube\\.22decembre\\.eu|\n                            facegirl\\.me|\n                            video\\.migennes\\.net|\n                            janny\\.moe|\n                            tube\\.p2p\\.legal|\n                            video\\.atlanti\\.se|\n                            troll\\.tv|\n                            peertube\\.geekael\\.fr|\n                            vid\\.leotindall\\.com|\n                            video\\.anormallostpod\\.ovh|\n                            p-tube\\.h3z\\.jp|\n                            tube\\.darfweb\\.eu|\n                            videos\\.iut-orsay\\.fr|\n                            peertube\\.solidev\\.net|\n                            videos\\.symphonie-of-code\\.fr|\n                            testtube\\.ortg\\.de|\n                            videos\\.cemea\\.org|\n                            peertube\\.gwendalavir\\.eu|\n                            video\\.passageenseine\\.fr|\n                            videos\\.festivalparminous\\.org|\n                            peertube\\.touhoppai\\.moe|\n                            peertube\\.duckdns\\.org|\n                            sikke\\.fi|\n                            peertube\\.mastodon\\.host|\n                            firedragonvideos\\.com|\n                            vidz\\.dou\\.bet|\n                            peertube\\.koehn\\.com|\n                            peer\\.hostux\\.social|\n                            share\\.tube|\n                            peertube\\.walkingmountains\\.fr|\n                            medias\\.libox\\.fr|\n                            peertube\\.moe|\n                            peertube\\.xyz|\n                            jp\\.peertube\\.network|\n                            videos\\.benpro\\.fr|\n                            tube\\.otter\\.sh|\n                            peertube\\.angristan\\.xyz|\n                            peertube\\.parleur\\.net|\n                            peer\\.ecutsa\\.fr|\n                            peertube\\.heraut\\.eu|\n                            peertube\\.tifox\\.fr|\n                            peertube\\.maly\\.io|\n                            vod\\.mochi\\.academy|\n                            exode\\.me|\n                            coste\\.video|\n                            tube\\.aquilenet\\.fr|\n                            peertube\\.gegeweb\\.eu|\n                            framatube\\.org|\n                            thinkerview\\.video|\n                            tube\\.conferences-gesticulees\\.net|\n                            peertube\\.datagueule\\.tv|\n                            video\\.lqdn\\.fr|\n                            meilleurtube\\.delire\\.party|\n                            tube\\.mochi\\.academy|\n                            peertube\\.dav\\.li|\n                            media\\.zat\\.im|\n                            pytu\\.be|\n                            peertube\\.valvin\\.fr|\n                            peertube\\.nsa\\.ovh|\n                            video\\.colibris-outilslibres\\.org|\n                            video\\.hispagatos\\.org|\n                            tube\\.svnet\\.fr|\n                            peertube\\.video|\n                            videos\\.lecygnenoir\\.info|\n                            peertube3\\.cpy\\.re|\n                            peertube2\\.cpy\\.re|\n                            videos\\.tcit\\.fr|\n                            peertube\\.cpy\\.re\n                        ))/(?:videos/(?:watch|embed)|api/v\\d/videos)/\n                    )\n                    (?P<id>[\\da-fA-F]{8}-[\\da-fA-F]{4}-[\\da-fA-F]{4}-[\\da-fA-F]{4}-[\\da-fA-F]{12})\n                    '
    _module = 'youtube_dl.extractor.peertube'


class YouNowMomentIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?younow\\.com/[^/]+/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.younow'

    @classmethod
    def suitable(cls, url):
        return (False
                if YouNowChannelIE.suitable(url)
                else super(YouNowMomentIE, cls).suitable(url))


class RaiIE(RaiBaseIE):
    _VALID_URL = u'https?://[^/]+\\.(?:rai\\.(?:it|tv)|rainews\\.it)/.+?-(?P<id>[\\da-f]{8}-[\\da-f]{4}-[\\da-f]{4}-[\\da-f]{4}-[\\da-f]{12})(?:-.+?)?\\.html'
    _module = 'youtube_dl.extractor.rai'


class NetEaseMusicListIE(NetEaseMusicBaseIE):
    _VALID_URL = u'https?://music\\.163\\.com/(#/)?(playlist|discover/toplist)\\?id=(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.neteasemusic'


class WeiqiTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?weiqitv\\.com/index/video_play\\?videoId=(?P<id>[A-Za-z0-9]+)'
    _module = 'youtube_dl.extractor.weiqitv'


class RestudyIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:(?:www|portal)\\.)?restudy\\.dk/video/[^/]+/id/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.restudy'


class VierVideosIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?P<site>vier|vijf)\\.be/(?P<program>[^/]+)/videos(?:\\?.*\\bpage=(?P<page>\\d+)|$)'
    _module = 'youtube_dl.extractor.vier'


class UOLIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:.+?\\.)?uol\\.com\\.br/.*?(?:(?:mediaId|v)=|view/(?:[a-z0-9]+/)?|video(?:=|/(?:\\d{4}/\\d{2}/\\d{2}/)?))(?P<id>\\d+|[\\w-]+-[A-Z0-9]+)'
    _module = 'youtube_dl.extractor.uol'


class MixcloudUserIE(MixcloudPlaylistBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?mixcloud\\.com/(?P<user>[^/]+)/(?P<type>uploads|favorites|listens)?/?$'
    _module = 'youtube_dl.extractor.mixcloud'


class TwentyThreeVideoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://video\\.(?P<domain>twentythree\\.net|23video\\.com|filmweb\\.no)/v\\.ihtml/player\\.html\\?(?P<query>.*?\\bphoto(?:_|%5f)id=(?P<id>\\d+).*)'
    _module = 'youtube_dl.extractor.twentythreevideo'


class PandoraTVIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                        https?://\n                            (?:\n                                (?:www\\.)?pandora\\.tv/view/(?P<user_id>[^/]+)/(?P<id>\\d+)|  # new format\n                                (?:.+?\\.)?channel\\.pandora\\.tv/channel/video\\.ptv\\?|        # old format\n                                m\\.pandora\\.tv/?\\?                                          # mobile\n                            )\n                    '
    _module = 'youtube_dl.extractor.pandoratv'


class MacGameStoreIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?macgamestore\\.com/mediaviewer\\.php\\?trailer=(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.macgamestore'


class WashingtonPostArticleIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?washingtonpost\\.com/(?:[^/]+/)*(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.washingtonpost'

    @classmethod
    def suitable(cls, url):
        return False if WashingtonPostIE.suitable(url) else super(WashingtonPostArticleIE, cls).suitable(url)


class SproutIE(AdobePassIE):
    _VALID_URL = u'https?://(?:www\\.)?sproutonline\\.com/watch/(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.sprout'


class TVCArticleIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?tvc\\.ru/(?!video/iframe/id/)(?P<id>[^?#]+)'
    _module = 'youtube_dl.extractor.tvc'


class LibraryOfCongressIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?loc\\.gov/(?:item/|today/cyberlc/feature_wdesc\\.php\\?.*\\brec=)(?P<id>[0-9a-z_.]+)'
    _module = 'youtube_dl.extractor.libraryofcongress'


class ClipsyndicateIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:chic|www)\\.clipsyndicate\\.com/video/play(list/\\d+)?/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.clipsyndicate'


class ScreencastOMaticIE(LazyLoadExtractor):
    _VALID_URL = u'https?://screencast-o-matic\\.com/watch/(?P<id>[0-9a-zA-Z]+)'
    _module = 'youtube_dl.extractor.screencastomatic'


class CrackedIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?cracked\\.com/video_(?P<id>\\d+)_[\\da-z-]+\\.html'
    _module = 'youtube_dl.extractor.cracked'


class LecturioDeCourseIE(LecturioBaseIE):
    _VALID_URL = u'https://(?:www\\.)?lecturio\\.de/[^/]+/(?P<id>[^/?#&]+)\\.kurs'
    _module = 'youtube_dl.extractor.lecturio'


class PokemonIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?pokemon\\.com/[a-z]{2}(?:.*?play=(?P<id>[a-z0-9]{32})|/(?:[^/]+/)+(?P<display_id>[^/?#&]+))'
    _module = 'youtube_dl.extractor.pokemon'


class WatchIndianPornIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?watchindianporn\\.net/(?:[^/]+/)*video/(?P<display_id>[^/]+)-(?P<id>[a-zA-Z0-9]+)\\.html'
    _module = 'youtube_dl.extractor.watchindianporn'


class ChaturbateIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:[^/]+\\.)?chaturbate\\.com/(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.chaturbate'


class TNAFlixNetworkEmbedIE(TNAFlixNetworkBaseIE):
    _VALID_URL = u'https?://player\\.(?:tna|emp)flix\\.com/video/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.tnaflix'


class PacktPubIE(PacktPubBaseIE):
    _VALID_URL = u'https?://(?:(?:www\\.)?packtpub\\.com/mapt|subscription\\.packtpub\\.com)/video/[^/]+/(?P<course_id>\\d+)/(?P<chapter_id>\\d+)/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.packtpub'


class NobelPrizeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?nobelprize\\.org/mediaplayer.*?\\bid=(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.nobelprize'


class VKWallPostIE(VKBaseIE):
    _VALID_URL = u'https?://(?:(?:(?:(?:m|new)\\.)?vk\\.com/(?:[^?]+\\?.*\\bw=)?wall(?P<id>-?\\d+_\\d+)))'
    _module = 'youtube_dl.extractor.vk'


class LivestreamShortenerIE(LazyLoadExtractor):
    _VALID_URL = u'https?://livestre\\.am/(?P<id>.+)'
    _module = 'youtube_dl.extractor.livestream'


class ReutersIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?reuters\\.com/.*?\\?.*?videoId=(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.reuters'


class MySpaceAlbumIE(LazyLoadExtractor):
    _VALID_URL = u'https?://myspace\\.com/([^/]+)/music/album/(?P<title>.*-)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.myspace'


class YourUploadIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?:yourupload\\.com/(?:watch|embed)|embed\\.yourupload\\.com)/(?P<id>[A-Za-z0-9]+)'
    _module = 'youtube_dl.extractor.yourupload'


class TurboIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?turbo\\.fr/videos-voiture/(?P<id>[0-9]+)-'
    _module = 'youtube_dl.extractor.turbo'


class CartoonNetworkIE(TurnerBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?cartoonnetwork\\.com/video/(?:[^/]+/)+(?P<id>[^/?#]+)-(?:clip|episode)\\.html'
    _module = 'youtube_dl.extractor.cartoonnetwork'


class NationalGeographicTVIE(FOXIE):
    _VALID_URL = u'https?://(?:www\\.)?nationalgeographic\\.com/tv/watch/(?P<id>[\\da-fA-F]+)'
    _module = 'youtube_dl.extractor.nationalgeographic'


class SpiegelIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?spiegel\\.de/video/[^/]*-(?P<id>[0-9]+)(?:-embed|-iframe)?(?:\\.html)?(?:#.*)?$'
    _module = 'youtube_dl.extractor.spiegel'


class LA7IE(LazyLoadExtractor):
    _VALID_URL = u'(?x)(https?://)?(?:\n        (?:www\\.)?la7\\.it/([^/]+)/(?:rivedila7|video)/|\n        tg\\.la7\\.it/repliche-tgla7\\?id=\n    )(?P<id>.+)'
    _module = 'youtube_dl.extractor.la7'


class NewgroundsIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?newgrounds\\.com/(?:audio/listen|portal/view)/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.newgrounds'


class BeatportIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.|pro\\.)?beatport\\.com/track/(?P<display_id>[^/]+)/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.beatport'


class OCWMITIE(LazyLoadExtractor):
    _VALID_URL = u'^https?://ocw\\.mit\\.edu/courses/(?P<topic>[a-z0-9\\-]+)'
    _module = 'youtube_dl.extractor.mit'


class NexxIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                        (?:\n                            https?://api\\.nexx(?:\\.cloud|cdn\\.com)/v3/(?P<domain_id>\\d+)/videos/byid/|\n                            nexx:(?:(?P<domain_id_s>\\d+):)?|\n                            https?://arc\\.nexx\\.cloud/api/video/\n                        )\n                        (?P<id>\\d+)\n                    '
    _module = 'youtube_dl.extractor.nexx'


class CCCIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?media\\.ccc\\.de/v/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.ccc'


class CBSInteractiveIE(CBSIE):
    _VALID_URL = u'https?://(?:www\\.)?(?P<site>cnet|zdnet)\\.com/(?:videos|video(?:/share)?)/(?P<id>[^/?]+)'
    _module = 'youtube_dl.extractor.cbsinteractive'


class TechTalksIE(LazyLoadExtractor):
    _VALID_URL = u'https?://techtalks\\.tv/talks/(?:[^/]+/)?(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.techtalks'


class EscapistIE(LazyLoadExtractor):
    _VALID_URL = u'https?://?(?:(?:www|v1)\\.)?escapistmagazine\\.com/videos/view/[^/]+/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.escapist'


class VidmeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://vid\\.me/(?:e/)?(?P<id>[\\da-zA-Z]{,5})(?:[^\\da-zA-Z]|$)'
    _module = 'youtube_dl.extractor.vidme'


class VidioIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?vidio\\.com/watch/(?P<id>\\d+)-(?P<display_id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.vidio'


class YahooGyaOIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:gyao\\.yahoo\\.co\\.jp/p|streaming\\.yahoo\\.co\\.jp/p/y)/(?P<id>\\d+/v\\d+)'
    _module = 'youtube_dl.extractor.yahoo'


class Revision3IE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?P<domain>(?:revision3|animalist)\\.com)/(?P<id>[^/]+(?:/[^/?#]+)?)'
    _module = 'youtube_dl.extractor.revision3'


class TwitchPastBroadcastsIE(TwitchVideosBaseIE):
    _VALID_URL = u'https?://(?:(?:www|go|m)\\.)?twitch\\.tv/(?P<id>[^/]+)/videos/past-broadcasts'
    _module = 'youtube_dl.extractor.twitch'


class FlickrIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.|secure\\.)?flickr\\.com/photos/[\\w\\-_@]+/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.flickr'


class InternetVideoArchiveIE(LazyLoadExtractor):
    _VALID_URL = u'https?://video\\.internetvideoarchive\\.net/(?:player|flash/players)/.*?\\?.*?publishedid.*?'
    _module = 'youtube_dl.extractor.internetvideoarchive'


class XiamiCollectionIE(XiamiPlaylistBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?xiami\\.com/collect/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.xiami'


class TeachingChannelIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?teachingchannel\\.org/videos/(?P<title>.+)'
    _module = 'youtube_dl.extractor.teachingchannel'


class StreamCZIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?stream\\.cz/.+/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.streamcz'


class RutubePersonIE(RutubePlaylistBaseIE):
    _VALID_URL = u'https?://rutube\\.ru/video/person/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.rutube'


class DailymotionPlaylistIE(DailymotionBaseInfoExtractor):
    _VALID_URL = u'(?:https?://)?(?:www\\.)?dailymotion\\.[a-z]{2,3}/playlist/(?P<id>x[0-9a-z]+)'
    _module = 'youtube_dl.extractor.dailymotion'


class GlideIE(LazyLoadExtractor):
    _VALID_URL = u'https?://share\\.glide\\.me/(?P<id>[A-Za-z0-9\\-=_+]+)'
    _module = 'youtube_dl.extractor.glide'


class SpiegeltvIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?spiegel\\.tv/videos/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.spiegeltv'


class XiamiSongIE(XiamiBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?xiami\\.com/song/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.xiami'


class TVPIE(LazyLoadExtractor):
    _VALID_URL = u'https?://[^/]+\\.tvp\\.(?:pl|info)/(?:video/(?:[^,\\s]*,)*|(?:(?!\\d+/)[^/]+/)*)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.tvp'


class DemocracynowIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?democracynow\\.org/(?P<id>[^\\?]*)'
    _module = 'youtube_dl.extractor.democracynow'


class YouNowChannelIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?younow\\.com/(?P<id>[^/]+)/channel'
    _module = 'youtube_dl.extractor.younow'


class NBCNewsIE(ThePlatformIE):
    _VALID_URL = u'(?x)https?://(?:www\\.)?(?:nbcnews|today|msnbc)\\.com/([^/]+/)*(?:.*-)?(?P<id>[^/?]+)'
    _module = 'youtube_dl.extractor.nbc'


class StreamangoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?:streamango\\.com|fruithosts\\.net|streamcherry\\.com)/(?:f|embed)/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.streamango'


class TVANouvellesArticleIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?tvanouvelles\\.ca/(?:[^/]+/)+(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.tvanouvelles'

    @classmethod
    def suitable(cls, url):
        return False if TVANouvellesIE.suitable(url) else super(TVANouvellesArticleIE, cls).suitable(url)


class PhoenixIE(DreiSatIE):
    _VALID_URL = u'(?x)https?://(?:www\\.)?phoenix\\.de/content/\n        (?:\n            phoenix/die_sendungen/(?:[^/]+/)?\n        )?\n        (?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.phoenix'


class ITTFIE(LazyLoadExtractor):
    _VALID_URL = u'https?://tv\\.ittf\\.com/video/[^/]+/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.laola1tv'


class FoxgayIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?foxgay\\.com/videos/(?:\\S+-)?(?P<id>\\d+)\\.shtml'
    _module = 'youtube_dl.extractor.foxgay'


class BTArticleIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?bt\\.no/(?:[^/]+/)+(?P<id>[^/]+)-\\d+\\.html'
    _module = 'youtube_dl.extractor.vgtv'


class NetEaseMusicDjRadioIE(NetEaseMusicBaseIE):
    _VALID_URL = u'https?://music\\.163\\.com/(#/)?djradio\\?id=(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.neteasemusic'


class TDSLifewayIE(LazyLoadExtractor):
    _VALID_URL = u'https?://tds\\.lifeway\\.com/v1/trainingdeliverysystem/courses/(?P<id>\\d+)/index\\.html'
    _module = 'youtube_dl.extractor.tdslifeway'


class BeamProLiveIE(BeamProBaseIE):
    _VALID_URL = u'https?://(?:\\w+\\.)?(?:beam\\.pro|mixer\\.com)/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.beampro'

    @classmethod
    def suitable(cls, url):
        return False if BeamProVodIE.suitable(url) else super(BeamProLiveIE, cls).suitable(url)


class STVPlayerIE(LazyLoadExtractor):
    _VALID_URL = u'https?://player\\.stv\\.tv/(?P<type>episode|video)/(?P<id>[a-z0-9]{4})'
    _module = 'youtube_dl.extractor.stv'


class RteIE(RteBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?rte\\.ie/player/[^/]{2,3}/show/[^/]+/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.rte'


class VideoPressIE(LazyLoadExtractor):
    _VALID_URL = u'https?://videopress\\.com/embed/(?P<id>[\\da-zA-Z]+)'
    _module = 'youtube_dl.extractor.videopress'


class NHLBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.nhl'


class NHLIE(NHLBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?(?P<site>nhl|wch2016)\\.com/(?:[^/]+/)*c-(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.nhl'


class GameOneIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?gameone\\.de/tv/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.gameone'


class XimalayaAlbumIE(XimalayaBaseIE):
    _VALID_URL = u'https?://(?:www\\.|m\\.)?ximalaya\\.com/(?P<uid>[0-9]+)/album/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.ximalaya'


class RUTVIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:test)?player\\.(?:rutv\\.ru|vgtrk\\.com)/\n                        (?P<path>\n                            flash\\d+v/container\\.swf\\?id=|\n                            iframe/(?P<type>swf|video|live)/id/|\n                            index/iframe/cast_id/\n                        )\n                        (?P<id>\\d+)\n                    '
    _module = 'youtube_dl.extractor.rutv'


class HotStarBaseIE(LazyLoadExtractor):
    _VALID_URL = None
    _module = 'youtube_dl.extractor.hotstar'


class HotStarPlaylistIE(HotStarBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?hotstar\\.com/tv/[^/]+/s-\\w+/list/[^/]+/t-(?P<id>\\w+)'
    _module = 'youtube_dl.extractor.hotstar'


class XboxClipsIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?xboxclips\\.com/(?:video\\.php\\?.*vid=|[^/]+/)(?P<id>[\\w-]{36})'
    _module = 'youtube_dl.extractor.xboxclips'


class ToypicsIE(LazyLoadExtractor):
    _VALID_URL = u'https?://videos\\.toypics\\.net/view/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.toypics'


class EaglePlatformIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    (?:\n                        eagleplatform:(?P<custom_host>[^/]+):|\n                        https?://(?P<host>.+?\\.media\\.eagleplatform\\.com)/index/player\\?.*\\brecord_id=\n                    )\n                    (?P<id>\\d+)\n                '
    _module = 'youtube_dl.extractor.eagleplatform'


class OnetChannelIE(OnetBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?onet\\.tv/[a-z]/(?P<id>[a-z]+)(?:[?#]|$)'
    _module = 'youtube_dl.extractor.onet'


class SlideshareIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?slideshare\\.net/[^/]+?/(?P<title>.+?)($|\\?)'
    _module = 'youtube_dl.extractor.slideshare'


class ComedyCentralTVIE(MTVServicesInfoExtractor):
    _VALID_URL = u'https?://(?:www\\.)?comedycentral\\.tv/(?:staffeln|shows)/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.comedycentral'


class ADNIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?animedigitalnetwork\\.fr/video/[^/]+/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.adn'


class FuxIE(FourTubeBaseIE):
    _VALID_URL = u'https?://(?:(?P<kind>www|m)\\.)?fux\\.com/(?:video|embed)/(?P<id>\\d+)(?:/(?P<display_id>[^/?#&]+))?'
    _module = 'youtube_dl.extractor.fourtube'


class PressTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?presstv\\.ir/[^/]+/(?P<y>\\d+)/(?P<m>\\d+)/(?P<d>\\d+)/(?P<id>\\d+)/(?P<display_id>[^/]+)?'
    _module = 'youtube_dl.extractor.presstv'


class NBCSportsIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?nbcsports\\.com//?(?:[^/]+/)+(?P<id>[0-9a-z-]+)'
    _module = 'youtube_dl.extractor.nbc'


class ThreeQSDNIE(LazyLoadExtractor):
    _VALID_URL = u'https?://playout\\.3qsdn\\.com/(?P<id>[\\da-f]{8}-[\\da-f]{4}-[\\da-f]{4}-[\\da-f]{4}-[\\da-f]{12})'
    _module = 'youtube_dl.extractor.threeqsdn'


class SaltTVIE(ZattooIE):
    _VALID_URL = u'https?://(?:www\\.)?tv\\.salt\\.ch/watch/(?P<channel>[^/]+?)/(?P<id>[0-9]+)[^/]+(?:/(?P<recid>[0-9]+))?'
    _module = 'youtube_dl.extractor.zattoo'


class MovingImageIE(LazyLoadExtractor):
    _VALID_URL = u'https?://movingimage\\.nls\\.uk/film/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.movingimage'


class ImdbIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www|m)\\.imdb\\.com/(?:video|title|list).+?[/-]vi(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.imdb'


class NineNowIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?9now\\.com\\.au/(?:[^/]+/){2}(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.ninenow'


class SVTIE(SVTBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?svt\\.se/wd\\?(?:.*?&)?widgetId=(?P<widget_id>\\d+)&.*?\\barticleId=(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.svt'


class ZattooLiveIE(ZattooBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?zattoo\\.com/watch/(?P<id>[^/]+)'
    _module = 'youtube_dl.extractor.zattoo'

    @classmethod
    def suitable(cls, url):
        return False if ZattooIE.suitable(url) else super(ZattooLiveIE, cls).suitable(url)


class NprIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?npr\\.org/(?:sections/[^/]+/)?\\d{4}/\\d{2}/\\d{2}/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.npr'


class MixcloudPlaylistIE(MixcloudPlaylistBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?mixcloud\\.com/(?P<user>[^/]+)/playlists/(?P<playlist>[^/]+)/?$'
    _module = 'youtube_dl.extractor.mixcloud'


class DropboxIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?dropbox[.]com/sh?/(?P<id>[a-zA-Z0-9]{15})/.*'
    _module = 'youtube_dl.extractor.dropbox'


class TVANouvellesIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?tvanouvelles\\.ca/videos/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.tvanouvelles'


class GaiaIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?gaia\\.com/video/(?P<id>[^/?]+).*?\\bfullplayer=(?P<type>feature|preview)'
    _module = 'youtube_dl.extractor.gaia'


class BRIE(LazyLoadExtractor):
    _VALID_URL = u'(?P<base_url>https?://(?:www\\.)?br(?:-klassik)?\\.de)/(?:[a-z0-9\\-_]+/)+(?P<id>[a-z0-9\\-_]+)\\.html'
    _module = 'youtube_dl.extractor.br'


class TunePkIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:\n                            (?:www\\.)?tune\\.pk/(?:video/|player/embed_player.php?.*?\\bvid=)|\n                            embed\\.tune\\.pk/play/\n                        )\n                        (?P<id>\\d+)\n                    '
    _module = 'youtube_dl.extractor.tunepk'


class NoovoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:[^/]+\\.)?noovo\\.ca/videos/(?P<id>[^/]+/[^/?#&]+)'
    _module = 'youtube_dl.extractor.noovo'


class CanvasIE(LazyLoadExtractor):
    _VALID_URL = u'https?://mediazone\\.vrt\\.be/api/v1/(?P<site_id>canvas|een|ketnet|vrtvideo)/assets/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.canvas'


class MotherlessIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?motherless\\.com/(?:g/[a-z0-9_]+/)?(?P<id>[A-Z0-9]+)'
    _module = 'youtube_dl.extractor.motherless'


class VH1IE(MTVServicesInfoExtractor):
    _VALID_URL = u'https?://(?:www\\.)?vh1\\.com/(?:video-clips|episodes)/(?P<id>[^/?#.]+)'
    _module = 'youtube_dl.extractor.vh1'


class AdobeTVChannelIE(AdobeTVPlaylistBaseIE):
    _VALID_URL = u'https?://tv\\.adobe\\.com/(?:(?P<language>fr|de|es|jp)/)?channel/(?P<id>[^/]+)(?:/(?P<category_urlname>[^/]+))?'
    _module = 'youtube_dl.extractor.adobetv'


class ChilloutzoneIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?chilloutzone\\.net/video/(?P<id>[\\w|-]+)\\.html'
    _module = 'youtube_dl.extractor.chilloutzone'


class DaumUserIE(DaumListIE):
    _VALID_URL = u'https?://(?:m\\.)?tvpot\\.daum\\.net/mypot/(?:View|Top)\\.(?:do|tv)\\?.*?ownerid=(?P<id>[0-9a-zA-Z]+)'
    _module = 'youtube_dl.extractor.daum'


class PhotobucketIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:[a-z0-9]+\\.)?photobucket\\.com/.*(([\\?\\&]current=)|_)(?P<id>.*)\\.(?P<ext>(flv)|(mp4))'
    _module = 'youtube_dl.extractor.photobucket'


class PatreonIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?patreon\\.com/(?:creation\\?hid=|posts/(?:[\\w-]+-)?)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.patreon'


class EveryonesMixtapeIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?everyonesmixtape\\.com/#/mix/(?P<id>[0-9a-zA-Z]+)(?:/(?P<songnr>[0-9]))?$'
    _module = 'youtube_dl.extractor.everyonesmixtape'


class AudiomackAlbumIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?audiomack\\.com/album/(?P<id>[\\w/-]+)'
    _module = 'youtube_dl.extractor.audiomack'


class BaiduVideoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://v\\.baidu\\.com/(?P<type>[a-z]+)/(?P<id>\\d+)\\.htm'
    _module = 'youtube_dl.extractor.baidu'


class OnionStudiosIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?onionstudios\\.com/(?:video(?:s/[^/]+-|/)|embed\\?.*\\bid=)(?P<id>\\d+)(?!-)'
    _module = 'youtube_dl.extractor.onionstudios'


class ViewLiftEmbedIE(ViewLiftBaseIE):
    _VALID_URL = u'https?://(?:(?:www|embed)\\.)?(?:(?:snagfilms|snagxtreme|funnyforfree|kiddovid|winnersview|(?:monumental|lax)sportsnetwork|vayafilm)\\.com|hoichoi\\.tv)/embed/player\\?.*\\bfilmId=(?P<id>[\\da-f]{8}-(?:[\\da-f]{4}-){3}[\\da-f]{12})'
    _module = 'youtube_dl.extractor.viewlift'


class Revision3EmbedIE(LazyLoadExtractor):
    _VALID_URL = u'(?:revision3:(?:(?P<playlist_type>[^:]+):)?|https?://(?:(?:(?:www|embed)\\.)?(?:revision3|animalist)|(?:(?:api|embed)\\.)?seekernetwork)\\.com/player/embed\\?videoId=)(?P<playlist_id>\\d+)'
    _module = 'youtube_dl.extractor.revision3'


class BlinkxIE(LazyLoadExtractor):
    _VALID_URL = u'(?:https?://(?:www\\.)blinkx\\.com/#?ce/|blinkx:)(?P<id>[^?]+)'
    _module = 'youtube_dl.extractor.blinkx'


class XMinusIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?x-minus\\.org/track/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.xminus'


class MyviIE(SprutoBaseIE):
    _VALID_URL = u'(?x)\n                        (?:\n                            https?://\n                                (?:www\\.)?\n                                myvi\\.\n                                (?:\n                                    (?:ru/player|tv)/\n                                    (?:\n                                        (?:\n                                            embed/html|\n                                            flash|\n                                            api/Video/Get\n                                        )/|\n                                        content/preloader\\.swf\\?.*\\bid=\n                                    )|\n                                    ru/watch/\n                                )|\n                            myvi:\n                        )\n                        (?P<id>[\\da-zA-Z_-]+)\n                    '
    _module = 'youtube_dl.extractor.myvi'


class EWETVIE(ZattooIE):
    _VALID_URL = u'https?://(?:www\\.)?tvonline\\.ewe\\.de/watch/(?P<channel>[^/]+?)/(?P<id>[0-9]+)[^/]+(?:/(?P<recid>[0-9]+))?'
    _module = 'youtube_dl.extractor.zattoo'


class VrtNUIE(GigyaBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?vrt\\.be/(?P<site_id>vrtnu)/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.canvas'


class MLBIE(NHLBaseIE):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:[\\da-z_-]+\\.)*(?P<site>mlb)\\.com/\n                        (?:\n                            (?:\n                                (?:[^/]+/)*c-|\n                                (?:\n                                    shared/video/embed/(?:embed|m-internal-embed)\\.html|\n                                    (?:[^/]+/)+(?:play|index)\\.jsp|\n                                )\\?.*?\\bcontent_id=\n                            )\n                            (?P<id>\\d+)\n                        )\n                    '
    _module = 'youtube_dl.extractor.mlb'


class EchoMskIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?echo\\.msk\\.ru/sounds/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.echomsk'


class VimeoReviewIE(VimeoBaseInfoExtractor):
    _VALID_URL = u'(?P<url>https://vimeo\\.com/[^/]+/review/(?P<id>[^/]+)/[0-9a-f]{10})'
    _module = 'youtube_dl.extractor.vimeo'


class WallaIE(LazyLoadExtractor):
    _VALID_URL = u'https?://vod\\.walla\\.co\\.il/[^/]+/(?P<id>\\d+)/(?P<display_id>.+)'
    _module = 'youtube_dl.extractor.walla'


class ClubicIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?clubic\\.com/video/(?:[^/]+/)*video.*-(?P<id>[0-9]+)\\.html'
    _module = 'youtube_dl.extractor.clubic'


class LetvCloudIE(LazyLoadExtractor):
    _VALID_URL = u'https?://yuntv\\.letv\\.com/bcloud.html\\?.+'
    _module = 'youtube_dl.extractor.leeco'


class MySpaceIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        myspace\\.com/[^/]+/\n                        (?P<mediatype>\n                            video/[^/]+/(?P<video_id>\\d+)|\n                            music/song/[^/?#&]+-(?P<song_id>\\d+)-\\d+(?:[/?#&]|$)\n                        )\n                    '
    _module = 'youtube_dl.extractor.myspace'


class SharedIE(SharedBaseIE):
    _VALID_URL = u'https?://shared\\.sx/(?P<id>[\\da-z]{10})'
    _module = 'youtube_dl.extractor.shared'


class ArteTVMagazineIE(ArteTVPlus7IE):
    _VALID_URL = u'https?://(?:www\\.)?arte\\.tv/magazine/[^/]+/(?P<lang>fr|de|en|es)/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.arte'

    @classmethod
    def suitable(cls, url):
        return False if ArteTVPlaylistIE.suitable(url) else super(ArteTVPlus7IE, cls).suitable(url)


class RTPIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?rtp\\.pt/play/p(?P<program_id>[0-9]+)/(?P<id>[^/?#]+)/?'
    _module = 'youtube_dl.extractor.rtp'


class SmotriBroadcastIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?P<url>smotri\\.com/live/(?P<id>[^/]+))/?.*'
    _module = 'youtube_dl.extractor.smotri'


class TestURLIE(LazyLoadExtractor):
    _VALID_URL = u'test(?:url)?:(?P<id>(?P<extractor>.+?)(?:_(?P<num>[0-9]+))?)$'
    _module = 'youtube_dl.extractor.testurl'


class TBSIE(TurnerBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?(?P<site>tbs|tntdrama)\\.com(?P<path>/(?:movies|shows/[^/]+/(?:clips|season-\\d+/episode-\\d+))/(?P<id>[^/?#]+))'
    _module = 'youtube_dl.extractor.tbs'


class ViuOTTIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?viu\\.com/ott/(?P<country_code>[a-z]{2})/[a-z]{2}-[a-z]{2}/vod/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.viu'


class LivestreamIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:new\\.)?livestream\\.com/(?:accounts/(?P<account_id>\\d+)|(?P<account_name>[^/]+))/(?:events/(?P<event_id>\\d+)|(?P<event_name>[^/]+))(?:/videos/(?P<id>\\d+))?'
    _module = 'youtube_dl.extractor.livestream'


class VODPlatformIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?vod-platform\\.net/[eE]mbed/(?P<id>[^/?#]+)'
    _module = 'youtube_dl.extractor.vodplatform'


class InstagramIE(LazyLoadExtractor):
    _VALID_URL = u'(?P<url>https?://(?:www\\.)?instagram\\.com/p/(?P<id>[^/?#&]+))'
    _module = 'youtube_dl.extractor.instagram'


class OutsideTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?outsidetv\\.com/(?:[^/]+/)*?play/[a-zA-Z0-9]{8}/\\d+/\\d+/(?P<id>[a-zA-Z0-9]{8})'
    _module = 'youtube_dl.extractor.outsidetv'


class NRKTVEpisodesIE(NRKPlaylistBaseIE):
    _VALID_URL = u'https?://tv\\.nrk\\.no/program/[Ee]pisodes/[^/]+/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.nrk'


class BambuserIE(LazyLoadExtractor):
    _VALID_URL = u'https?://bambuser\\.com/v/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.bambuser'


class DailyMailIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?dailymail\\.co\\.uk/(?:video/[^/]+/video-|embed/video/)(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.dailymail'


class TumblrIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?P<blog_name>[^/?#&]+)\\.tumblr\\.com/(?:post|video)/(?P<id>[0-9]+)(?:$|[/?#])'
    _module = 'youtube_dl.extractor.tumblr'


class HuajiaoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?huajiao\\.com/l/(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.huajiao'


class NickNightIE(NickDeIE):
    _VALID_URL = u'https?://(?:www\\.)(?P<host>nicknight\\.(?:de|at|tv))/(?:playlist|shows)/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.nick'


class AdobeTVVideoIE(LazyLoadExtractor):
    _VALID_URL = u'https?://video\\.tv\\.adobe\\.com/v/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.adobetv'


class SmotriIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?(?:smotri\\.com/video/view/\\?id=|pics\\.smotri\\.com/(?:player|scrubber_custom8)\\.swf\\?file=)(?P<id>v(?P<realvideoid>[0-9]+)[a-z0-9]{4})'
    _module = 'youtube_dl.extractor.smotri'


class MinistryGridIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?ministrygrid\\.com/([^/?#]*/)*(?P<id>[^/#?]+)/?(?:$|[?#])'
    _module = 'youtube_dl.extractor.ministrygrid'


class CBCPlayerIE(LazyLoadExtractor):
    _VALID_URL = u'(?:cbcplayer:|https?://(?:www\\.)?cbc\\.ca/(?:player/play/|i/caffeine/syndicate/\\?mediaId=))(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.cbc'


class VyboryMosIE(LazyLoadExtractor):
    _VALID_URL = u'https?://vybory\\.mos\\.ru/(?:#precinct/|account/channels\\?.*?\\bstation_id=)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.vyborymos'


class XiamiAlbumIE(XiamiPlaylistBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?xiami\\.com/album/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.xiami'


class AbcNewsVideoIE(AMPIE):
    _VALID_URL = u'(?x)\n                    https?://\n                        abcnews\\.go\\.com/\n                        (?:\n                            [^/]+/video/(?P<display_id>[0-9a-z-]+)-|\n                            video/embed\\?.*?\\bid=\n                        )\n                        (?P<id>\\d+)\n                    '
    _module = 'youtube_dl.extractor.abcnews'


class SpankBangIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:[^/]+\\.)?spankbang\\.com/(?P<id>[\\da-z]+)/(?:video|play|embed)\\b'
    _module = 'youtube_dl.extractor.spankbang'


class ITVBTCCIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?itv\\.com/btcc/(?:[^/]+/)*(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.itv'


class TuneInStationIE(TuneInBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?tunein\\.com/(?:radio/.*?-s|station/.*?StationId=|embed/player/s)(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.tunein'

    @classmethod
    def suitable(cls, url):
        return False if TuneInClipIE.suitable(url) else super(TuneInStationIE, cls).suitable(url)


class BrightcoveLegacyIE(LazyLoadExtractor):
    _VALID_URL = u'(?:https?://.*brightcove\\.com/(services|viewer).*?\\?|brightcove:)(?P<query>.*)'
    _module = 'youtube_dl.extractor.brightcove'


class UrortIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?urort\\.p3\\.no/#!/Band/(?P<id>[^/]+)$'
    _module = 'youtube_dl.extractor.urort'


class MNetTVIE(ZattooIE):
    _VALID_URL = u'https?://(?:www\\.)?tvplus\\.m\\-net\\.de/watch/(?P<channel>[^/]+?)/(?P<id>[0-9]+)[^/]+(?:/(?P<recid>[0-9]+))?'
    _module = 'youtube_dl.extractor.zattoo'


class RTL2YouSeriesIE(RTL2YouBaseIE):
    _VALID_URL = u'http?://you\\.rtl2\\.de/videos/(?P<id>\\d+)'
    _module = 'youtube_dl.extractor.rtl2'


class AppleDailyIE(NextMediaIE):
    _VALID_URL = u'https?://(www|ent)\\.appledaily\\.com\\.tw/[^/]+/[^/]+/[^/]+/(?P<date>\\d+)/(?P<id>\\d+)(/.*)?'
    _module = 'youtube_dl.extractor.nextmedia'


class IwaraIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.|ecchi\\.)?iwara\\.tv/videos/(?P<id>[a-zA-Z0-9]+)'
    _module = 'youtube_dl.extractor.iwara'


class HetKlokhuisIE(NPODataMidEmbedIE):
    _VALID_URL = u'https?://(?:www\\.)?hetklokhuis\\.nl/[^/]+/\\d+/(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.npo'


class EmbedlyIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www|cdn\\.)?embedly\\.com/widgets/media\\.html\\?(?:[^#]*?&)?url=(?P<id>[^#&]+)'
    _module = 'youtube_dl.extractor.embedly'


class LinuxAcademyIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:www\\.)?linuxacademy\\.com/cp/\n                        (?:\n                            courses/lesson/course/(?P<chapter_id>\\d+)/lesson/(?P<lesson_id>\\d+)|\n                            modules/view/id/(?P<course_id>\\d+)\n                        )\n                    '
    _module = 'youtube_dl.extractor.linuxacademy'


class NPOIE(NPOBaseIE):
    _VALID_URL = u'(?x)\n                    (?:\n                        npo:|\n                        https?://\n                            (?:www\\.)?\n                            (?:\n                                npo\\.nl/(?:[^/]+/)*|\n                                (?:ntr|npostart)\\.nl/(?:[^/]+/){2,}|\n                                omroepwnl\\.nl/video/fragment/[^/]+__|\n                                (?:zapp|npo3)\\.nl/(?:[^/]+/){2,}\n                            )\n                        )\n                        (?P<id>[^/?#]+)\n                '
    _module = 'youtube_dl.extractor.npo'

    @classmethod
    def suitable(cls, url):
        return (False if any(ie.suitable(url)
                for ie in (NPOLiveIE, NPORadioIE, NPORadioFragmentIE))
                else super(NPOIE, cls).suitable(url))


class NPOPlaylistBaseIE(NPOIE):
    _VALID_URL = u'(?x)\n                    (?:\n                        npo:|\n                        https?://\n                            (?:www\\.)?\n                            (?:\n                                npo\\.nl/(?:[^/]+/)*|\n                                (?:ntr|npostart)\\.nl/(?:[^/]+/){2,}|\n                                omroepwnl\\.nl/video/fragment/[^/]+__|\n                                (?:zapp|npo3)\\.nl/(?:[^/]+/){2,}\n                            )\n                        )\n                        (?P<id>[^/?#]+)\n                '
    _module = 'youtube_dl.extractor.npo'

    @classmethod
    def suitable(cls, url):
        return (False if any(ie.suitable(url)
                for ie in (NPOLiveIE, NPORadioIE, NPORadioFragmentIE))
                else super(NPOIE, cls).suitable(url))


class WNLIE(NPOPlaylistBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?omroepwnl\\.nl/video/detail/(?P<id>[^/]+)__\\d+'
    _module = 'youtube_dl.extractor.npo'

    @classmethod
    def suitable(cls, url):
        return (False if any(ie.suitable(url)
                for ie in (NPOLiveIE, NPORadioIE, NPORadioFragmentIE))
                else super(NPOIE, cls).suitable(url))


class AndereTijdenIE(NPOPlaylistBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?anderetijden\\.nl/programma/(?:[^/]+/)+(?P<id>[^/?#&]+)'
    _module = 'youtube_dl.extractor.npo'

    @classmethod
    def suitable(cls, url):
        return (False if any(ie.suitable(url)
                for ie in (NPOLiveIE, NPORadioIE, NPORadioFragmentIE))
                else super(NPOIE, cls).suitable(url))


class MioMioIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?miomio\\.tv/watch/cc(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.miomio'


class ArteTVCinemaIE(ArteTVPlus7IE):
    _VALID_URL = u'https?://cinema\\.arte\\.tv/(?P<lang>fr|de|en|es)/(?P<id>.+)'
    _module = 'youtube_dl.extractor.arte'

    @classmethod
    def suitable(cls, url):
        return False if ArteTVPlaylistIE.suitable(url) else super(ArteTVPlus7IE, cls).suitable(url)


class AdultSwimIE(TurnerBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?adultswim\\.com/videos/(?P<show_path>[^/?#]+)(?:/(?P<episode_path>[^/?#]+))?'
    _module = 'youtube_dl.extractor.adultswim'


class IGNIE(LazyLoadExtractor):
    _VALID_URL = u'https?://.+?\\.ign\\.com/(?:[^/]+/)?(?P<type>videos|show_videos|articles|feature|(?:[^/]+/\\d+/video))(/.+)?/(?P<name_or_id>.+)'
    _module = 'youtube_dl.extractor.ign'


class PCMagIE(IGNIE):
    _VALID_URL = u'https?://(?:www\\.)?pcmag\\.com/(?P<type>videos|article2)(/.+)?/(?P<name_or_id>.+)'
    _module = 'youtube_dl.extractor.ign'


class OneUPIE(IGNIE):
    _VALID_URL = u'https?://gamevideos\\.1up\\.com/(?P<type>video)/id/(?P<name_or_id>.+)\\.html'
    _module = 'youtube_dl.extractor.ign'


class ACastChannelIE(LazyLoadExtractor):
    _VALID_URL = u'(?x)\n                    https?://\n                        (?:\n                            (?:www\\.)?acast\\.com/|\n                            play\\.acast\\.com/s/\n                        )\n                        (?P<id>[^/#?]+)\n                    '
    _module = 'youtube_dl.extractor.acast'

    @classmethod
    def suitable(cls, url):
        return False if ACastIE.suitable(url) else super(ACastChannelIE, cls).suitable(url)


class LineTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://tv\\.line\\.me/v/(?P<id>\\d+)_[^/]+-(?P<segment>ep\\d+-\\d+)'
    _module = 'youtube_dl.extractor.line'


class VPROIE(NPOPlaylistBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?(?:(?:tegenlicht\\.)?vpro|2doc)\\.nl/(?:[^/]+/)*(?P<id>[^/]+)\\.html'
    _module = 'youtube_dl.extractor.npo'

    @classmethod
    def suitable(cls, url):
        return (False if any(ie.suitable(url)
                for ie in (NPOLiveIE, NPORadioIE, NPORadioFragmentIE))
                else super(NPOIE, cls).suitable(url))


class PuhuTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?puhutv\\.com/(?P<id>[^/?#&]+)-izle'
    _module = 'youtube_dl.extractor.puhutv'


class MwaveIE(LazyLoadExtractor):
    _VALID_URL = u'https?://mwave\\.interest\\.me/(?:[^/]+/)?mnettv/videodetail\\.m\\?searchVideoDetailVO\\.clip_id=(?P<id>[0-9]+)'
    _module = 'youtube_dl.extractor.mwave'


class CWTVIE(LazyLoadExtractor):
    _VALID_URL = u'https?://(?:www\\.)?cw(?:tv(?:pr)?|seed)\\.com/(?:shows/)?(?:[^/]+/)+[^?]*\\?.*\\b(?:play|watch)=(?P<id>[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12})'
    _module = 'youtube_dl.extractor.cwtv'


class HotStarIE(HotStarBaseIE):
    _VALID_URL = u'https?://(?:www\\.)?hotstar\\.com/(?:.+?[/-])?(?P<id>\\d{10})'
    _module = 'youtube_dl.extractor.hotstar'


class TwitterAmplifyIE(TwitterBaseIE):
    _VALID_URL = u'https?://amp\\.twimg\\.com/v/(?P<id>[0-9a-f\\-]{36})'
    _module = 'youtube_dl.extractor.twitter'


class GenericIE(LazyLoadExtractor):
    _VALID_URL = u'.*'
    _module = 'youtube_dl.extractor.generic'

_ALL_CLASSES = [TelewebionIE, IconosquareIE, NocoIE, HitboxIE, DailymotionIE, TwitCastingIE, EllenTubePlaylistIE, HungamaSongIE, MyChannelsIE, MuenchenTVIE, LecturioCourseIE, MorningstarIE, FiveThirtyEightIE, SRGSSRIE, VKUserVideosIE, GoogleDriveIE, ServusIE, SztvHuIE, MinotoIE, CuriosityStreamIE, QQMusicIE, TwitchVodIE, IvideonIE, MedialaanIE, CultureboxIE, MailRuMusicIE, FoxSportsIE, MediasetIE, SaveFromIE, MeipaiIE, LifeEmbedIE, NownessIE, WatIE, IPrimaIE, DisneyIE, YoukuShowIE, OpenloadIE, StreamcloudIE, NiconicoPlaylistIE, DaisukiMottoPlaylistIE, KUSIIE, PodomaticIE, TVN24IE, YahooSearchIE, DVTVIE, FourTubeIE, TheSunIE, YahooIE, CloudflareStreamIE, NineCNineMediaIE, LyndaCourseIE, DiscoveryGoIE, ExpressenIE, VivoIE, FranceTVJeunesseIE, GazetaIE, TwitterCardIE, ZattooIE, EinsUndEinsTVIE, ImdbListIE, M6IE, TMZIE, ComedyCentralShortnameIE, WDRMobileIE, USATodayIE, TwentyFourVideoIE, DrTuberIE, FrontendMastersIE, TuneInClipIE, METAIE, KuwoIE, DaumIE, NFLIE, CloudyIE, Sport5IE, AppleTrailersIE, SverigesRadioEpisodeIE, SexuIE, NickBrIE, GrouponIE, Vbox7IE, Laola1TvEmbedIE, Laola1TvIE, EHFTVIE, YandexMusicTrackIE, SendtoNewsIE, RaiPlayIE, BostonGlobeIE, AWAANVideoIE, QQMusicAlbumIE, TwitterIE, TeleTaskIE, OoyalaIE, TVNowShowIE, CinemaxIE, ClippitIE, VikiIE, RedditIE, VimeoOndemandIE, ShowRoomLiveIE, MelonVODIE, RTVSIE, FXNetworksIE, SafariIE, AWAANLiveIE, Ir90TvIE, PornoVoisinesIE, InstagramTagIE, DFBIE, PuhuTVSerieIE, FolketingetIE, WholeCloudIE, VevoIE, Lecture2GoIE, WimpIE, MetacafeIE, VevoPlaylistIE, YouPornIE, TriluliluIE, TwitchAllVideosIE, TVPWebsiteIE, TVPEmbedIE, DctpTvIE, ElPaisIE, ABCOTVSClipsIE, WatchBoxIE, RtlNlIE, CBSNewsLiveVideoIE, RuutuIE, EllenTubeVideoIE, UstreamIE, JamendoAlbumIE, DumpertIE, PlayFMIE, DiscoveryIE, GloboIE, FreesoundIE, ViddlerIE, CBCWatchIE, TwitchStreamIE, MangomoloLiveIE, CrunchyrollShowPlaylistIE, PornerBrosIE, NexxEmbedIE, WeiboIE, ArteTvIE, GameOnePlaylistIE, CharlieRoseIE, RadioFranceIE, ViceIE, CoubIE, GodTubeIE, VidLiiIE, VideaIE, ITVIE, PluralsightCourseIE, PicartoVodIE, VLiveChannelIE, HarkIE, PearVideoIE, RENTVArticleIE, ORFFM4StoryIE, LoveHomePornIE, DRTVLiveIE, ARDIE, NYTimesArticleIE, ChirbitProfileIE, TheInterceptIE, MallTVIE, TVPlayerIE, NiconicoIE, LentaIE, ReverbNationIE, EMPFlixIE, TheSceneIE, HRTiIE, MatchTVIE, SBSIE, CriterionIE, MicrosoftVirtualAcademyCourseIE, NownessSeriesIE, UDNEmbedIE, AdobeTVShowIE, MediasiteNamedCatalogIE, ViewLiftIE, InaIE, CommonMistakesIE, KuwoSingerIE, NownessPlaylistIE, VideoPremiumIE, ToggleIE, AnimeOnDemandIE, ViqeoIE, TF1IE, TFOIE, NDRIE, DefenseGouvFrIE, MarkizaIE, XstreamIE, NovaEmbedIE, YahooGyaOPlayerIE, TV2ArticleIE, EllenTubeIE, VesselIE, HeiseIE, TikTokUserIE, AddAnimeIE, BitChuteChannelIE, YoutubeSearchIE, StitcherIE, Channel9IE, VrakIE, ArkenaIE, OktoberfestTVIE, TVNoeIE, DWIE, ZDFIE, YandexMusicAlbumIE, CSNNEIE, PinkbikeIE, DeezerPlaylistIE, DRBonanzaIE, FranceTVInfoSportIE, TEDIE, StretchInternetIE, PlatziIE, SVTPageIE, MTVDEIE, CNBCIE, NonkTubeIE, GloboArticleIE, TwitchVideoIE, EitbIE, URPlayIE, PolskieRadioCategoryIE, TvigleIE, TuneInProgramIE, BusinessInsiderIE, NowVideoIE, NTVDeIE, CarambaTVIE, TikTokIE, TwitchHighlightsIE, LecturioIE, XHamsterIE, HypemIE, GameInformerIE, IviIE, SenateISVPIE, DTubeIE, AsianCrushIE, CCMAIE, WSJArticleIE, SeznamZpravyArticleIE, PeriscopeUserIE, EuropaIE, CNNBlogsIE, Tele5IE, PluralsightIE, QuantumTVIE, OnetPlIE, HitRecordIE, RegioTVIE, VidbitIE, PeriscopeIE, RudoIE, JeuxVideoIE, DHMIE, EpornerIE, AWAANIE, TVLandIE, BBCCoUkIE, FrontendMastersLessonIE, NormalbootsIE, TVPlayHomeIE, GameSpotIE, DiscoveryVRIE, VootIE, ComedyCentralFullEpisodesIE, ClypIE, TeachableIE, UnityIE, SlidesLiveIE, RTVELiveIE, UnicodeBOMIE, HellPornoIE, YoutubeShowIE, SafariApiIE, ClipRsIE, EsriVideoIE, SkySportsIE, PornHdIE, RuvIE, DiggIE, NickIE, FoxNewsArticleIE, XFileShareIE, MinhatecaIE, StanfordOpenClassroomIE, PikselIE, SlutloadIE, SoundgasmIE, TVNowIE, FlipagramIE, YandexMusicPlaylistIE, MovieClipsIE, RadioDeIE, KuwoMvIE, AllocineIE, NRLTVIE, UstudioIE, TagesschauIE, YoutubeHistoryIE, LePlaylistIE, MixcloudIE, ImgurIE, HowcastIE, Varzesh3IE, LiTVIE, YoutubeSearchURLIE, VTXTVIE, SpiegelArticleIE, KontrTubeIE, MTVServicesEmbeddedIE, BioBioChileTVIE, VHXEmbedIE, CuriosityStreamCollectionIE, RTVETelevisionIE, NineGagIE, OnDemandKoreaIE, ESPNArticleIE, XTubeIE, SmotriUserIE, KhanAcademyIE, BiliBiliBangumiIE, MotherlessGroupIE, Canalc2IE, JWPlatformIE, NPOLiveIE, SpankwireIE, JojIE, APAIE, NTVCoJpCUIE, RutubePlaylistIE, TechTVMITIE, XimalayaIE, EroProfileIE, HKETVIE, CNNIE, BildIE, CrooksAndLiarsIE, MakerTVIE, SportBoxIE, ViafreeIE, QuicklineIE, AparatIE, CCTVIE, VRVSeriesIE, AmericasTestKitchenIE, DigitekaIE, GaskrankIE, MotorsportIE, SRGSSRPlayIE, BehindKinkIE, BBCCoUkPlaylistIE, LeIE, ABCOTVSIE, DreiSatIE, FOXIE, CamdemyFolderIE, RayWenderlichIE, GigaIE, KonserthusetPlayIE, CrackleIE, BetIE, KeezMoviesIE, ExtremeTubeIE, Tube8IE, KarriereVideosIE, VidziIE, SnotrIE, LemondeIE, PornComIE, IncIE, NRKPlaylistIE, SkylineWebcamsIE, ZypeIE, EggheadCourseIE, AnvatoIE, FOX9IE, C56IE, VideomoreSeasonIE, AtresPlayerIE, AudiMediaIE, EyedoTVIE, AolIE, ATVAtIE, VODPlIE, ABCIE, LiveLeakIE, IndavideoEmbedIE, ComedyCentralIE, SkyNewsArabiaArticleIE, ParliamentLiveUKIE, Tele13IE, InstagramUserIE, MITIE, SafariCourseIE, CamdemyIE, WDRIE, PlatziCourseIE, BandcampWeeklyIE, NewstubeIE, SVTSeriesIE, BokeCCIE, Zaq1IE, MoviezineIE, VideoWeedIE, TVNetIE, MusicPlayOnIE, BandcampIE, BBCCoUkIPlayerPlaylistIE, Ku6IE, NFBIE, GameStarIE, ViceArticleIE, FacebookIE, CeskaTelevizePoradyIE, CSpanIE, ManyVidsIE, RTBFIE, TinyPicIE, TVNowAnnualIE, PandaTVIE, PopcornTVIE, PornFlipIE, BeamProVodIE, TeleQuebecEmissionIE, VLivePlaylistIE, LivestreamOriginalIE, CloserToTruthIE, AdobeTVIE, RBMARadioIE, OraTVIE, UKTVPlayIE, WDRPageIE, PBSIE, ProSiebenSat1IE, LimelightChannelListIE, GooglePlusIE, YandexDiskIE, BTVestlendingenIE, CiscoLiveSessionIE, HelsinkiIE, NBCIE, EinthusanIE, LifeNewsIE, RTL2YouIE, PyvideoIE, LyndaIE, HearThisAtIE, GPUTechConfIE, NBAIE, TVAIE, ZapiksIE, ZDFChannelIE, PornTubeIE, TVNowNewIE, RUHDIE, NBCOlympicsIE, TwitchChapterIE, BleacherReportCMSIE, NRKTVSeriesIE, DouyuShowIE, TwitchUploadsIE, NosVideoIE, IzleseneIE, VideomoreVideoIE, SWRMediathekIE, CanvasEenIE, FacebookPluginsVideoIE, AlphaPornoIE, FiveTVIE, YouNowLiveIE, LEGOIE, SoundgasmProfileIE, RENTVIE, GoshgayIE, BleacherReportIE, BYUtvIE, MicrosoftVirtualAcademyIE, LCIIE, NuvidIE, NRKIE, PornHubPlaylistIE, Ro220IE, VoiceRepublicIE, ArteTVPlus7IE, ArteTVConcertIE, ArteTVCreativeIE, TheOperaPlatformIE, ArteTVEmbedIE, ArteTVDDCIE, AudiomackIE, BeegIE, YoutubeChannelIE, TeleQuebecIE, YouJizzIE, NRKSkoleIE, TuneInTopicIE, ABCIViewIE, SixPlayIE, VimeoChannelIE, FreespeechIE, FiveMinIE, FranceTVSiteIE, ZingMp3IE, MTVVideoIE, VestiIE, IqiyiIE, VoxMediaIE, AsianCrushPlaylistIE, HowStuffWorksIE, NhkVodIE, NetEaseMusicSingerIE, NZZIE, FC2EmbedIE, XNXXIE, WebcasterFeedIE, YoutubeLiveIE, MDRIE, CNBCVideoIE, CDAIE, WSJIE, PladformIE, VierIE, VimeoIE, BambuserChannelIE, PornotubeIE, FunkChannelIE, HGTVComShowIE, RoosterTeethIE, TelegraafIE, DRTVIE, YoutubeTruncatedIDIE, CNNArticleIE, JpopsukiIE, UstreamChannelIE, DBTVIE, MTV81IE, ToypicsUserIE, TwentyMinutenIE, PromptFileIE, AliExpressLiveIE, ThisAmericanLifeIE, BFIPlayerIE, HiDiveIE, RtmpIE, TubiTvIE, VikiChannelIE, AirMozillaIE, DPlayItIE, XHamsterEmbedIE, SportDeutschlandIE, WorldStarHipHopIE, R7ArticleIE, NozIE, BellMediaIE, RutubeMovieIE, DaisukiMottoIE, MovieFapIE, CBCIE, XiamiArtistIE, WebOfStoriesPlaylistIE, UMGDeIE, QQMusicSingerIE, ParamountNetworkIE, RedBullTVIE, ESPNIE, DiscoveryGoPlaylistIE, AppleConnectIE, CarambaTVPageIE, HotNewHipHopIE, GlattvisionTVIE, ORFOE1IE, YoutubePlaylistsIE, Porn91IE, VzaarIE, CiscoLiveSearchIE, GoogleSearchIE, TeacherTubeIE, AppleTrailersSectionIE, VubeIE, PacktPubCourseIE, ViideaIE, ToonGogglesIE, LnkGoIE, ArchiveOrgIE, WWEIE, AdobeConnectIE, FilmOnChannelIE, PerformGroupIE, CBSLocalIE, TrailerAddictIE, HRTiPlaylistIE, VimeoWatchLaterIE, ShahidShowIE, MGTVIE, Formula1IE, FreshLiveIE, CondeNastIE, NetzkinoIE, BandcampAlbumIE, BrightcoveNewIE, SevenPlusIE, MyVisionTVIE, TelecincoIE, DPlayIE, DiscoveryNetworksDeIE, AZMedienIE, AWAANSeasonIE, SeekerIE, NRKTVEpisodeIE, PolskieRadioIE, CultureUnpluggedIE, BuzzFeedIE, TV5MondePlusIE, MetacriticIE, XTubeUserIE, KakaoIE, EggheadLessonIE, IviCompilationIE, LinkedInLearningCourseIE, ACastIE, TeamTreeHouseIE, FczenitIE, OnetMVPIE, YandexVideoIE, HistoricFilmsIE, AudioBoomIE, RutubeEmbedIE, MojvideoIE, VimeoAlbumIE, VimeoGroupsIE, DigitallySpeakingIE, SapoIE, RadioJavanIE, VRVIE, WebcasterIE, MySpassIE, ORFFM4IE, MiTeleIE, FrontendMastersCourseIE, OsnatelTVIE, GoIE, UFCTVIE, LRTIE, OnetIE, VineUserIE, MediciIE, WebOfStoriesIE, NDREmbedBaseIE, LimelightChannelIE, RICEIE, DouyuTVIE, JamendoIE, CanalplusIE, QQMusicPlaylistIE, MangomoloVideoIE, Go90IE, BigflixIE, YoutubeSearchDateIE, TruNewsIE, RteRadioIE, TutvIE, ThePlatformIE, TheWeatherChannelIE, SkyNewsArabiaIE, ArteTVInfoIE, TVPlayIE, FranceCultureIE, TNAFlixIE, ARDBetaMediathekIE, DaumClipIE, ScreencastIE, FranceTVIE, VRTIE, ARDMediathekIE, SRMediathekIE, PornHubIE, HistoryTopicIE, InternazionaleIE, NetEaseMusicProgramIE, SunPornoIE, NJoyEmbedIE, NPORadioFragmentIE, JoveIE, GDCVaultIE, TVNowSeasonIE, TeleMBIE, NBCSportsStreamIE, GenerationWhatIE, NJoyIE, TeachableCourseIE, FazIE, HentaiStigmaIE, AuroraVidIE, ThisOldHouseIE, MSNIE, NetEaseMusicIE, NovaIE, MTVIE, CMTIE, BitChuteIE, OoyalaExternalIE, XBefIE, NBCOlympicsStreamIE, PhilharmonieDeParisIE, ChirbitIE, RutubeChannelIE, FirstTVIE, AMCNetworksIE, ServingSysIE, VuClipIE, YoutubeSubscriptionsIE, VeeHDIE, VodlockerIE, UdemyIE, MmsIE, BBCIE, KuwoAlbumIE, NextTVIE, RadioCanadaAudioVideoIE, TV2IE, VimpleIE, YinYueTaiIE, TennisTVIE, RaiPlayLiveIE, AlJazeeraIE, CBCWatchVideoIE, SAKTVIE, SpringboardPlatformIE, OdnoklassnikiIE, TV2HuIE, PornoXOIE, RedditRIE, EightTracksIE, WakanimIE, BIQLEIE, SouthParkIE, SouthParkDeIE, SouthParkNlIE, SouthParkEsIE, SouthParkDkIE, LcpIE, ViceShowIE, AbcNewsIE, TheStarIE, NewgroundsPlaylistIE, TweakersIE, FunimationIE, RadioCanadaIE, TouTvIE, RTVNHIE, VoxMediaVolumeIE, CamModelsIE, KalturaIE, SteamIE, RTVEALaCartaIE, ComCarCoffIE, MgoonIE, TVCIE, ToshIE, RTL2IE, EHowIE, GiantBombIE, HornBunnyIE, VShareIE, MyviEmbedIE, KinoPoiskIE, FranceTVEmbedIE, PlaysTVIE, DotsubIE, TastyTradeIE, MnetIE, NextMediaIE, NextMediaActionNewsIE, CeskaTelevizeIE, PeopleIE, FoxNewsIE, RedTubeIE, TV4IE, VidmeUserLikesIE, PicartoIE, NetEaseMusicAlbumIE, DWArticleIE, VideomoreIE, MofosexIE, XXXYMoviesIE, KaraoketvIE, StreamableIE, NaverIE, NRKTVSeasonIE, RTSIE, SpankBangPlaylistIE, MediasiteIE, BRMediathekIE, TeleBruxellesIE, LimelightMediaIE, FilmwebIE, YoukuIE, LinkedInLearningIE, PlayPlusTVIE, YnetIE, RaiPlayPlaylistIE, FusionIE, RoxwelIE, WeiboMobileIE, Puls4IE, PlaywireIE, LcpPlayIE, TeleQuebecLiveIE, CJSWIE, TOnlineIE, VideofyMeIE, NetPlusIE, NBCSportsVPlayerIE, SVTPlayIE, HitboxLiveIE, KankanIE, NPORadioIE, YoutubeRecommendedIE, VimeoLikesIE, BreakIE, VidmeUserIE, PlaytvakIE, WashingtonPostIE, WalyTVIE, RadioBremenIE, VeohIE, PlayvidIE, TMZArticleIE, LearnrIE, RockstarGamesIE, VineIE, CBCOlympicsIE, FootyRoomIE, NYTimesIE, XVideosIE, VideoDetectiveIE, ViewsterIE, ArteTVFutureIE, NDTVIE, MarkizaPageIE, BiliBiliIE, KanalPlayIE, CtsNewsIE, FunnyOrDieIE, RozhlasIE, CCCPlaylistIE, USANetworkIE, NerdCubedFeedIE, FranceTVInfoIE, ViuIE, MailRuMusicSearchIE, GolemIE, WDRElefantIE, BBCCoUkArticleIE, MwaveMeetGreetIE, SinaIE, SohuIE, BravoTVIE, CinchcastIE, YoutubePlaylistIE, YoutubeWatchLaterIE, LibsynIE, KrasViewIE, MediasiteCatalogIE, KickStarterIE, EngadgetIE, LocalNews8IE, DailymotionUserIE, InfoQIE, OdaTVIE, YoutubeIE, UstudioEmbedIE, UplynkIE, UplynkPreplayIE, YoutubeFavouritesIE, VGTVIE, AcademicEarthCourseIE, VVVVIDIE, MassengeschmackTVIE, TruTVIE, XuiteIE, FranceInterIE, CrunchyrollIE, NetEaseMusicMvIE, RTVEInfantilIE, SmotriCommunityIE, FunkMixIE, CamWithHerIE, ORFIPTVIE, FilmOnIE, NickRuIE, RDSIE, SonyLIVIE, ScrippsNetworksWatchIE, FC2IE, TwitchProfileIE, CTVNewsIE, MyVidsterIE, BBVTVIE, ImgurGalleryIE, ImgurAlbumIE, HuffPostIE, HungamaIE, CloudTimeIE, BloombergIE, KuwoChartIE, YoutubeTruncatedURLIE, TeacherTubeUserIE, KetnetIE, NDREmbedIE, YourPornIE, ShahidIE, ViuPlaylistIE, RottenTomatoesIE, BpbIE, SverigesRadioPublicationIE, MoeVideoIE, ArteTVPlaylistIE, VKIE, ExpoTVIE, KuwoCategoryIE, MiaoPaiIE, YesJapanIE, AENetworksIE, RayWenderlichCourseIE, MegaphoneIE, VimeoUserIE, SoundcloudIE, SoundcloudSearchIE, SoundcloudUserIE, SoundcloudSetIE, SoundcloudTrackStationIE, SoundcloudPlaylistIE, TagesschauPlayerIE, ATTTechChannelIE, BellatorIE, VLiveIE, EbaumsWorldIE, TeamcocoIE, NationalGeographicVideoIE, CliphunterIE, R7IE, UnistraIE, KeekIE, YapFilesIE, SchoolTVIE, AfreecaTVIE, NTVRuIE, RMCDecouverteIE, TuneInShortenerIE, DaumPlaylistIE, QQMusicToplistIE, ORFTVthekIE, WistiaIE, GfycatIE, NJPWWorldIE, MixcloudStreamIE, LiveLeakEmbedIE, TwitchClipsIE, StreetVoiceIE, SyfyIE, RutubeIE, YoutubeUserIE, NickDeIE, NintendoIE, QuicklineLiveIE, HBOIE, UdemyCourseIE, ThisAVIE, CamTubeIE, SeznamZpravyIE, MailRuIE, ThePlatformFeedIE, CBSIE, CBSSportsIE, CorusIE, CBSNewsIE, NRKTVIE, NRKTVDirekteIE, TassIE, PornHubUserVideosIE, PeerTubeIE, YouNowMomentIE, RaiIE, NetEaseMusicListIE, WeiqiTVIE, RestudyIE, VierVideosIE, UOLIE, MixcloudUserIE, TwentyThreeVideoIE, PandoraTVIE, MacGameStoreIE, WashingtonPostArticleIE, SproutIE, TVCArticleIE, LibraryOfCongressIE, ClipsyndicateIE, ScreencastOMaticIE, CrackedIE, LecturioDeCourseIE, PokemonIE, WatchIndianPornIE, ChaturbateIE, TNAFlixNetworkEmbedIE, PacktPubIE, NobelPrizeIE, VKWallPostIE, LivestreamShortenerIE, ReutersIE, MySpaceAlbumIE, YourUploadIE, TurboIE, CartoonNetworkIE, NationalGeographicTVIE, SpiegelIE, LA7IE, NewgroundsIE, BeatportIE, OCWMITIE, NexxIE, CCCIE, CBSInteractiveIE, TechTalksIE, EscapistIE, VidmeIE, VidioIE, YahooGyaOIE, Revision3IE, TwitchPastBroadcastsIE, FlickrIE, InternetVideoArchiveIE, XiamiCollectionIE, TeachingChannelIE, StreamCZIE, RutubePersonIE, DailymotionPlaylistIE, GlideIE, SpiegeltvIE, XiamiSongIE, TVPIE, DemocracynowIE, YouNowChannelIE, NBCNewsIE, StreamangoIE, TVANouvellesArticleIE, PhoenixIE, ITTFIE, FoxgayIE, BTArticleIE, NetEaseMusicDjRadioIE, TDSLifewayIE, BeamProLiveIE, STVPlayerIE, RteIE, VideoPressIE, NHLIE, GameOneIE, XimalayaAlbumIE, RUTVIE, HotStarPlaylistIE, XboxClipsIE, ToypicsIE, EaglePlatformIE, OnetChannelIE, SlideshareIE, ComedyCentralTVIE, ADNIE, FuxIE, PressTVIE, NBCSportsIE, ThreeQSDNIE, SaltTVIE, MovingImageIE, ImdbIE, NineNowIE, SVTIE, ZattooLiveIE, NprIE, MixcloudPlaylistIE, DropboxIE, TVANouvellesIE, GaiaIE, BRIE, TunePkIE, NoovoIE, CanvasIE, MotherlessIE, VH1IE, AdobeTVChannelIE, ChilloutzoneIE, DaumUserIE, PhotobucketIE, PatreonIE, EveryonesMixtapeIE, AudiomackAlbumIE, BaiduVideoIE, OnionStudiosIE, ViewLiftEmbedIE, Revision3EmbedIE, BlinkxIE, XMinusIE, MyviIE, EWETVIE, VrtNUIE, MLBIE, EchoMskIE, VimeoReviewIE, WallaIE, ClubicIE, LetvCloudIE, MySpaceIE, SharedIE, ArteTVMagazineIE, RTPIE, SmotriBroadcastIE, TestURLIE, TBSIE, ViuOTTIE, LivestreamIE, VODPlatformIE, InstagramIE, OutsideTVIE, NRKTVEpisodesIE, BambuserIE, DailyMailIE, TumblrIE, HuajiaoIE, NickNightIE, AdobeTVVideoIE, SmotriIE, MinistryGridIE, CBCPlayerIE, VyboryMosIE, XiamiAlbumIE, AbcNewsVideoIE, SpankBangIE, ITVBTCCIE, TuneInStationIE, BrightcoveLegacyIE, UrortIE, MNetTVIE, RTL2YouSeriesIE, AppleDailyIE, IwaraIE, HetKlokhuisIE, EmbedlyIE, LinuxAcademyIE, NPOIE, WNLIE, AndereTijdenIE, MioMioIE, ArteTVCinemaIE, AdultSwimIE, IGNIE, PCMagIE, OneUPIE, ACastChannelIE, LineTVIE, VPROIE, PuhuTVIE, MwaveIE, CWTVIE, HotStarIE, TwitterAmplifyIE, GenericIE]
