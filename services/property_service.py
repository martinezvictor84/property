from .habi_db import HabiDb


def get_filter(params):
    filter = {}
    if params.get('status_id'):
        filter['status_id'] = params.get('status_id')
    if params.get('year'):
        filter['year'] = params.get('year')
    if params.get('city'):
        filter['city'] = params.get('city')
    return filter


class PropertyService:
    def __init__(self):
        self.habi_db = HabiDb()

    def get_properties(self, params):
        try:
            filters = get_filter(params)
        except Exception as e:
            raise FilterError(str(e))
        return self.habi_db.get_properties(filters)


class FilterError(Exception):
    pass
