
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
        if self.is_on and 1 <= self.volume_level <= 10:
            return self.volume_level
        else:
            return False

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

    def decrease_volume(self):
        self.volume_level -= 1

    def get_channel(self):
        if self.is_on and 1 <= self.channel <= 100:
            return self.channel
        else:
            return False

    def set_channel(self, channel):
        if not self.is_on:
            print("TV is off. Please turn it on before setting a channel.")
            return
        if 1 <= channel <= 100:
            self.channel = channel
        else:
            raise ValueError("Channel should be between 1 and 100.")

    def channel_up(self):
        self.channel += 1

    def channel_down(self):
        self.channel -= 1




