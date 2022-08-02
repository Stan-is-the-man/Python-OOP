from project.hero import Hero
from unittest import TestCase, main


class TestHero(TestCase):
    def test_constructor(self):
        hero = Hero("username", 10, 50.0, 20.0)
        self.assertEqual('username', hero.username)
        self.assertEqual(10, hero.level)
        self.assertEqual(50.0, hero.health)
        self.assertEqual(20.0, hero.damage)

    def test_battle_enemy_has_the_same_name_raise_error(self):
        hero = Hero("username", 10, 50.0, 20.0)
        enemy_hero = Hero("username", 14, 50.4, 20.3)
        with self.assertRaises(Exception) as ex:
            hero.battle(enemy_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_hero_health_less_or_equal_zero_raise_error(self):
        # negative health
        hero = Hero("username", 10, -1, 20.0)
        enemy_hero = Hero("enemy_user_name", 14, 50.4, 20.3)
        with self.assertRaises(Exception) as ex:
            hero.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

        # 0 health
        hero = Hero("username", 10, 0, 20.0)
        enemy_hero = Hero("enemy_user_name", 14, 50.4, 20.3)
        with self.assertRaises(Exception) as ex:
            hero.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_health_less_or_equal_zero_raise_error(self):
        # negative health
        hero = Hero("username", 10, 50, 20.0)
        enemy_hero = Hero("enemy_user_name", 14, -7, 20.3)
        with self.assertRaises(Exception) as ex:
            hero.battle(enemy_hero)
        self.assertEqual("You cannot fight enemy_user_name. He needs to rest", str(ex.exception))

        # 0 health
        hero = Hero("username", 10, 50, 20.0)
        enemy_hero = Hero("enemy_user_name", 14, 0, 20.3)
        with self.assertRaises(Exception) as ex:
            hero.battle(enemy_hero)
        self.assertEqual("You cannot fight enemy_user_name. He needs to rest", str(ex.exception))

    def test_battle_0_or_negative_health(self):
        # only 0
        hero = Hero("username", 10, 300, 20.0)
        enemy_hero = Hero("enemy_user_name", 10, 200, 30.0)
        self.assertEqual("Draw", hero.battle(enemy_hero))

        # negative health
        hero = Hero("username", 10, 299, 20.0)
        enemy_hero = Hero("enemy_user_name", 10, 199, 30.0)
        self.assertEqual("Draw", hero.battle(enemy_hero))

    def test_battle_enemy_0_or_negative_health(self):
        # 0 health
        hero = Hero("username", 10, 500, 20.0)
        enemy_hero = Hero("enemy_user_name", 10, 200, 30.0)
        self.assertEqual("You win", hero.battle(enemy_hero))


        # negative health
        hero = Hero("username", 10, 500, 20.0)
        enemy_hero = Hero("enemy_user_name", 10, 199, 30.0)
        self.assertEqual("You win", hero.battle(enemy_hero))
        self.assertEqual(11, hero.level)
        self.assertEqual(205.0, hero.health)
        self.assertEqual(25, hero.damage)

    def test_battle_hero_0_or_less_health(self):
        # 0 health
        hero = Hero("username", 10, 300, 20.0)
        enemy_hero = Hero("enemy_user_name", 10, 700, 30.0)

        # negative health
        hero = Hero("username", 10, 100, 20.0)
        enemy_hero = Hero("enemy_user_name", 10, 700, 30.0)

        self.assertEqual("You lose", hero.battle(enemy_hero))
        self.assertEqual(11, enemy_hero.level)
        self.assertEqual(505.0, enemy_hero.health)
        self.assertEqual(35, enemy_hero.damage)

if __name__ == "__main__":
    main()
