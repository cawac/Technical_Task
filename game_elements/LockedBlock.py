from .Block import Block


class LockedBlock(Block):
    def __init__(self, x, y, path_to_image="images/0.png"):
        super().__init__(x, y, path_to_image)
        self.name = 0

    def is_movable(self):
        return False


