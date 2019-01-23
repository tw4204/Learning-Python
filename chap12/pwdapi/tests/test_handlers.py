import json
from unittest.mock import patch
from nose.tools import assert_dict_equal, assert_equal
import falcon
import falcon.testing as testing
from core.handlers import(
    PasswordValidatorHandler, PasswordGeneratorHandler
)


class PGHTest(PasswordGeneratorHandler):
    def process_request(self, req, resp):
        self.req, self.resp = req, resp
        return super(PGHTest, self).process_request(req, resp)


class PVHTest(PasswordValidatorHandler):
    def process_request(self, req, resp):
        self.req, self.resp = req, resp
        return super(PVHTest, self).process_request(req, resp)


class TestPasswordValidatorHandler(testing.TestBase):
    def before(self):
        self.resource = PVHTest()
        self.api.add_route('/password/validate/', self.resource)

    def test_post(self):
        self.simulate_request(
            '/password/validate',
            body=json.dumps(
                {'password': 'abcABC0123#&'}
            ),
            method='POST'
        )
        resp = self.resource.resp

        assert_equal('200 OK', resp.status)
        assert_dict_equal(
            {'password': 'abcABC0123#&',
                'score': {
                    'case': 3, 'length': 5, 'numbers': 2,
                    'special': 4, 'ratio': 2, 'total': 16
                },
                'valid': True
            },
            json.loads(resp.body)
        )

class TestPasswordGeneratorHandler(testing.TestBase):
    def before(self):
        self.resource = PGHTest()
        self.api.add_route('/password/generate/', self.resource)

    @patch('core.handlers.PasswordGenerator')
    def test_get(self, PasswordGenerator):
        PasswordGenerator.generate.return_value = (7, 'abc123')
        self.simulate_request(
            '/password/generate/',
            query_string='length=7',
            method='GET'
        )
        resp = self.resource.resp

        assert_equal('200 OK', resp.status)
        assert_equal([7, 'abc123'], json.loads(resp.body))

