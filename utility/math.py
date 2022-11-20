class Infix:
    """Base class for infix creation."""
    def __init__(self, function):
        self.function = function
    def __ror__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))
    def __or__(self, other):
        return self.function(other)
    def __rlshift__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))
    def __rshift__(self, other):
        return self.function(other)
    def __call__(self, value1, value2):
        return self.function(value1, value2)

def sum_tuples(a,b):
    result = []
    for i in range(0, len(a)):
        result.append(a[i] + b[i])
    return tuple(result)


infix_sum_tuple=Infix(sum_tuples)
"""Returns a new Tuple with the sum of left and right Tuple values."""

infix_clamp = Infix(lambda value, range: max(range[0], min(value, range[1])))
"""Clamps left value at the range (min, max) of right value."""


def space_to_center(obj: tuple[int, int], container: tuple[int,int]):
    """Gets the required offset to center a point in a container.

        Args:
            obj (tuple[int,int]): The position of the object to be centered.
            container (tuple[int,int]): The size of the container to center the object in.
            
        Returns:
        tuple[int,int]: The x and y required offset.
    """
    return ((container[0] - obj[0]) // 2, (container[1] - obj[1]) // 2)

def between(value, min, max, inclusive = True):
    """Returns a value inside the bounds of min and max.

    Args:
        value (int | float): The value to clamp.
        min (int | float): The min value.
        max (int | float): The max value.
        inclusive (bool, optional): Whether the min and max should be inclusive or not. Defaults to True.

    Returns:
        (int | float): The clamped value, between min and max range.
    """
    if inclusive:
        return value >= min and value <= max
    return value > min and value < max