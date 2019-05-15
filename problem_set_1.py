import re
import unittest


class BasicMatching(unittest.TestCase):
    """Fill in a regular expression that will match the
    target strings, without matching the other strings.
    """

    def test_mentions_pet(self):
        with_pet = [
            "I like my cat.",
            "A cat is a person's best friend.",
            "Look at that cat sleeping in the window.",
            "A cheetah is faster than any dog.",
            "But I love my dogs too.",
            ]
        without_pet = [
            "I instead like my Ferrari.",
            "My brother likes many sports.",
            "The top speed of an F1 car is faster than a cheetah.",
            ]

        pattern = r""  # TODO

        regex = re.compile(pattern)

        for text in with_pet:
            b = bool(regex.search(text))
            self.assertTrue(b, f"Failed to match: {text}")

        for text in without_pet:
            b = bool(regex.search(text))
            self.assertFalse(b, f"False match: {text}")

    def test_mentions_price(self):
        has_price = [
            "Robot kit: $199.99",
            "Jetpack: $7.89",
            "Boombox: $11",
            "CD with Never Gonna Give You Up: $0.50",
            ]
        no_price = [
            "Pranking the meeting on the 11th floor: priceless",
            "For everything else that costs $$$, there's bitcoins.",
            "The current temperature is 72.9 degrees centigrade.",
            "This 98 degrees CD is expen$ive!"
            ]

        pattern = r"(\$[0-9]{1,3}\.?[0-9]{0,2})"  # TODOne

        regex = re.compile(pattern)

        for text in has_price:
            b = bool(regex.search(text))
            self.assertTrue(b, f"Failed to match: {text}")

        for text in no_price:
            b = bool(regex.search(text))
            self.assertFalse(b, f"False match: {text}")

    def test_zipcode_detector(self):
        has_zip = [
            "20252 is the personal zip for Smokey the Bear",
            "Hey Google, what's the weather in 99501.",
            "General Electric's Schenectady office claims the entire 12345 zip.",
            "The lowest zip code, 00501, is in Holtsville, NY.",
            "The exact zip for the Empire State Building is: 10118-0114.",
            ]
        no_zip = [
            "T-minus 6 5 4 3 2 1...",
            "You can reach me at (555) 555-5555 later today.",
            "Pi is approximately 3.14159265.",
            ]

        for text in has_zip:
            b = has_zipcode(text)
            self.assertTrue(b, f"Failed to match: {text}")

        for text in no_zip:
            b = has_zipcode(text)
            self.assertFalse(b, f"False match: {text}")


def has_zipcode(text):
    """Uses a RegEx to detect if the input mentions a zipcode.

    Expects a string. Returns a boolean."""
    return None  # TODO


if __name__ == '__main__':
    unittest.main(verbosity=2)  # Use 1 for more compact output.
