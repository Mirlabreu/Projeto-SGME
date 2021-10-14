import json
import os
import requests
from nose.tools import *
import sys
import unittest

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_dir = os.path.join(ROOT_DIR, 'utils')
sys.path.append(path_dir)

from main_functions import *


class TestTimezone(unittest.TestCase):

    def test_get_timezone(self):
        header = {'Authorization': get_authorization_token()}

        response = requests.get(f'{URL}/timezone', headers=header)
        assert response.status_code == 200

        json_data = json.loads(response.content)

        tzone_element = json_data[0]
        assert_in('id', tzone_element)
        assert_equal(type(tzone_element['id']), int)

        assert_in('name', tzone_element)
        assert_equal(type(tzone_element['name']), str)

        assert_in('timeAdjustment', tzone_element)
        assert_equal(type(tzone_element['timeAdjustment']), str)

        assert_in('active', tzone_element)
        assert_equal(type(tzone_element['active']), bool)
