from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings

from libmondo import MondoOauthClient, MondoSessionClient
from libbitmondo import BitMondoClient


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
    bitmondo = BitMondoClient(mondo_session, account_id)
    bitmondo.incoming_payment('1Bdii7sGaE2i6AFUPThTCoFsXWKJdSJ955',
                              '1MNe417Sx3WGtbdcZg2v8wnBPodkbsL1R8',
                              6.543,
                              '16aef80dd4cfd5fe717f19151f9bd9491b13c30171bacdd96a6ab6366459fbe')
    bitmondo.outgoing_payment('1Bdii7sGaE2i6AFUPThTCoFsXWKJdSJ955',
                              '1MNe417Sx3WGtbdcZg2v8wnBPodkbsL1R8',
                              6.543,
                              '16aef80dd4cfd5fe717f19151f9bd9491b13c30171bacdd96a6ab6366459fbe')
    a
    return HttpResponseRedirect('/mondo')


