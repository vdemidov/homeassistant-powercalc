"""The Powercalc constants."""

from datetime import timedelta

from homeassistant.backports.enum import StrEnum
from homeassistant.components.utility_meter.const import DAILY, MONTHLY, WEEKLY
from homeassistant.const import (
    STATE_NOT_HOME,
    STATE_OFF,
    STATE_STANDBY,
    STATE_UNAVAILABLE,
)

MIN_HA_VERSION = "2022.2"

DOMAIN = "powercalc"
DOMAIN_CONFIG = "config"

DATA_CALCULATOR_FACTORY = "calculator_factory"
DATA_CONFIGURED_ENTITIES = "configured_entities"
DATA_DISCOVERED_ENTITIES = "discovered_entities"
DATA_DOMAIN_ENTITIES = "domain_entities"
DATA_USED_UNIQUE_IDS = "used_unique_ids"
DATA_PROFILE_LIBRARY = "profile_library"

DUMMY_ENTITY_ID = "sensor.dummy"

CONF_AREA = "area"
CONF_CALIBRATE = "calibrate"
CONF_CREATE_GROUP = "create_group"
CONF_CREATE_DOMAIN_GROUPS = "create_domain_groups"
CONF_CREATE_ENERGY_SENSOR = "create_energy_sensor"
CONF_CREATE_ENERGY_SENSORS = "create_energy_sensors"
CONF_CREATE_UTILITY_METERS = "create_utility_meters"
CONF_DAILY_FIXED_ENERGY = "daily_fixed_energy"
CONF_ENABLE_AUTODISCOVERY = "enable_autodiscovery"
CONF_ENERGY_INTEGRATION_METHOD = "energy_integration_method"
CONF_ENERGY_SENSOR_CATEGORY = "energy_sensor_category"
CONF_ENERGY_SENSOR_ID = "energy_sensor_id"
CONF_ENERGY_SENSOR_NAMING = "energy_sensor_naming"
CONF_ENERGY_SENSOR_FRIENDLY_NAMING = "energy_sensor_friendly_naming"
CONF_ENERGY_SENSOR_PRECISION = "energy_sensor_precision"
CONF_ENERGY_SENSOR_UNIT_PREFIX = "energy_sensor_unit_prefix"
CONF_FIXED = "fixed"
CONF_FORCE_UPDATE_FREQUENCY = "force_update_frequency"
CONF_GROUP = "group"
CONF_GROUP_POWER_ENTITIES = "group_power_entities"
CONF_GROUP_ENERGY_ENTITIES = "group_energy_entities"
CONF_GROUP_MEMBER_SENSORS = "group_member_sensors"
CONF_GAMMA_CURVE = "gamma_curve"
CONF_HIDE_MEMBERS = "hide_members"
CONF_IGNORE_UNAVAILABLE_STATE = "ignore_unavailable_state"
CONF_INCLUDE = "include"
CONF_LINEAR = "linear"
CONF_MODEL = "model"
CONF_MANUFACTURER = "manufacturer"
CONF_MODE = "mode"
CONF_MULTIPLY_FACTOR = "multiply_factor"
CONF_MULTIPLY_FACTOR_STANDBY = "multiply_factor_standby"
CONF_POWER_FACTOR = "power_factor"
CONF_POWER_SENSOR_CATEGORY = "power_sensor_category"
CONF_POWER_SENSOR_NAMING = "power_sensor_naming"
CONF_POWER_SENSOR_FRIENDLY_NAMING = "power_sensor_friendly_naming"
CONF_POWER_SENSOR_PRECISION = "power_sensor_precision"
CONF_POWER = "power"
CONF_POWER_SENSOR_ID = "power_sensor_id"
CONF_POWER_TEMPLATE = "power_template"
CONF_MIN_POWER = "min_power"
CONF_MAX_POWER = "max_power"
CONF_ON_TIME = "on_time"
CONF_TEMPLATE = "template"
CONF_SENSOR_TYPE = "sensor_type"
CONF_SUB_PROFILE = "sub_profile"
CONF_UPDATE_FREQUENCY = "update_frequency"
CONF_VALUE = "value"
CONF_VALUE_TEMPLATE = "value_template"
CONF_VOLTAGE = "voltage"
CONF_WLED = "wled"
CONF_STATES_POWER = "states_power"
CONF_START_TIME = "start_time"
CONF_STANDBY_POWER = "standby_power"
CONF_SUB_GROUPS = "sub_groups"
CONF_CALCULATION_ENABLED_CONDITION = "calculation_enabled_condition"
CONF_DISABLE_STANDBY_POWER = "disable_standby_power"
CONF_CUSTOM_MODEL_DIRECTORY = "custom_model_directory"
CONF_UTILITY_METER_OFFSET = "utility_meter_offset"
CONF_UTILITY_METER_TYPES = "utility_meter_types"
CONF_UTILITY_METER_TARIFFS = "utility_meter_tariffs"

