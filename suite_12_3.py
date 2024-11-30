import unittest


def skip_if_frozen(test_func):
    def wrapper(self):
        if getattr(self, 'is_frozen', False):
            raise unittest.SkipTest('Тесты в этом кейсе заморожены')
        return test_func(self)

    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_challenge(self):
        self.assertEqual(1 + 1, 2)

    @skip_if_frozen
    def test_run(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_walk(self):
        self.assertIn(2, [1, 2, 3])


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_first_tournament(self):
        self.assertEqual(2 * 2, 4)

    @skip_if_frozen
    def test_second_tournament(self):
        self.assertFalse(False)

    @skip_if_frozen
    def test_third_tournament(self):
        self.assertIsNone(None)


suite = unittest.TestSuite()
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
