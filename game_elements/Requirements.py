from .Field import Field
from .NoneBlock import NoneBlock


class Requirements(Field):
    def __init__(self, path_to_background, requirements, x=0, y=0):
        super().__init__(path_to_background, len(requirements), 1, x, y)
        for i in range(len(requirements)):
            if requirements[i] is not None:
                self.map[0][i] = NoneBlock(i * self.block_rect.width + 5 * (i + 1), 5, str(requirements[i]))
