import sys

from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

# FIXME - Comments should all be writting with effective grammar and punctuation.
# FIXME - Remove hardcoded URLs from views.py
# FIXME - Remove hardcoded URL from forms in list.html and home.html


class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'live_server_url'):
            if cls.server_url == cls.live_server_url:
                super().tearDownClass()

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_text_in_list_of_table_rows(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
