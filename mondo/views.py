from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings

from libmondo import MondoOauthClient, MondoSessionClient


mondo_client = MondoOauthClient(
    settings.MONDO_AUTH_URL,
    settings.MONDO_API_URL,
    settings.MONDO_CLIENT_ID,
    settings.MONDO_CLIENT_SECRET,
    settings.MONDO_REDIRECT_URL,
)


@login_required
def home_view(request):
    return render(request, 'home.html', {
        'mondo_auth_url': mondo_client.get_auth_link('somerandom'),
    })


@login_required
def authorize_view(request):
    token = mondo_client.get_token(request.GET['code'])
    mondo_session = MondoSessionClient(mondo_client, token)
    account_id = mondo_client.get_accounts(token)['accounts'][0]['id']
    print account_id
    print token
    print mondo_session.create_feed_item(
        account_id,
        'hello',
        'from London',
        'https://bitstickers.net/wp-content/uploads/2013/12/btc-orange.jpg',
        'https://blockchain.info/address/1K8jWKBgWU2L1zvBbTn4G3vMyJx8Ra1J6G',
        '#000',
        '#000',
        '#FFF',
    )

    return HttpResponseRedirect('/mondo')


