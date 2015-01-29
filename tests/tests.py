from __future__ import unicode_literals

from contextlib import contextmanager
import time

from django import forms
from django.conf import settings
from django.contrib.admin import site
from django.contrib.admin.tests import AdminSeleniumWebDriverTestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import SimpleTestCase

from admin_enhancer import widgets

from .models import Book


class InteractionTest(AdminSeleniumWebDriverTestCase):
    available_apps = settings.INSTALLED_APPS

    def setUp(self):
        super(InteractionTest, self).setUp()
        User.objects.create_superuser('super', '', 'secret')

    def wait_for_popup(self, name):
        def popup_is_loaded(driver):
            return driver.current_window_handle == name
        self.wait_until(popup_is_loaded)

    @contextmanager
    def handle_popup(self, trigger):
        initial_window_handle = self.selenium.current_window_handle
        window_handles = set(self.selenium.window_handles)
        try:
            trigger()
            self.wait_until(lambda driver: set(driver.window_handles) != window_handles)
            new_window_handle = (set(self.selenium.window_handles) - window_handles).pop()
            self.selenium.switch_to.window(new_window_handle)
            yield new_window_handle
        finally:
            time.sleep(1)
            self.selenium.switch_to.window(initial_window_handle)

    def test_widget_interactions(self):
        self.admin_login('super', 'secret')
        driver = self.selenium
        driver.set_page_load_timeout(10)
        driver.get("%s%s" % (self.live_server_url, reverse('admin:tests_book_add')))

        author_select = driver.find_element_by_id('id_author')
        edit_author_btn = driver.find_element_by_id('edit_id_author')
        add_author_btn = driver.find_element_by_id('add_id_author')
        delete_author_btn = driver.find_element_by_id('delete_id_author')

        self.assertIsNone(edit_author_btn.get_attribute('href'))
        self.assertIsNone(delete_author_btn.get_attribute('href'))

        def author_options():
            author_options = author_select.find_elements_by_tag_name('option')
            options_label = []
            selected_option_label = None
            for option in author_options:
                label = option.get_attribute('innerHTML')
                options_label.append(label)
                if option.get_attribute('selected'):
                    selected_option_label = label
            return selected_option_label, options_label

        def interact(button, name):
            with self.handle_popup(button.click):
                driver.implicitly_wait(1)
                driver.find_element_by_id('id_name').clear()
                driver.find_element_by_id('id_name').send_keys(name)
                driver.find_element_by_name('_save').click()
            selected_option_label, options_label = author_options()
            self.assertEqual(['---------', name], options_label)
            self.assertEqual(name, selected_option_label)

        interact(add_author_btn, 'David Abraham')

        self.assertIsNotNone(edit_author_btn.get_attribute('href'))
        self.assertIsNotNone(delete_author_btn.get_attribute('href'))

        interact(edit_author_btn, 'David Abram')

        with self.handle_popup(delete_author_btn.click):
            driver.find_element_by_css_selector('input[type="submit"]').click()

        selected_option_label, options_label = author_options()
        self.assertEqual(['---------'], options_label)
        self.assertEqual('---------', selected_option_label)

        self.assertIsNone(edit_author_btn.get_attribute('href'))
        self.assertIsNone(delete_author_btn.get_attribute('href'))


class RelatedFieldWidgetWrapperTests(SimpleTestCase):
    def test_select_multiple_widget_cant_change_delete_related(self):
        rel = Book._meta.get_field('themes').rel
        widget = forms.SelectMultiple()
        wrapper = widgets.RelatedFieldWidgetWrapper(
            widget, rel, site,
            can_add_related=True,
            can_change_related=True,
            can_delete_related=True,
        )
        self.assertTrue(wrapper.can_add_related)
        self.assertFalse(wrapper.can_change_related)
        self.assertFalse(wrapper.can_delete_related)

    def test_on_delete_cascade_rel_cant_delete_related(self):
        rel = Book._meta.get_field('collection').rel
        widget = forms.Select()
        wrapper = widgets.RelatedFieldWidgetWrapper(
            widget, rel, site,
            can_add_related=True,
            can_change_related=True,
            can_delete_related=True,
        )
        self.assertTrue(wrapper.can_add_related)
        self.assertTrue(wrapper.can_change_related)
        self.assertFalse(wrapper.can_delete_related)
