import urllib
import requests


class MondoOauthClientBase(object):
    class MondoError(Exception):
        pass

    def __init__(self, auth_url, api_url, client_id, client_secret, redirect_url):
        self._auth_url = auth_url
        self._api_url = api_url
        self._client_id = client_id
        self._client_secret = client_secret
        self._redirect_url = redirect_url

    def get_auth_link(self, state):
        """
        Create auth link
        """
        return '%s?%s' % (self._auth_url, urllib.urlencode({
            'client_id': self._client_id,
            'state': state,
            'response_type': 'code',
            'redirect_uri': self._redirect_url,
        }))

    def get_token(self, code):
        """
        Returns Bearer token
        """
        r = requests.post(self._api_url + '/oauth2/token', data={
            'grant_type': 'authorization_code',
            'client_id': self._client_id,
            'client_secret': self._client_secret,
            'redirect_uri': self._redirect_url,
            'code': code,
        })
        try:
            return r.json()['access_token']
        except Exception, e:
            raise self.MondoError(e)

    def request(self, token, method, path, data=None):
        r = requests.request(
            method,
            self._api_url+path,
            headers={
                'Authorization': 'Bearer %s' % token,
            },
            data=data,
        )
        try:
            return r.json()
        except Exception, e:
            raise self.MondoError(e)


class MondoOauthClient(MondoOauthClientBase):
    def get_accounts(self, token):
        return self.request(token, 'GET', '/accounts')

    def create_feed_item(self, token, account_id, title, body, image_url, url, title_color,
                         body_color, background_color):
        return self.request(token, 'POST', '/feed', {
            'account_id': account_id,
            'type': 'basic',
            'url': url,
            'params[title]': title,
            'params[image_url]': image_url,
            'params[background_color]': background_color,
            'params[body_color]': body_color,
            'params[title_color]': title_color,
            'params[body]': body,
        })


class MondoSessionClient(object):
    def __init__(self, oauth_client, token):
        self._oauth_client = oauth_client
        self._token = token

    def __getattr__(self, item):
        return lambda *args, **kwargs: getattr(self._oauth_client, item)(self._token, *args, **kwargs)


__all__ = ['MondoOauthClient', 'MondoSessionClient']
