from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import *


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']


class InternetAdmin(admin.ModelAdmin):
    list_display = ['title', 'company']


class InternetAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Internet.objects.add_related_count(
            qs,
            I_Paket,
            'internet',
            'products_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = Internet.objects.add_related_count(qs,
                                                I_Paket,
                                                'internet',
                                                'products_count',
                                                cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count

    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count

    related_products_cumulative_count.short_description = 'Related products (in tree)'


class TarifAdmin(admin.ModelAdmin):
    list_display = ['tariflar', 'nomi', 'muddati', 'narxi']


class TarifAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Internet.objects.add_related_count(
            qs,
            T_Paket,
            'tariflar',
            'products_cumulative_count',
            cumulative=True)

        # Add non cumulative product count
        qs = Internet.objects.add_related_count(qs,
                                                T_Paket,
                                                'tariflar',
                                                'products_count',
                                                cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count

    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count

    related_products_cumulative_count.short_description = 'Related products (in tree)'


class I_PaketAdmin(admin.ModelAdmin):
    list_display = ['internet', 'company', 'nomi']


class T_PaketAdmin(admin.ModelAdmin):
    list_display = ['tariflar', 'company', 'nomi']


admin.site.register(Internet, InternetAdmin2)
admin.site.register(Tariflar, TarifAdmin2)
admin.site.register(Company, CompanyAdmin)
admin.site.register(T_Paket, T_PaketAdmin)
admin.site.register(I_Paket, I_PaketAdmin)
admin.site.register(SMS_Paket)
admin.site.register(SMS)
admin.site.register(Foydali)
admin.site.register(F_Paket)
admin.site.register(Xizmatlar)
admin.site.register(X_Paket)
admin.site.register(Daqiqalar)
admin.site.register(D_Paket)
