import requests

from conf.configuration import SERVICE_URL_2

from src.baseclasses.responce import Response
from src.schemas_service_url2.user import User


def test_getting_user():
    response = requests.get(SERVICE_URL_2)
    test_object = Response(response)
    test_object.assert_status_code(200).check_validate(User)