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


class TestProfiles(unittest.TestCase):


    def test_get_profiles(self):
        header = {'Authorization': get_authorization_token()}

        response = requests.get(f'{URL}/profiles', headers=header)
        assert response.status_code == 200

        json_data = json.loads(response.content)

        pfl_administrator = json_data[0]
        assert_in('id', pfl_administrator)
        assert_equal(type(pfl_administrator['id']), int)
        assert_equal(pfl_administrator['id'], 1)

        assert_in('name', pfl_administrator)
        assert_equal(type(pfl_administrator['name']), str)
        assert_equal(pfl_administrator['name'], 'Administrator')

        assert_in('type', pfl_administrator)
        assert_equal(type(pfl_administrator['type']), str)
        assert_equal(pfl_administrator['type'], 'ADMINISTRATOR')

        pfl_achiever = json_data[1]
        assert_in('id', pfl_achiever)
        assert_equal(type(pfl_achiever['id']), int)
        assert_equal(pfl_achiever['id'], 2)

        assert_in('name', pfl_achiever)
        assert_equal(type(pfl_achiever['name']), str)
        assert_equal(pfl_achiever['name'], 'Achiever')

        assert_in('type', pfl_achiever)
        assert_equal(type(pfl_achiever['type']), str)
        assert_equal(pfl_achiever['type'], 'ACHIEVER')

        pfl_adviser = json_data[2]
        assert_in('id', pfl_adviser)
        assert_equal(type(pfl_adviser['id']), int)
        assert_equal(pfl_adviser['id'], 3)

        assert_in('name', pfl_adviser)
        assert_equal(type(pfl_adviser['name']), str)
        assert_equal(pfl_adviser['name'], 'Adviser')

        assert_in('type', pfl_adviser)
        assert_equal(type(pfl_adviser['type']), str)
        assert_equal(pfl_adviser['type'], 'ADVISER')

        pfl_coordinator = json_data[3]
        assert_in('id', pfl_coordinator)
        assert_equal(type(pfl_coordinator['id']), int)
        assert_equal(pfl_coordinator['id'], 4)

        assert_in('name', pfl_coordinator)
        assert_equal(type(pfl_coordinator['name']), str)
        assert_equal(pfl_coordinator['name'], 'Coordinator')

        assert_in('type', pfl_coordinator)
        assert_equal(type(pfl_coordinator['type']), str)
        assert_equal(pfl_coordinator['type'], 'COORDINATOR')


