from unittest import TestCase, main
from calculator_main import do_calculations


class CalculatorMainTest(TestCase):
    def test_do_calculations(self):
        self.assertEqual(do_calculations('2+2'), 4)
        self.assertEqual(do_calculations('3-1'), 2)
        self.assertEqual(do_calculations('4*2'), 8)
        self.assertEqual(do_calculations('10/2'), 5)


if __name__ == '__main__':
    main()
