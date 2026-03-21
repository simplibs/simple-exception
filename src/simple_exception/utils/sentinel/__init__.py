from .UNSET import UnsetType, UNSET


_DESIGN_NOTES = """
# utils/sentinel

## Contents
The library's sentinel values — exported from the library and available to users.

| Name        | Description                                                  |
|-------------|--------------------------------------------------------------|
| `UnsetType` | Singleton type representing an unset value                   |
| `UNSET`     | A pre-created instance of `UnsetType` — used throughout      |
"""