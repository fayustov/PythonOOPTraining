from BaseWeapon import BaseWeapon

class rifle(BaseWeapon):
    def __init__(self):
        super().__init__()
        self.damage = 10 # урон
        self.max_clip = 50 # максимальная вместительность обоймы
        self.current_clip = 5 # кол-во патронов в обойме

    COUNT_SHOOT = 3

    def shoot(self):
        if self.clip_check() == False:
            print('Need reload')
            return
        if self.current_clip >= self.COUNT_SHOOT:
            self.current_clip = self.current_clip - self.COUNT_SHOOT
            shoot_text = self.COUNT_SHOOT * ' "Bow!"'
            shoot_text = shoot_text[1:]
            print(f'{shoot_text} from rifle, damage: -{self.damage * self.COUNT_SHOOT}%, в обойме осталось: {self.current_clip}')
        else:
            shoot_text = self.current_clip * ' "Bow!"'
            shoot_text = shoot_text[1:]
            number_of_shoots = self.current_clip
            self.current_clip = 0
            print(f'{shoot_text} from rifle, damage: -{self.damage * number_of_shoots}%, в обойме осталось: {self.current_clip}')
