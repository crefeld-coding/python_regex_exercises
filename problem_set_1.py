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


if __name__ == '__main__':
    unittest.main(verbosity=2)  # Use 1 for more compact output.
