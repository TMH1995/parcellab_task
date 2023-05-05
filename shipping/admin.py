from django.contrib import admin
from shipping.models import Shipment,Origin,Temperature,Address,Article


class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('tracking_number', 'carrier','sender_address', 'receiver_address','article','article_quantity','article_quantity')
    list_filter=['carrier']
    fields = ('tracking_number', 'carrier','sender_address', 'receiver_address','article','article_quantity')
    search_fields = ['tracking_number','carrier','article__name']


class TemperatureAdmin(admin.ModelAdmin):
    # list_display = ('degree','origin')
    readonly_fields = ('updated_at',)
admin.site.register(Shipment,ShipmentAdmin)

admin.site.register(Origin)
admin.site.register(Temperature,TemperatureAdmin)
admin.site.register(Address)
admin.site.register(Article)