from abc import ABC, abstractmethod

class BaseWeapon(ABC):
    damage: int
    current_clip: int
    max_clip: int
    def __init__(self):
        super().__init__()

    @abstractmethod
    def shoot(self):
        pass

    def reload(self, bullet_count):
        self.current_clip = self.current_clip + bullet_count
        if self.current_clip > self.max_clip:
            remains = self.current_clip - self.max_clip
            self.current_clip = self.max_clip
            return remains
        return 0

    def clip_check(self):
        return self.current_clip > 0