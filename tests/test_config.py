"""Test irrigation_unlimited user configurations. Not exactly a test
   but a place to check if configuration files are valid and possibly
   debug them."""
# pylint: disable=unused-import
from datetime import timedelta, datetime
import json
import pytest
import homeassistant.core as ha
from custom_components.irrigation_unlimited.const import (
    DOMAIN,
    SERVICE_TIME_ADJUST,
)
from tests.iu_test_support import IUExam

IUExam.quiet_mode()

# Remove the following decorator to run test
# @pytest.mark.skip
async def test_config(hass: ha.HomeAssistant, skip_dependencies, skip_history):
    """Test loading of a config."""
    # pylint: disable=unused-argument

    async with IUExam(hass, "test_config.yaml") as exam:

        # """Prevent checking results. Helpful for just outputting results"""
        # exam.no_check()

        # Run a single test
        # await exam.begin_test(1)
        # print(json.dumps(exam.coordinator.as_dict(), default=str))
        # await exam.finish_test()

        # Run all tests
        # await exam.run_all()

        # Run a test with a service call
        # await exam.begin_test(1)
        # await hass.services.async_call(
        #     DOMAIN,
        #     SERVICE_TIME_ADJUST,
        #     {
        #         "entity_id": "binary_sensor.irrigation_unlimited_c1_m",
        #         "sequence_id": 1,
        #         "zones": 0,
        #         "actual": "00:10",
        #     },
        #     True,
        # )
        # await exam.finish_test()

        # Run to a point in time
        # await exam.begin_test(1)
        # await exam.run_until(datetime.fromisoformat("2021-01-04 06:02:00+00:00"))
        # await exam.finish_test()

        # Run for a period of time
        # await exam.begin_test(1)
        # await exam.run_for(timedelta(minutes=15))
        # await exam.finish_test()

        exam.check_summary()
