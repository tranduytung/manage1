from manage1.tests import *

class TestFullcalendarController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='fullcalendar', action='index'))
        # Test response...
