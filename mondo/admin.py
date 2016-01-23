from django.contrib import admin

from mondo.models import MondoAccount, BitcoinAddress


admin.site.register(MondoAccount)
admin.site.register(BitcoinAddress)

