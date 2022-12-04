from BaseWeapon import BaseWeapon
from gun import gun
from rifle import rifle


class hero:
    current_weapon: BaseWeapon
    weapons_arsenal = []

    num_current_weapon = 0

    def __init__(self):
        self.weapons_arsenal = [
            gun(), rifle()
        ]
        self.current_weapon = self.weapons_arsenal[self.num_current_weapon]

    def shoot(self):
        self.current_weapon.shoot()

    def change_weapon(self):
        self.num_current_weapon += 1
        if self.num_current_weapon == len(self.weapons_arsenal):
            self.num_current_weapon = 0
        self.current_weapon = self.weapons_arsenal[self.num_current_weapon]

    def reload_current_weapon(self, bullet_count):
        self.current_weapon.reload(bullet_count)