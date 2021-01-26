from oauthlib.oauth2 import WebApplicationClient

from myapp.config import GOOGLE_CLIENT_ID

client = WebApplicationClient(GOOGLE_CLIENT_ID)
