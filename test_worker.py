class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTests(TestCase):
    def test_if_worker_is_initialized_with_correctly(self):
        worker = Worker("Bai Hui", 5000, 10)
        self.assertEqual("Bai Hui", worker.name)
        self.assertEqual(5000, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money)

    def test_energy_is_incremented_after_rest(self):
        worker = Worker("Bai Hui", 5000, 10)
        self.assertEqual(10, worker.energy)
        worker.rest()
        self.assertEqual(11, worker.energy)

    def test_worker_tries_to_work_with_negative_energy(self):
        worker = Worker("Bai Hui", 5000, -5)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_worker_tries_to_work_with_0_energy(self):
        worker = Worker("Bai Hui", 5000, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_money_is_increased_when_work(self):
        worker = Worker("Bai Hui", 5000, 5)
        self.assertEqual(0, worker.money)
        worker.work()
        self.assertEqual(5000, worker.money)

        # extra work for testing the money(+=)
        worker.work()
        self.assertEqual(10000, worker.money)

    def test_energy_is_decreased_when_work(self):
        worker = Worker("Bai Hui", 5000, 5)
        self.assertEqual(5, worker.energy)
        worker.work()
        self.assertEqual(4, worker.energy)

    def test_get_info(self):
        worker = Worker("Bai Hui", 5000, 5)
        result = worker.get_info()
        expected = f'Bai Hui has saved 0 money.'
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
