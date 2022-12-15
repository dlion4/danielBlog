from django.contrib import admin
from .models import Advert, AdvertImage

# custom actions

def make_paid(request, modelname, queryset):
    queryset.update(is_paid=True)
make_paid.shortdescription = "Make Ad Paid"


def revoke_payment(request, modelname, queryset):
    queryset.update(is_paid=False)
revoke_payment.shortdescription = "Revoke Payment"

# Register your models here.

class AdvertAdminImageInlines(admin.StackedInline):
    model = AdvertImage
    extra = 0
    
    
@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ("name", "source", "is_paid", "url")
    inlines = [AdvertAdminImageInlines, ]
    list_filter = ("is_paid", "source")
    search_fields = ("source", "name")
    actions = [make_paid, revoke_payment]
    fieldsets = (
        ("Mandatory Field", {
            "fields": (
                "name",
                "source",
                "url",
            ),
        }),
    )
    