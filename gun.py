from BaseWeapon import BaseWeapon

class gun(BaseWeapon):
    def __init__(self):
        super().__init__()
        self.damage = 15
        self.max_clip = 20
        self.current_clip = 10

    def shoot(self):
        if self.clip_check():
            self.current_clip = self.current_clip - 1
            print(f'"Bow!" from gun, damage: -{self.damage}%, в обойме осталось: {self.current_clip}')
        else:
            print('Need reload')
            return


