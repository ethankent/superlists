from unittest import skip

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidently tries to submit an empty list item.
        # She hits ENTER on the empty input box.
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        # The home page refreshes and displays an error message similar to: "List items cannot be blank."
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # Edith tries again with some text for the item. This time it works.
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk\n')
        self.check_for_text_in_list_of_table_rows('1: Buy milk')

        # Curious to see what will happen if she does it again, she decides to submit a second blank item.
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        # She recieves a similar warning on the list view page.
        self.check_for_text_in_list_of_table_rows('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # And she can fix it once more by entering text into the input box.
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea\n')
        self.check_for_text_in_list_of_table_rows('1: Buy milk')
        self.check_for_text_in_list_of_table_rows('2: Make tea')
