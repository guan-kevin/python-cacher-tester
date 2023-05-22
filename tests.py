import unittest
from artifacts.basic import get_artifact_language, get_artifact_status

class Test(unittest.TestCase):
    def test_language(self):
        result = get_artifact_language('ProgVal-Limnoria-149133609')
        self.assertEqual(result, 'Python')

    def test_status(self):
        result = get_artifact_status('gwtbootstrap3-gwtbootstrap3-92837490')
        self.assertEqual(result, 'active')


if __name__ == '__main__':
    unittest.main()
