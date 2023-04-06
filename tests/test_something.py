import requests

from conf.configuration import SERVICE_URL

from src.enums.global_enums import GlobalErrorMessages
from src.baseclasses.responce import Response
from src.schemas.post import POST_SCHEMA


def test_getting_post():
    check_res = requests.get(url=SERVICE_URL)
    response = Response(check_res)

    response.assert_status_code(200).check_validate(POST_SCHEMA)



