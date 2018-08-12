import os

from betamax import Betamax
from betamax_serializers import pretty_json
from decouple import config


class Config:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DEBUG = config('DEBUG', default=False, cast=bool)
    # Database config
    SQLITE_URL_DEFAULT = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    DATABASE_URL = config('DATABASE_URL', default=SQLITE_URL_DEFAULT)
    # Betamax config
    CASSETTES_DIR = os.path.join(BASE_DIR, u'resources', u'cassettes')
    MATCH_REQUESTS_ON = [u'method', u'uri', u'path', u'query']
    config = Betamax.configure()

    def __init__(self):
        Betamax.register_serializer(pretty_json.PrettyJSONSerializer)
        self.config.cassette_library_dir = self.CASSETTES_DIR
        self.config.default_cassette_options[u'serialize_with'] = u'prettyjson'
        self.config.default_cassette_options[u'match_requests_on'] = self.MATCH_REQUESTS_ON
        self.config.default_cassette_options[u'preserve_exact_body_bytes'] = True
