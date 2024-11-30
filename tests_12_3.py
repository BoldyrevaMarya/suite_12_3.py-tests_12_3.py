import runner
import runner_and_tournament
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test_runner = runner.Runner('Nina')
        for _ in range(10):
            test_runner.walk()
        self.assertEqual(test_runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test_runner = runner.Runner('Milka')
        for _ in range(10):
            test_runner.run()
        self.assertEqual(test_runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_runner1 = runner.Runner('Nina')
        test_runner2 = runner.Runner('Milka')
        for _ in range(10):
            test_runner1.run()
            test_runner2.walk()
        self.assertNotEqual(test_runner1.distance, test_runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for value in cls.all_results.values():
            print(value)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour1(self):
        tour = runner_and_tournament.Tournament(9, self.runner1, self.runner3)
        self.all_results['test1'] = tour.start()
        temp = list(self.all_results.values())
        self.assertTrue(temp[-1], 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour2(self):
        tour = runner_and_tournament.Tournament(9, self.runner2, self.runner3)
        self.all_results['test2'] = tour.start()
        temp = list(self.all_results.values())
        self.assertTrue(temp[-1], 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour3(self):
        tour = runner_and_tournament.Tournament(9, self.runner1, self.runner2, self.runner3)
        self.all_results['test3'] = tour.start()
        temp = list(self.all_results.values())
        self.assertTrue(temp[-1], 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour4(self):
        tour = runner_and_tournament.Tournament(9, self.runner1, self.runner2, self.runner3)
        self.all_results['test4'] = tour.start()
        temp = list(self.all_results.values())
        self.assertTrue(temp[0], 'Сергей')
