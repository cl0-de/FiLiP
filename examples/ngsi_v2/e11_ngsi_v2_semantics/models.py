"""
Autogenerated Models for the vocabulary described by the ontologies:
	http://www.semanticweb.org/building (building circuits)
"""

from enum import Enum
from typing import Dict, Union, List
from filip.semantics.semantics_models import\
	SemanticClass,\
	SemanticIndividual,\
	RelationField,\
	DataField,\
	SemanticDeviceClass,\
	DeviceAttributeField,\
	CommandField
from filip.semantics.semantics_manager import\
	SemanticsManager,\
	InstanceRegistry


semantic_manager: SemanticsManager = SemanticsManager(
	instance_registry=InstanceRegistry(),
)

# ---------CLASSES--------- #


class Thing(SemanticClass):
	"""
	Predefined root_class

	Source(s): 
		None (Predefined)
	"""

	def __new__(cls, *args, **kwargs):
		kwargs['semantic_manager'] = semantic_manager
		return super().__new__(cls, *args, **kwargs)

	def __init__(self, *args, **kwargs):
		kwargs['semantic_manager'] = semantic_manager
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)


class Room(Thing):
	"""
	Generated SemanticClass without description

	Source(s): 
		http://www.semanticweb.org/building (building circuits)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.goalTemperature._rules = [('exactly|1', [['integer']])]
			self.name._rules = [('exactly|1', [['string']])]
			self.volume._rules = [('some', [['rational']])]

			self.hasOutlet._rules = [('only', [[Outlet]])]
			self.hasSensor._rules = [('only', [[Sensor]])]
			self.hasTenant._rules = [('only', [[Tenant]])]

			self.hasOutlet._instance_identifier = self.get_identifier()
			self.hasSensor._instance_identifier = self.get_identifier()
			self.hasTenant._instance_identifier = self.get_identifier()
			self.goalTemperature._instance_identifier = self.get_identifier()
			self.name._instance_identifier = self.get_identifier()
			self.volume._instance_identifier = self.get_identifier()

	# Data fields

	goalTemperature: DataField = DataField(
		name='goalTemperature',
		rule='exactly 1 integer',
		semantic_manager=semantic_manager)

	name: DataField = DataField(
		name='name',
		rule='exactly 1 string',
		semantic_manager=semantic_manager)

	volume: DataField = DataField(
		name='volume',
		rule='some rational',
		semantic_manager=semantic_manager)

	# Relation fields

	hasOutlet: RelationField = RelationField(
		name='hasOutlet',
		rule='only Outlet',
		inverse_of=['connectedTo'],
		semantic_manager=semantic_manager)

	hasSensor: RelationField = RelationField(
		name='hasSensor',
		rule='only Sensor',
		semantic_manager=semantic_manager)

	hasTenant: RelationField = RelationField(
		name='hasTenant',
		rule='only Tenant',
		semantic_manager=semantic_manager)


class Building(Thing):
	"""
	Generated SemanticClass without description

	Source(s): 
		http://www.semanticweb.org/building (building circuits)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.goalTemperature._rules = [('exactly|1', [['integer']])]
			self.name._rules = [('exactly|1', [['string']])]

			self.hasFloor._rules = [('min|1', [[Floor]])]

			self.hasFloor._instance_identifier = self.get_identifier()
			self.goalTemperature._instance_identifier = self.get_identifier()
			self.name._instance_identifier = self.get_identifier()

	# Data fields

	goalTemperature: DataField = DataField(
		name='goalTemperature',
		rule='exactly 1 integer',
		semantic_manager=semantic_manager)

	name: DataField = DataField(
		name='name',
		rule='exactly 1 string',
		semantic_manager=semantic_manager)

	# Relation fields

	hasFloor: RelationField = RelationField(
		name='hasFloor',
		rule='min 1 Floor',
		semantic_manager=semantic_manager)


