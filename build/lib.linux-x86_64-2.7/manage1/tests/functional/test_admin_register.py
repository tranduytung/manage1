from manage1.tests import *

class TestRegisterController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='admin/register', action='index'))
        # Test response...
