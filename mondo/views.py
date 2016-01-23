from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.core.urlresolvers import reverse

from libmondo import MondoOauthClient, MondoSessionClient
from libbitmondo import BitMondoClient

from mondo.models import MondoAccount, BitcoinAddress


mondo_client = MondoOauthClient(
    settings.MONDO_AUTH_URL,
    settings.MONDO_API_URL,
    settings.MONDO_CLIENT_ID,
    settings.MONDO_CLIENT_SECRET,
    settings.MONDO_REDIRECT_URL,
)


def home_view(request):
    if request.session.get('account_id'):
        account = MondoAccount.objects.get(id=request.session.get('account_id'))
    else:
        account = None

    addresses = []
    if account:
        addresses = account.bitcoinaddress_set.all()

    return render(request, 'home.html', {
        'mondo_auth_url': mondo_client.get_auth_link('somerandom'),
        'account': account,
        'addresses': addresses,
    })


def authorize_view(request):
    token = mondo_client.get_token(request.GET['code'])
    mondo_session = MondoSessionClient(mondo_client, token)
    account_id = mondo_session.get_accounts()['accounts'][0]['id']

    account, created = MondoAccount.objects.get_or_create(
        username='ondrejsika@ondrejsika.com',
        # token=token,
        account_id=account_id,
    )
    account.token = token
    account.save()
    request.session['account_id'] = account.id

    # bitmondo = BitMondoClient(mondo_session, account_id)
    # bitmondo.incoming_payment('1Bdii7sGaE2i6AFUPThTCoFsXWKJdSJ955',
    #                           '1MNe417Sx3WGtbdcZg2v8wnBPodkbsL1R8',
    #                           6.543,
    #                           '16aef80dd4cfd5fe717f19151f9bd9491b13c30171bacdd96a6ab6366459fbe')
    # bitmondo.outgoing_payment('1Bdii7sGaE2i6AFUPThTCoFsXWKJdSJ955',
    #                           '1MNe417Sx3WGtbdcZg2v8wnBPodkbsL1R8',
    #                           6.543,
    #                           '16aef80dd4cfd5fe717f19151f9bd9491b13c30171bacdd96a6ab6366459fbe')
    return HttpResponseRedirect(reverse('mondo:home'))

def logout_view(request):
    del request.session['account_id']
    return HttpResponseRedirect(reverse('mondo:home'))

def deactivate_view(request):
    account, created = MondoAccount.objects.get_or_create(
        username=request.session['account_id'],
    )
    account.delete()

    del request.session['account_id']
    return HttpResponseRedirect(reverse('mondo:home'))
