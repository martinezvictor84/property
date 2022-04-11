from services.property_service import PropertyService
import json


def property_handler(event, contex=None):
    config = get_settings()
    params = event['queryStringParameters'] or {}
    service = PropertyService(config)
    res = service.get_properties(params)
    return response_json(200, res)


def get_settings():
    f = open('resources/config.json')
    return json.load(f)


def response_json(status_code: int, body: dict):
    return {
        "statusCode": status_code,
        "body": json.dumps(body)
    }


if __name__ == '__main__':
    filters = {
        'status_id': 1,
        'year': 2000,
        'city': 'bogota'

    }
    data = property_handler({'queryStringParameters': filters}, None)
    print(data)