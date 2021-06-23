from mptt.admin import DraggableMPTTAdmin
from .models import *
from django.contrib import admin
from .models import Internet


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']
    search_fields = ('title',)


class InternetAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_filter = ('company',)
    search_fields = ('title',)

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


class TarifAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_filter = ('company',)
    search_fields = ('title',)

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
    list_display = ['nomi','internet', 'company']
    list_filter = ('company',)

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['hajmi'].label = 'Hajmi (MB)'
        form.base_fields['narxi'].label = 'Narxi (UZS)'
        return form
    autocomplete_fields = ('internet', 'company')


class T_PaketAdmin(admin.ModelAdmin):
    list_display = ['nomi','tariflar', 'company']
    autocomplete_fields = ('tariflar', 'company')
    list_filter = ('company',)
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['muddati'].label = 'Muddati (kun)'
        form.base_fields['narxi'].label = 'Narxi (UZS)'
        return form


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
