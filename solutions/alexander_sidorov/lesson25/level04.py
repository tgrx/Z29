from project.consts import SEP


class Path:
    def __init__(self, path: str):
        self.__parts = tuple(filter(bool, path.split(r"\/")))

    def __str__(self):
        return SEP.join(self.__parts)

    def __truediv__(self, other):
        if not isinstance(other, (str, Path)):
            raise ValueError("cannot build path from values other than str or Path")

        path = str(other)
        new_parts = filter(bool, (str(self), path))
        new_path = SEP.join(new_parts)

        return Path(new_path)
