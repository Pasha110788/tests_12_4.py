import logging
import unittest

from rt_with_exceptions import Runner

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding='utf-8',
                    format="%(asctime)s / %(levelname)s / %(message)s")


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            runner = Runner("TesterWalk", -2)
            for i in range(10):
                runner.walk()
            logging.info('"test_walk" выполнен успешно')
            self.assertEqual(runner.distance, 50)
        except ValueError:
            logging.warning("Неверная скорость для Runner")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            runner = Runner(123)
            for i in range(10):
                runner.run()
            logging.info('"test_run" выполнен успешно')
            self.assertEqual(runner.distance, 100)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challehge(self):
        runner1 = Runner("TesterChall1")
        runner2 = Runner("TesterChall2")
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()
