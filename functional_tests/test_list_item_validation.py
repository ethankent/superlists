from unittest import skip

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidently tries to submit an empty list item.
        # She hits ENTER on the empty input box.

        # The home page refreshes and displays an error message: "List items cannot be blank."

        # Edith tries again with some text for the item. This time it works.

        # Curious to see what will happen if she does it again, she decides to submit a second blank item.

        # She recieves a similar warning on the list view page.

        # And she can fix it once more by entering text into the input box.
        self.fail('Write me.')
