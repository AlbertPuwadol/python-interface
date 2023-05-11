import abc

class Double(metaclass=abc.ABCMeta):
    """Double precision floating point number."""
    pass

Double.register(float)

print(issubclass(float, Double))
print(isinstance(1.2345, Double))

@Double.register
class Double64:
    """A 64-bit double-precision floating-point number."""
    pass

print(issubclass(Double64, Double))