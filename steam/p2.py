"""
Module for reading Portal 2 data using the Steam API

Copyright (c) 2010, Anthony Garcia <lagg@lavabit.com>

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
"""

import items

_APP_ID = 620

class backpack(items.backpack):
    def __init__(self, sid, **kwargs):
        super(backpack, self).__init__(_APP_ID, sid, **kwargs)

class item_schema(items.schema):
    def __init__(self, **kwargs):
        super(item_schema, self).__init__(_APP_ID, item_type = item, **kwargs)

class item(items.item):
    def get_full_item_name(self, prefixes = None):
        return items.item.get_full_item_name(self, None)

    def get_equipped_classes(self):
        """ The `equipped' field isn't exposed in Portal 2
        for one (probably silly) reason or another. So we still use the inventory
        token """
        inventory_token = self.get_inventory_token()
        classes = []

        equipped = ((inventory_token & self.equipped_field) >> 16)
        if equipped == 3: classes = [1, 2]
        elif equipped > 0: classes = [equipped]

        return classes

    def __init__(self, schema, init_item):
        super(item, self).__init__(schema, init_item)