# Redefine constants from integration component.
# Has been refactored in HA 2022.4, we need to support older HA versions as well.
ENERGY_INTEGRATION_METHOD_LEFT = "left"
ENERGY_INTEGRATION_METHOD_RIGHT = "right"
ENERGY_INTEGRATION_METHOD_TRAPEZODIAL = "trapezoidal"
ENERGY_INTEGRATION_METHODS = [
    ENERGY_INTEGRATION_METHOD_LEFT,
    ENERGY_INTEGRATION_METHOD_RIGHT,
    ENERGY_INTEGRATION_METHOD_TRAPEZODIAL,
]


class UnitPrefix(StrEnum):
    """Allowed unit prefixes."""

    NONE = "none"
    KILO = "k"
    MEGA = "M"


ENTITY_CATEGORY_CONFIG = "config"
ENTITY_CATEGORY_DIAGNOSTIC = "diagnostic"
ENTITY_CATEGORY_NONE = None
ENTITY_CATEGORY_SYSTEM = "system"
ENTITY_CATEGORIES = [
    ENTITY_CATEGORY_CONFIG,
    ENTITY_CATEGORY_DIAGNOSTIC,
    ENTITY_CATEGORY_NONE,
    ENTITY_CATEGORY_SYSTEM,
]

DEFAULT_UPDATE_FREQUENCY = timedelta(minutes=10)
DEFAULT_POWER_NAME_PATTERN = "{} power"
DEFAULT_POWER_SENSOR_PRECISION = 2
DEFAULT_ENERGY_INTEGRATION_METHOD = ENERGY_INTEGRATION_METHOD_TRAPEZODIAL
DEFAULT_ENERGY_NAME_PATTERN = "{} energy"
DEFAULT_ENERGY_SENSOR_PRECISION = 4
DEFAULT_ENTITY_CATEGORY = ENTITY_CATEGORY_NONE
DEFAULT_UTILITY_METER_TYPES = [DAILY, WEEKLY, MONTHLY]

DISCOVERY_SOURCE_ENTITY = "source_entity"
DISCOVERY_POWER_PROFILE = "power_profile"

ATTR_CALCULATION_MODE = "calculation_mode"
ATTR_ENERGY_SENSOR_ENTITY_ID = "energy_sensor_entity_id"
ATTR_ENTITIES = "entities"
ATTR_INTEGRATION = "integration"
ATTR_IS_GROUP = "is_group"
ATTR_SOURCE_ENTITY = "source_entity"
ATTR_SOURCE_DOMAIN = "source_domain"

SERVICE_RESET_ENERGY = "reset_energy"
SERVICE_CALIBRATE_UTILITY_METER = "calibrate_utility_meter"

MODE_LUT = "lut"
MODE_LINEAR = "linear"
MODE_FIXED = "fixed"
MODE_WLED = "wled"

OFF_STATES = (STATE_OFF, STATE_NOT_HOME, STATE_STANDBY, STATE_UNAVAILABLE)


class CalculationStrategy(StrEnum):
    """Possible virtual power calculation strategies."""

    LUT = "lut"
    LINEAR = "linear"
    FIXED = "fixed"
    WLED = "wled"


class SensorType(StrEnum):
    """Possible modes for a number selector."""

    DAILY_ENERGY = "daily_energy"
    VIRTUAL_POWER = "virtual_power"
    GROUP = "group"
