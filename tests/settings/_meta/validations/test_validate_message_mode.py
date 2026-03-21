"""
Tests for validate_message_mode — built-in modes, custom modes, invalid values, and exception fields.
"""
import pytest
from simple_exception.settings._meta.validations.SimpleExceptionSettingsError import SimpleExceptionSettingsError
from simple_exception.settings._meta.validations.validate_message_mode import validate_message_mode
from simple_exception.modes.PRETTY import PRETTY
from simple_exception.modes.SIMPLE import SIMPLE
from simple_exception.modes.ONELINE import ONELINE
from simple_exception.modes.LOG import LOG


# -----------------------------------------------------------------------------
# validate_message_mode
# -----------------------------------------------------------------------------

@pytest.mark.parametrize("value", [PRETTY, SIMPLE, ONELINE, LOG])
def test_all_builtin_modes_pass(value):
    """All built-in modes must pass validation."""
    validate_message_mode(value)


def test_custom_mode_instance_passes():
    """A custom ModeBase instance must pass validation."""
    from simple_exception.modes.base_class import ModeBase

    class CustomMode(ModeBase):
        def _full_outcome(self, data, caller_info):
            return "custom"

    validate_message_mode(CustomMode())


@pytest.mark.parametrize("value", [
    "PRETTY",
    None,
    42,
    type("FakeMode", (), {})(),
])
def test_invalid_values_raise(value):
    """Anything other than a ModeBase instance must raise SimpleExceptionSettingsError."""
    with pytest.raises(SimpleExceptionSettingsError):
        validate_message_mode(value)


def test_exception_contains_correct_fields():
    """The raised exception must have correctly populated fields."""
    invalid = "PRETTY"
    with pytest.raises(SimpleExceptionSettingsError) as exc_info:
        validate_message_mode(invalid)
    assert exc_info.value.value == invalid
    assert exc_info.value.value_label == "DEFAULT_MESSAGE_MODE"
    assert "value is not a valid output mode" in exc_info.value.problem
    assert exc_info.value.error_name == "SETTINGS ERROR"