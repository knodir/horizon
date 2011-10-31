# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2011 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
# Copyright 2011 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Views for home page.
"""
from django import template
from django import shortcuts
from django.views.decorators import vary

import horizon
from horizon.views import auth as auth_views


def user_home(user):
    if user.admin:
        return horizon.get_dashboard('syspanel').get_absolute_url()
    return horizon.get_dashboard('dash').get_absolute_url()


@vary.vary_on_cookie
def splash(request):
    form, handled = auth_views.Login.maybe_handle(request)
    if handled:
        return handled

    return shortcuts.render(request, 'splash.html', {'form': form})
