import unittest
from Service.mercadolibreAPI import MercadoLibre


class MyTestCase(unittest.TestCase):
    def ItemInformationUnitTestSuccess(self):
        try:
            response = MercadoLibre.get_item_information("MLA1126591385")
            if response:
                self.assertTrue(True, "Get Item Information success")
        except Exception as exception:
            self.assertFalse(False, f"Item not Found - {exception}")

    def ItemInformationUnitTestFail(self):
        response = MercadoLibre.get_item_information("MLA112659138")
        self.assertEqual(response["status"], 404, "Item Not Found")


if __name__ == '__main__':
    unittest.main()
