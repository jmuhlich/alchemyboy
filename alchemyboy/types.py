"""Basic SQLAlchemy types."""

import datetime as datetime_
from sqlalchemy.sql import sqltypes
from factory import fuzzy

from .base import ModelFactoryMetaClass


def register(typ):
    """SQLAlchemy attribute type registration shortcut.

    :param typ: SQLAlchemy type, type decorator, related model class, etc.
    """
    def wrapper(func):
        """Function that accepts the attribute type and returns a factoryboy attribute."""
        ModelFactoryMetaClass.types[typ] = func
        return func
    return wrapper


@register(sqltypes.Numeric)
def numeric(typ):
    """Fuzzy numeric type."""
    precision = typ.precision
    if precision is None:
        precision = 5
    return fuzzy.FuzzyDecimal(low=0.0, high=999.99, precision=precision)


@register(sqltypes.Float)
def float(typ):
    """Fuzzy float type."""
    low = 0.0
    high = 999.0
    precision = typ.precision
    if precision is None:
        precision = 5
    if typ.asdecimal:
        return fuzzy.FuzzyDecimal(low=low, high=high, precision=precision)
    else:
        return fuzzy.FuzzyFloat(low=low, high=high)


@register(sqltypes.DateTime)
def datetime(typ):
    """Fuzzy datetime."""
    return fuzzy.FuzzyNaiveDateTime(start_dt=datetime_.datetime(1900, 1, 1))


@register(sqltypes.Date)
def date(typ):
    """Fuzzy date."""
    return fuzzy.FuzzyDate(start_date=datetime_.date(1900, 1, 1))


@register(sqltypes.Boolean)
def boolean(typ):
    """Fuzzy boolean."""
    return fuzzy.FuzzyChoice(choices=[True, False])


@register(sqltypes.Integer)
def integer(typ):
    """Fuzzy integer."""
    return fuzzy.FuzzyInteger(low=0, high=65535)


@register(sqltypes.Text)
def text(typ):
    """Fuzzy text."""
    length = typ.length
    if length is None:
        length = 500
    return fuzzy.FuzzyText(length=length)


@register(sqltypes.String)
def string(typ):
    """Fuzzy string."""
    return fuzzy.FuzzyText(length=typ.length)


@register(sqltypes.Unicode)
def unicode(typ):
    """Fuzzy unicode."""
    return fuzzy.FuzzyText(length=typ.length)
