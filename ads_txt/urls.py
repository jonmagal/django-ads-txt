from django.urls import re_path

from ads_txt.views import rules_list

urlpatterns = [
    re_path(r'^$', rules_list, name='ads_txt_rule_list'),
]
