"""
Tests for UNSET and UnsetType — singleton behaviour, repr, bool, and type checking.
"""
import pytest
from simple_exception.utils import UNSET, UnsetType


# -----------------------------------------------------------------------------
# Singleton
# -----------------------------------------------------------------------------

def test_singleton_repeated_calls_return_same_instance():
    """UnsetType() must always return the same instance."""
    assert UnsetType() is UnsetType()


def test_singleton_unset_is_instance_of_unset_type():
    """The global UNSET must be an instance of UnsetType."""
    assert isinstance(UNSET, UnsetType)


def test_singleton_multiple_instances_share_identity():
    """Multiple variables must all point to the same singleton object."""
    a = UnsetType()
    b = UnsetType()
    assert a is b is UNSET


# -----------------------------------------------------------------------------
# __repr__
# -----------------------------------------------------------------------------

def test_repr_returns_unset_string():
    """repr(UNSET) must return the exact string 'UNSET'."""
    assert repr(UNSET) == "UNSET"


# -----------------------------------------------------------------------------
# __bool__
# -----------------------------------------------------------------------------

def test_bool_unset_is_falsy():
    """UNSET must be falsy — bool(UNSET) == False."""
    assert not UNSET


def test_bool_returns_exactly_false():
    """bool(UNSET) must return exactly False, not just a falsy value."""
    assert bool(UNSET) is False


# -----------------------------------------------------------------------------
# Type checking
# -----------------------------------------------------------------------------

def test_not_instance_of_other_types():
    """UNSET must not be an instance of common types such as str, int, or None."""
    assert not isinstance(UNSET, str)
    assert not isinstance(UNSET, int)
    assert UNSET is not None