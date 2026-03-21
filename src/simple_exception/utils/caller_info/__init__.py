from .extract_caller_info import extract_caller_info


_DESIGN_NOTES = """
# utils/caller_info

## Contents
A diagnostic utility for determining the call site of an exception
in the call stack.

| Name                  | Description                                                    |
|-----------------------|----------------------------------------------------------------|
| `extract_caller_info` | Walks the stack and returns info about the first relevant frame |

## Usage
    from .caller_info import extract_caller_info

## Notes
This package is intentionally separated from the other utilities — it is
a self-contained diagnostic responsibility that is unrelated to the sentinel
or the exception helper functions.
"""