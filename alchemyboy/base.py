"""Base model factory."""

from factory import SubFactory
from factory.alchemy import SQLAlchemyModelFactory
from factory.base import FactoryMetaClass

from sqlalchemy.inspection import inspect
from sqlalchemy.orm.properties import RelationshipProperty, ColumnProperty, CompositeProperty
from sqlalchemy.orm.base import MANYTOONE


class ModelFactoryMetaClass(FactoryMetaClass):

    """Model factory metaclass."""

    types = {}
    """Attribute types and factories map."""

    def __new__(mcs, class_name, bases, attrs):
        """Create new factory type."""
        meta = attrs.get("Meta")
        if getattr(meta, "abstract", None) is True or meta.model is None:
            return super(ModelFactoryMetaClass, mcs).__new__(mcs, class_name, bases, attrs)

        # Process relationships and composites
        composite_columns = set()
        for prop in inspect(meta.model).iterate_properties:
            if prop.key in attrs:
                continue
            elif isinstance(prop, RelationshipProperty):
                if prop.direction == MANYTOONE:
                    attrs[prop.key] = ModelSubFactory(prop.mapper.class_)
            elif isinstance(prop, CompositeProperty):
                composite_columns.update(prop.columns)
                attrs[prop.key] = mcs.types.get[prop.composite_class]

        # Process columns
        for prop in inspect(meta.model).iterate_properties:
            if prop.key in attrs:
                continue
            elif isinstance(prop, ColumnProperty):
                for col in prop.columns:
                    if col not in composite_columns:
                        attrs[prop.key] = mcs.types[col.type.__class__](col.type)

        factory_class = super(ModelFactoryMetaClass, mcs).__new__(mcs, class_name, bases, attrs)
        mcs.factories[factory_class._meta.model] = factory_class
        return factory_class


class ModelSubFactory(SubFactory):

    """Model sub-factory."""

    def __init__(self, model, **kwargs):
        super(SubFactory, self).__init__(**kwargs)
        self.model = model
        self.factory = None

    def get_factory(self):
        return ModelFactoryMetaClass.factories[self.model]


class BaseModelFactory(SQLAlchemyModelFactory):

    """Base model factory."""

    __metaclass__ = ModelFactoryMetaClass

    class Meta:
        abstract = True
