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


class TestUserprofile(unittest.TestCase):

    def test_get_user_profile(self):
        header = {'Authorization': get_authorization_token()}

        response = requests.get(f'{URL}/user-profile', headers=header)
        assert response.status_code == 200

        json_data = json.loads(response.content)
        languages = json_data['languages']
        timezones = json_data['timezones']

        pt_language = languages[0]
        assert_in('id', pt_language)
        assert_equal(type(pt_language['id']), int)
        assert_equal(pt_language['id'], 1)

        assert_in('name', pt_language)
        assert_equal(type(pt_language['name']), str)
        assert_equal(pt_language['name'], 'Português')

        assert_in('code', pt_language)
        assert_equal(type(pt_language['code']), str)
        assert_equal(pt_language['code'], 'pt')

        en_language = languages[1]
        assert_in('id', en_language)
        assert_equal(type(en_language['id']), int)
        assert_equal(en_language['id'], 2)

        assert_in('name', en_language)
        assert_equal(type(en_language['name']), str)
        assert_equal(en_language['name'], 'English')

        assert_in('code', en_language)
        assert_equal(type(en_language['code']), str)
        assert_equal(en_language['code'], 'en')

        es_language = languages[2]
        assert_in('id', es_language)
        assert_equal(type(es_language['id']), int)
        assert_equal(es_language['id'], 3)

        assert_in('name', es_language)
        assert_equal(type(es_language['name']), str)
        assert_equal(es_language['name'], 'Español')

        assert_in('code', es_language)
        assert_equal(type(es_language['code']), str)
        assert_equal(es_language['code'], 'es')

        tzone_element = timezones[0]
        assert_in('id', tzone_element)
        assert_equal(type(tzone_element['id']), int)

        assert_in('name', tzone_element)
        assert_equal(type(tzone_element['name']), str)

        assert_in('timeAdjustment', tzone_element)
        assert_equal(type(tzone_element['timeAdjustment']), str)

        assert_in('active', tzone_element)
        assert_equal(type(tzone_element['active']), bool)



