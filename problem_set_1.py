import re
import unittest


class BasicMatching(unittest.TestCase):
    """Fill in a regular expression that will match the
    target strings, without matching the other strings.
    """

    def test_pets(self):
        pets = [
            "cat",
            "dog",
            "pig",
            "pup",
            "bat",
            ]
        not_pets = [
            "hat",
            "car",
            "bar",
            "can",
            "van",
            ]
        pattern = r""  # TODO
        regex = re.compile(pattern)

        for pet in pets:
            b = bool(regex.fullmatch(pet))
            self.assertTrue(b, f"Failed to match: {pet}")

        for other in not_pets:
            b = bool(regex.fullmatch(other))
            self.assertFalse(b, f"False match: {other}")


if __name__ == '__main__':
    unittest.main(verbosity=2)  # Use 1 for more compact output.
