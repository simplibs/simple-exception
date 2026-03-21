from .bool_or_exception import bool_or_exception


_DESIGN_NOTES = """
# utils/exception_helper

## Contents
A helper function for conditional exception raising.

| Name                | Description                                                     |
|---------------------|-----------------------------------------------------------------|
| `bool_or_exception` | Returns False or raises SimpleException based on return_bool    |

## Usage
    from .exception_helper import bool_or_exception

## Notes
This package is intentionally separated from the other utilities — it is
supplementary functionality that depends on `SimpleException`. The lazy
import inside `bool_or_exception` prevents a circular dependency.
"""