class Sensor(SemanticDeviceClass, Thing):
	"""
	Generated SemanticClass without description

	Source(s): 
		http://www.semanticweb.org/building (building circuits)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.measures._rules = [('exactly|1', [['MeasurementType']])]
			self.unit._rules = [('exactly|1', [['Unit']])]

			self.measurement._instance_identifier = self.get_identifier()
			self.measures._instance_identifier = self.get_identifier()
			self.unit._instance_identifier = self.get_identifier()

	# Data fields

	measurement: DeviceAttributeField = DeviceAttributeField(
		name='measurement',
		semantic_manager=semantic_manager)

	measures: DataField = DataField(
		name='measures',
		rule='exactly 1 MeasurementType',
		semantic_manager=semantic_manager)

	unit: DataField = DataField(
		name='unit',
		rule='exactly 1 Unit',
		semantic_manager=semantic_manager)


class Producer(SemanticDeviceClass, Thing):
	"""
	Generated SemanticClass without description

	Source(s): 
		http://www.semanticweb.org/building (building circuits)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.name._rules = [('exactly|1', [['string']])]

			self.controlCommand._instance_identifier = self.get_identifier()
			self.name._instance_identifier = self.get_identifier()
			self.state._instance_identifier = self.get_identifier()

	# Data fields

	controlCommand: CommandField = CommandField(
		name='controlCommand',
		semantic_manager=semantic_manager)

	name: DataField = DataField(
		name='name',
		rule='exactly 1 string',
		semantic_manager=semantic_manager)

	state: DeviceAttributeField = DeviceAttributeField(
		name='state',
		semantic_manager=semantic_manager)


class Outlet(SemanticDeviceClass, Thing):
	"""
	Generated SemanticClass without description

	Source(s): 
		http://www.semanticweb.org/building (building circuits)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:

			self.connectedTo._rules = [('min|1', [[Circuit]]), ('exactly|1', [[Room]])]

			self.connectedTo._instance_identifier = self.get_identifier()
			self.controlCommand._instance_identifier = self.get_identifier()
			self.state._instance_identifier = self.get_identifier()

	# Data fields

	controlCommand: CommandField = CommandField(
		name='controlCommand',
		semantic_manager=semantic_manager)

	state: DeviceAttributeField = DeviceAttributeField(
		name='state',
		semantic_manager=semantic_manager)

	# Relation fields

	connectedTo: RelationField = RelationField(
		name='connectedTo',
		rule='min 1 Circuit, exactly 1 Room',
		inverse_of=['hasOutlet'],
		semantic_manager=semantic_manager)


class Floor(Thing):
	"""
	Generated SemanticClass without description

	Source(s): 
		http://www.semanticweb.org/building (building circuits)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.name._rules = [('exactly|1', [['string']])]

			self.hasRoom._rules = [('only', [[Room]])]

			self.hasRoom._instance_identifier = self.get_identifier()
			self.name._instance_identifier = self.get_identifier()

	# Data fields

	name: DataField = DataField(
		name='name',
		rule='exactly 1 string',
		semantic_manager=semantic_manager)

	# Relation fields

	hasRoom: RelationField = RelationField(
		name='hasRoom',
		rule='only Room',
		semantic_manager=semantic_manager)


