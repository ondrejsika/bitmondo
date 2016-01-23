from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.core.urlresolvers import reverse

from libmondo import MondoOauthClient, MondoSessionClient
from libbitmondo import BitMondoClient
from libbitcoin import get_balance

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
    return HttpResponseRedirect(reverse('mondo:home'))


def logout_view(request):
    del request.session['account_id']
    return HttpResponseRedirect(reverse('mondo:home'))


def deactivate_view(request):
    account, created = MondoAccount.objects.get_or_create(
        id=request.session['account_id'],
    )
    account.bitcoinaddress_set.all().delete()
    account.delete()

    del request.session['account_id']
    return HttpResponseRedirect(reverse('mondo:home'))


def address_add_view(request):
    account = MondoAccount.objects.get(id=request.session.get('account_id'))

    raw_address = request.POST.get('address')
    address, created = BitcoinAddress.objects.get_or_create(account=account, address=raw_address,
                                                            last_balance=get_balance(raw_address))
    address.save()
    return HttpResponseRedirect(reverse('mondo:home'))


def address_remove_view(request):
    account = MondoAccount.objects.get(id=request.session.get('account_id'))

    raw_address = request.GET.get('address')
    address = BitcoinAddress.objects.get(account=account, address=raw_address)
    address.delete()
    return HttpResponseRedirect(reverse('mondo:home'))
