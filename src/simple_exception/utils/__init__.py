from .sentinel import UnsetType, UNSET
from .caller_info import extract_caller_info
from .exception_helper import bool_or_exception


_DESIGN_NOTES = """
# utils

## Contents
The library's shared utilities, split into three self-contained packages
by responsibility. `UnsetType` and `UNSET` are exported from the library
for use in user code.

| Package            | Name                  | Description                                         |
|--------------------|-----------------------|-----------------------------------------------------|
| `sentinel`         | `UnsetType`           | Singleton type representing an unset value          |
|                    | `UNSET`               | A pre-created instance of `UnsetType`               |
| `caller_info`      | `extract_caller_info` | Diagnostic function for determining the call site   |
| `exception_helper` | `bool_or_exception`   | Shortcut for conditional exception raising          |

## Why three packages
Each package has a different responsibility and a different character:
- `sentinel` — a data pattern, independent of everything else in the library
- `caller_info` — a diagnostic utility, independent of the library
- `exception_helper` — supplementary functionality that depends on `SimpleException`;
  the lazy import inside the function prevents a circular dependency
"""