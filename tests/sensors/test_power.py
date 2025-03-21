from homeassistant.components import input_boolean, sensor
from homeassistant.components.utility_meter.sensor import SensorDeviceClass
from homeassistant.const import (
    CONF_ENTITIES,
    CONF_ENTITY_ID,
    CONF_NAME,
    CONF_PLATFORM,
    STATE_OFF,
    STATE_ON,
)
from homeassistant.core import EVENT_HOMEASSISTANT_START, CoreState, HomeAssistant
from homeassistant.setup import async_setup_component
from pytest_homeassistant_custom_component.common import MockEntity, MockEntityPlatform

from custom_components.powercalc.const import (
    ATTR_ENTITIES,
    CONF_CREATE_GROUP,
    CONF_FIXED,
    CONF_MODE,
    CONF_POWER,
    CONF_POWER_SENSOR_ID,
    CONF_POWER_SENSOR_PRECISION,
    CONF_STANDBY_POWER,
    DOMAIN,
    DUMMY_ENTITY_ID,
    CalculationStrategy,
)

from ..common import (
    create_input_boolean,
    create_input_number,
    get_simple_fixed_config,
    run_powercalc_setup_yaml_config,
)


async def test_use_real_power_sensor_in_group(hass: HomeAssistant):
    assert await async_setup_component(
        hass, input_boolean.DOMAIN, {"input_boolean": {"test": None}}
    )

    platform = MockEntityPlatform(hass)
    entity = MockEntity(
        name="existing_power", unique_id="1234", device_class=SensorDeviceClass.POWER
    )
    await platform.async_add_entities([entity])

    await hass.async_block_till_done()

    await async_setup_component(
        hass,
        sensor.DOMAIN,
        {
            sensor.DOMAIN: {
                CONF_PLATFORM: DOMAIN,
                CONF_CREATE_GROUP: "TestGroup",
                CONF_ENTITIES: [
                    {
                        CONF_ENTITY_ID: "sensor.dummy",
                        CONF_POWER_SENSOR_ID: "sensor.existing_power",
                    },
                    {
                        CONF_ENTITY_ID: "input_boolean.test",
                        CONF_MODE: CalculationStrategy.FIXED,
                        CONF_FIXED: {CONF_POWER: 50},
                    },
                ],
            }
        },
    )

    await hass.async_block_till_done()

    group_state = hass.states.get("sensor.testgroup_power")
    assert group_state
    assert group_state.attributes.get(ATTR_ENTITIES) == {
        "sensor.existing_power",
        "sensor.test_power",
    }


async def test_rounding_precision(hass: HomeAssistant):
    await create_input_boolean(hass)

    config = {CONF_POWER_SENSOR_PRECISION: 4}
    await async_setup_component(hass, DOMAIN, {DOMAIN: config})

    await run_powercalc_setup_yaml_config(
        hass,
        get_simple_fixed_config("input_boolean.test", 50),
    )

    state = hass.states.get("sensor.test_power")
    assert state.state == "0.0000"

    hass.states.async_set("input_boolean.test", STATE_ON)
    await hass.async_block_till_done()

    power_state = hass.states.get("sensor.test_power")
    assert power_state.state == "50.0000"


async def test_initial_state_is_calculated_after_startup(hass: HomeAssistant):
    """
    The initial state of the power sensor should be calculated after HA startup completes.
    When we do it already during powercalc setup some entities referred in template could be unknown yet
    """
    hass.state = CoreState.not_running

    await run_powercalc_setup_yaml_config(
        hass,
        {
            CONF_ENTITY_ID: DUMMY_ENTITY_ID,
            CONF_NAME: "Henkie",
            CONF_FIXED: {CONF_POWER: "{{states('input_number.test')}}"},
        },
    )

    await create_input_number(hass, "test", 30)

    hass.bus.async_fire(EVENT_HOMEASSISTANT_START)
    await hass.async_block_till_done()

    assert hass.states.get("sensor.henkie_power").state == "30.00"


async def test_standby_power(hass: HomeAssistant):
    await create_input_boolean(hass)

    await run_powercalc_setup_yaml_config(
        hass,
        {
            CONF_ENTITY_ID: "input_boolean.test",
            CONF_MODE: CalculationStrategy.FIXED,
            CONF_STANDBY_POWER: 0.5,
            CONF_FIXED: {CONF_POWER: 15},
        },
    )

    hass.states.async_set("input_boolean.test", STATE_OFF)
    await hass.async_block_till_done()

    power_state = hass.states.get("sensor.test_power")
    assert power_state.state == "0.50"

    hass.states.async_set("input_boolean.test", STATE_ON)
    await hass.async_block_till_done()

    power_state = hass.states.get("sensor.test_power")
    assert power_state.state == "15.00"
