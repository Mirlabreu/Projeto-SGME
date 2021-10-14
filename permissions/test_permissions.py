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


class TestPermissions(unittest.TestCase):

    def test_get_permissions(self):
        header = {'Authorization': get_authorization_token()}

        response = requests.get(f'{URL}/permissions', headers=header)
        assert response.status_code == 200

        json_data = json.loads(response.content)

        first_element = json_data[0]
        assert_in('id', first_element)
        assert_equal(type(first_element['id']), int)

        assert_in('name', first_element)
        assert_equal(type(first_element['name']), str)

        assert_in('adviser', first_element)
        assert_equal(type(first_element['adviser']), bool)

        assert_in('achiever', first_element)
        assert_equal(type(first_element['achiever']), bool)

        assert_in('administrator', first_element)
        assert_equal(type(first_element['administrator']), bool)

        assert_in('coordinator', first_element)
        assert_equal(type(first_element['coordinator']), bool)

        assert_in('active', first_element)
        assert_equal(type(first_element['active']), bool)

        assert_in('tag', first_element)
        assert_equal(type(first_element['tag']), str)
