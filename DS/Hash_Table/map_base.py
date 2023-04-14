from collections.abc import MutableMapping

class MapBase(MutableMapping):
    """Our own abstract base class that includes a nonpublic Item class."""

    # Nested Item class
    class Item:
        """Lightweight composite to store key-value pairs as map items."""
        __slots__ = ('_key', '_value')  # Use parentheses to specify multiple slots

        def __init__(self, k, v):
            self._key = k  # Use private attributes to store key and value
            self._value = v

        def __eq__(self, other):
            # Compare items based on their keys
            return self._key == other._key

        def __ne__(self, other):
            # Opposite of __eq__
            return not (self == other)

        def __lt__(self, other):
            # Compare items based on their keys
            return self._key < other._key
