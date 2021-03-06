DATABASE_AUTO_CREATE_INDEX = True
DATABASE_SUPPORT_AWS_DOCUMENT_DB = False
DATABASES = {
    'default': {
        'db': 'secret',
        'host': 'localhost',
        'port': 27017,
        'username': '',
        'password': ''
    }
}

CACHES = {
    'default': {},
    'local': {
        'backend': 'spaceone.core.cache.local_cache.LocalCache',
        'max_size': 128,
        'ttl': 86400
    }
}

HANDLERS = {}

CONNECTORS = {
    'IdentityConnector': {},
    'AWSSecretManagerConnector': {},
    'VaultConnector': {
#        url = 'http://vault:8200',
#        token = 'myroot'
    }
}

ENDPOINTS = {}

LOG = {}

