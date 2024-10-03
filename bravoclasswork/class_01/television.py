
class Television:

    def __init__(self):
        self.is_on:bool = False
        self.channel: int = 1
        self.volume_level = 2

    def _turn_on(self):
        self.is_on = True

    def _turn_off(self) :
        self.is_on = False

    def get_is_on(self) :
        return self.is_on

    def get_volume(self) -> int:
        return self.volume_level

    def set_volume(self, volume_level):
            if not self.is_on:
                print("TV is off. Please turn it on before setting a volume level.")
                return
            if 1 <= volume_level <= 10:
                self.volume_level = volume_level
            else:
                raise ValueError("Volume level should be between 1 and 10.")

    def increase_volume(self ) -> None:
                self.volume_level += 1
