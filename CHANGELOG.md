# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog,
and this project adheres to Semantic Versioning.

## [0.1.2] - 2026-04-13

### Deprecated
- **This package is now deprecated.** Please migrate to [`simplibs-exception`](https://pypi.org/project/simplibs-exception/)
- `simple-exception` will remain available for backward compatibility, but new projects should use the `simplibs` ecosystem instead
- The simplibs ecosystem provides better organization, improved API design, and continued maintenance
- All functionality from `simple-exception` is available in `simplibs-exception` with enhanced features

### Migration Guide
If you're using `simple-exception`, update your imports:

```python
# Old (deprecated)
from simplibs.exception import SimpleException

# New (recommended)
from simplibs.exception import SimpleException
```

The API remains compatible — no code changes needed, just update the package dependency.

---

## [0.1.1] - 2026-03-23

### Fixed
- Type hint for `exception` parameter now accepts both Exception classes and instances
- Improved typing consistency in `ProcessExceptionParamMixin`

## [0.1.0] - 2026-03-21

### Added
- `SimpleException` — structured exception with diagnostic output
- Support for `message`, `value`, `value_label`, `expected`, `problem`,
  `context`, `how_to_fix`, `error_name`, `exception`, `get_location`,
  `skip_locations`, and `oneline` parameters
- Four output modes: `PRETTY`, `SIMPLE`, `ONELINE`, `LOG`
- `SimpleExceptionSettings` — global configuration for the entire ecosystem
- Custom mode support via `ModeBase`
- Serialisation via `to_dict()`, `to_json()`, `to_debug_dict()`
- Utility tools: `UNSET`/`UnsetType`, `bool_or_exception`, `extract_caller_info`
- Full test coverage (~288 tests)