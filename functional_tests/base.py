from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import sys


class FunctionalTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        self.outputdir = '/home/rosien/projects/tdd'
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = '/usr/bin/google-chrome'
        self.service_log_path = "{}/chromedriver.log".format(self.outputdir)
        self.service_args = ['--verbose']
        self.browser = webdriver.Chrome('/home/rosien/chromedriver',
                                        chrome_options=self.options,
                                        service_args=self.service_args,
                                        service_log_path=self.service_log_path)

        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])