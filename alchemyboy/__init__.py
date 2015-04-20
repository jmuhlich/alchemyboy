"""alchemyboy public API."""

__version__ = '1.0.0'

try:
    from .base import BaseModelFactory
    from .types import register

    __all__ = [
        BaseModelFactory.__name__,
        register.__name__,
    ]
except ImportError:  # pragma: no cover
    # avoid import errors when only __version__ is needed (for setup.py)
    pass
