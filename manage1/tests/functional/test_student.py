from manage1.tests import *

class TestStudentController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='student', action='index'))
        # Test response...
