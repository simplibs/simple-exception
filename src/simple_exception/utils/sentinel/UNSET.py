from typing import Final


class UnsetType:
    """Singleton sentinel type representing an unset value."""

    # Attribute for the singleton instance
    _instance = None

    # Create the singleton instance
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __repr__(self):
        return "UNSET"

    def __bool__(self):
        return False


# Sentinel
UNSET: Final = UnsetType()


_DESIGN_NOTES = """
# UnsetType and UNSET

## Purpose
A sentinel for distinguishing an unset value from an intentionally passed `None` —
because `None` is a valid value in this library with its own meaning.

## Why not None?
```python
def func(value = None):
    if value is None:
        # ambiguous — was None passed intentionally, or was nothing passed at all?
```
```python
def func(value: UnsetType = UNSET):
    if value is UNSET:
        # parameter was not provided → apply default behaviour
    elif value is None:
        # None was passed intentionally → specific logic applies
```

## Singleton
`UnsetType` is implemented as a singleton — all instances are identical.
Comparisons must therefore always use `is`, never `==`:
```python
value is UNSET      # ✓ correct
value == UNSET      # ✗ never do this
```

## __bool__
`UnsetType.__bool__` returns `False` — `UNSET` therefore behaves as a falsy value:
```python
if not value:
    # true for UNSET, None, False, "", and 0
```
For an explicit check, always use `is UNSET`.

## UNSET
A pre-created singleton instance of `UnsetType` — used throughout the library
as the default value for parameters that do not need to be provided.

## Notes
- The `Final` annotation ensures that `UNSET` cannot be reassigned.
- Both objects (`UnsetType` and `UNSET`) are exported from the library —
  users may use them in their own type annotations and checks.
"""