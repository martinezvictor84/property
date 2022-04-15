from .habi_db import HabiDb


def get_filter(params):
    filter_map = {
        "status_id": {'column': 'status_id', 'condition': '='},
        "year_gte": {'column': 'year', 'condition': '>='},
        "year_lte": {'column': 'year', 'condition': '<='},
        "price_gte": {'column': 'price', 'condition': '>='},
        "price_lte": {'column': 'price', 'condition': '<='},
        "city": {'column': 'city', 'condition': '='}
    }
    return {key: {
                'value': params.get(key),
                'column': filter_map[key]['column'],
                'condition': filter_map[key]['condition']
            } for key, value in filter_map.items() if params.get(key)}


class PropertyService:
    def __init__(self):
        self.habi_db = HabiDb()

    def get_properties(self, params):
        try:
            filters = get_filter(params)
            per_page = params.get('per_page', 50)
            page = params.get('page', 1)
        except Exception as e:
            raise FilterError(str(e))
        return self.habi_db.get_properties(filters, page, per_page)


class FilterError(Exception):
    pass
