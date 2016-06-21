from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html', request=request) # added to fix unexpected error re csrf token
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
            request = HttpRequest()
            request.method = 'POST'
            request.POST['item_text'] = 'A new list item'

            response = home_page(request)

            # code below: request = request is to fix the unexpected error triggered by a csrf token issue in django 1.9
            expected_html = render_to_string(
                'home.html',
                {'new_item_text': 'A new list item'},
                request=request
            )
            self.assertEqual(response.content.decode(), expected_html)


