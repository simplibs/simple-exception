# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-03-21

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