class Tenant(Thing):
	"""
	Generated SemanticClass without description

	Source(s): 
		http://www.semanticweb.org/building (building circuits)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.goalTemperature._rules = [('exactly|1', [['integer']])]
			self.name._rules = [('exactly|1', [['string']])]

			self.goalTemperature._instance_identifier = self.get_identifier()
			self.name._instance_identifier = self.get_identifier()

	# Data fields

	goalTemperature: DataField = DataField(
		name='goalTemperature',
		rule='exactly 1 integer',
		semantic_manager=semantic_manager)

	name: DataField = DataField(
		name='name',
		rule='exactly 1 string',
		semantic_manager=semantic_manager)


class Circuit(Thing):
	"""
	Generated SemanticClass without description

	Source(s): 
		http://www.semanticweb.org/building (building circuits)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.name._rules = [('exactly|1', [['string']])]

			self.hasOutlet._rules = [('min|1', [[Outlet]])]
			self.hasProducer._rules = [('min|1', [[Producer]])]

			self.hasOutlet._instance_identifier = self.get_identifier()
			self.hasProducer._instance_identifier = self.get_identifier()
			self.name._instance_identifier = self.get_identifier()

	# Data fields

	name: DataField = DataField(
		name='name',
		rule='exactly 1 string',
		semantic_manager=semantic_manager)

	# Relation fields

	hasOutlet: RelationField = RelationField(
		name='hasOutlet',
		rule='min 1 Outlet',
		inverse_of=['connectedTo'],
		semantic_manager=semantic_manager)

	hasProducer: RelationField = RelationField(
		name='hasProducer',
		rule='min 1 Producer',
		semantic_manager=semantic_manager)


class HeatProducer(Producer):
	"""
	Generated SemanticClass without description

	Source(s): 
		http://www.semanticweb.org/building (building circuits)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.name._rules = [('exactly|1', [['string']])]

			self.controlCommand._instance_identifier = self.get_identifier()
			self.name._instance_identifier = self.get_identifier()
			self.state._instance_identifier = self.get_identifier()

	# Data fields

	controlCommand: CommandField = CommandField(
		name='controlCommand',
		semantic_manager=semantic_manager)

	name: DataField = DataField(
		name='name',
		rule='exactly 1 string',
		semantic_manager=semantic_manager)

	state: DeviceAttributeField = DeviceAttributeField(
		name='state',
		semantic_manager=semantic_manager)


class ColdProducer(Producer):
	"""
	Generated SemanticClass without description

	Source(s): 
		http://www.semanticweb.org/building (building circuits)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.name._rules = [('exactly|1', [['string']])]

			self.controlCommand._instance_identifier = self.get_identifier()
			self.name._instance_identifier = self.get_identifier()
			self.state._instance_identifier = self.get_identifier()

	# Data fields

	controlCommand: CommandField = CommandField(
		name='controlCommand',
		semantic_manager=semantic_manager)

	name: DataField = DataField(
		name='name',
		rule='exactly 1 string',
		semantic_manager=semantic_manager)

	state: DeviceAttributeField = DeviceAttributeField(
		name='state',
		semantic_manager=semantic_manager)


class AirProducer(Producer):
	"""
	Generated SemanticClass without description

	Source(s): 
		http://www.semanticweb.org/building (building circuits)
	"""

	def __init__(self, *args, **kwargs):
		is_initialised = 'id' in self.__dict__
		super().__init__(*args, **kwargs)
		if not is_initialised:
			self.name._rules = [('exactly|1', [['string']])]

			self.controlCommand._instance_identifier = self.get_identifier()
			self.name._instance_identifier = self.get_identifier()
			self.state._instance_identifier = self.get_identifier()

	# Data fields

	controlCommand: CommandField = CommandField(
		name='controlCommand',
		semantic_manager=semantic_manager)

	name: DataField = DataField(
		name='name',
		rule='exactly 1 string',
		semantic_manager=semantic_manager)

	state: DeviceAttributeField = DeviceAttributeField(
		name='state',
		semantic_manager=semantic_manager)


# ---------Individuals--------- #


class ExampleIndividual(SemanticIndividual):
	_parent_classes: List[type] = []


