from django import forms

from django.utils.translation import gettext_lazy
from django.utils.translation import ugettext_lazy


class MyForm(forms.Form):
    gettext_lazy_translated = forms.CharField(
        label=gettext_lazy("gettext_lazy translated"),
        required=True,
        widget=forms.TextInput(attrs={"placeholder": gettext_lazy("gettext_lazy")}),
    )
    ugettext_lazy_translated = forms.CharField(
        label=ugettext_lazy("ugettext_lazy translated"),
        required=True,
        widget=forms.TextInput(attrs={"placeholder": ugettext_lazy("ugettext_lazy")}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["gettext_lazy_translated_custom_init"] = forms.CharField(
            label=gettext_lazy("gettext_lazy init - NOT translated"),
            widget=forms.TextInput(
                attrs={"placeholder": gettext_lazy("Won't be in translations")}
            ),
        )
        self.fields["ugettext_lazy_translated_custom_init"] = forms.CharField(
            label=gettext_lazy("ugettext_lazy init - translated"),
            widget=forms.TextInput(
                attrs={"placeholder": ugettext_lazy("Will be in translations")}
            ),
        )
