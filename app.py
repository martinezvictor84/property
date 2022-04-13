from services.property_service import PropertyService
from services.property_service import FilterError
import json
import logging


def property_handler(event, contex=None):
    params = event['queryStringParameters'] or {}
    try:
        service = PropertyService()
        res = service.get_properties(params)
        return response_json(200, res)
    except FilterError:
        return response_json(400, {'message': 'bad request'})
    except Exception as e:
        logging.error(str(e))
        return response_json(500, {
            'message': 'an error has occurred, please try'
                       ' again or contact support'})


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