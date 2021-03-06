from django.db.backends.oracle.base import (
    DatabaseWrapper as OracleDatabaseWrapper,
    DatabaseFeatures as OracleDatabaseFeatures,
)
from django.contrib.gis.db.backends.base import BaseSpatialFeatures
from django.contrib.gis.db.backends.oracle.creation import OracleCreation
from django.contrib.gis.db.backends.oracle.introspection import OracleIntrospection
from django.contrib.gis.db.backends.oracle.operations import OracleOperations


class DatabaseFeatures(BaseSpatialFeatures, OracleDatabaseFeatures):
    pass


class DatabaseWrapper(OracleDatabaseWrapper):
    def __init__(self, *args, **kwargs):
        super(DatabaseWrapper, self).__init__(*args, **kwargs)
        self.features = DatabaseFeatures(self)
        self.ops = OracleOperations(self)
        self.creation = OracleCreation(self)
        self.introspection = OracleIntrospection(self)