# ---------Datatypes--------- #
semantic_manager.datatype_catalogue = {
	'MeasurementType': {
		'type': 'enum',
		'enum_values': ['Air_Quality', 'Temperature'],
	},
	'Unit': {
		'type': 'enum',
		'enum_values': ['Celsius', 'Kelvin', 'Relative_Humidity'],
	},
	'rational': {
		'type': 'number',
		'number_decimal_allowed': True,
	},
	'real': {
		'type': 'number',
	},
	'PlainLiteral': {
		'type': 'string',
	},
	'XMLLiteral': {
		'type': 'string',
	},
	'Literal': {
		'type': 'string',
	},
	'anyURI': {
		'type': 'string',
	},
	'base64Binary': {
		'type': 'string',
	},
	'boolean': {
		'type': 'enum',
		'enum_values': ['True', 'False'],
	},
	'byte': {
		'type': 'number',
		'number_range_min': -128,
		'number_range_max': 127,
		'number_has_range': True,
	},
	'dateTime': {
		'type': 'date',
	},
	'dateTimeStamp': {
		'type': 'date',
	},
	'decimal': {
		'type': 'number',
		'number_decimal_allowed': True,
	},
	'double': {
		'type': 'number',
		'number_decimal_allowed': True,
	},
	'float': {
		'type': 'number',
		'number_decimal_allowed': True,
	},
	'hexBinary': {
		'allowed_chars': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'],
		'type': 'string',
	},
	'int': {
		'type': 'number',
		'number_range_min': -2147483648,
		'number_range_max': 2147483647,
		'number_has_range': True,
	},
	'integer': {
		'type': 'number',
	},
	'language': {
		'type': 'string',
	},
	'long': {
		'type': 'number',
		'number_range_min': -9223372036854775808,
		'number_range_max': 9223372036854775807,
		'number_has_range': True,
	},
	'Name': {
		'type': 'string',
	},
	'NCName': {
		'forbidden_chars': [':'],
		'type': 'string',
	},
	'negativeInteger': {
		'type': 'number',
		'number_range_max': -1,
		'number_has_range': True,
	},
	'NMTOKEN': {
		'type': 'string',
	},
	'nonNegativeInteger': {
		'type': 'number',
		'number_range_min': 0,
		'number_has_range': True,
	},
	'nonPositiveInteger': {
		'type': 'number',
		'number_range_max': -1,
		'number_has_range': True,
	},
	'normalizedString': {
		'type': 'string',
	},
	'positiveInteger': {
		'type': 'number',
		'number_range_min': 0,
		'number_has_range': True,
	},
	'short': {
		'type': 'number',
		'number_range_min': -32768,
		'number_range_max': 32767,
		'number_has_range': True,
	},
	'string': {
		'type': 'string',
	},
	'token': {
		'type': 'string',
	},
	'unsignedByte': {
		'type': 'number',
		'number_range_min': 0,
		'number_range_max': 255,
		'number_has_range': True,
	},
	'unsignedInt': {
		'type': 'number',
		'number_range_min': 0,
		'number_range_max': 4294967295,
		'number_has_range': True,
	},
	'unsignedLong': {
		'type': 'number',
		'number_range_min': 0,
		'number_range_max': 18446744073709551615,
		'number_has_range': True,
	},
	'unsignedShort': {
		'type': 'number',
		'number_range_min': 0,
		'number_range_max': 65535,
		'number_has_range': True,
	},
}


class MeasurementType(str, Enum):
	value_Air_Quality = 'Air_Quality'
	value_Temperature = 'Temperature'


class Unit(str, Enum):
	value_Celsius = 'Celsius'
	value_Kelvin = 'Kelvin'
	value_Relative_Humidity = 'Relative_Humidity'


# ---------Class Dict--------- #

semantic_manager.class_catalogue = {
	'AirProducer': AirProducer,
	'Building': Building,
	'Circuit': Circuit,
	'ColdProducer': ColdProducer,
	'Floor': Floor,
	'HeatProducer': HeatProducer,
	'Outlet': Outlet,
	'Producer': Producer,
	'Room': Room,
	'Sensor': Sensor,
	'Tenant': Tenant,
	'Thing': Thing,
	}


semantic_manager.individual_catalogue = {
	'ExampleIndividual': ExampleIndividual,
	}
