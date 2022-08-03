"""Test irrigation_unlimited coordinator entity operations."""
from datetime import datetime
import homeassistant.core as ha
import homeassistant.util.dt as dt
from homeassistant.const import (
    ATTR_ICON,
    STATE_OK,
)
from custom_components.irrigation_unlimited.const import (
    ATTR_CONTROLLER_COUNT,
)
from tests.iu_test_support import IUExam, mk_local

IUExam.quiet_mode()


# pylint: disable=unused-argument
async def test_coordinator_entity(
    hass: ha.HomeAssistant, skip_dependencies, skip_history
):
    """Test coordinator entity."""
    # pylint: disable=too-many-statements

    async with IUExam(hass, "test_coordinator_entity.yaml") as exam:
        await exam.begin_test(1)

        await exam.run_until("2021-01-04 06:02")
        sta = hass.states.get("irrigation_unlimited.coordinator")
        assert sta.state == STATE_OK
        assert sta.attributes[ATTR_ICON] == "mdi:zodiac-aquarius"
        assert sta.attributes[ATTR_CONTROLLER_COUNT] == 1
        assert exam.lvt(sta.attributes["next_tick"]) == mk_local("2021-01-04 06:05")

        await exam.run_until("2021-01-04 06:07")
        sta = hass.states.get("irrigation_unlimited.coordinator")
        assert exam.lvt(sta.attributes["next_tick"]) == mk_local("2021-01-04 06:07:30")

        await exam.run_until("2021-01-04 06:11:30")
        sta = hass.states.get("irrigation_unlimited.coordinator")
        assert exam.lvt(sta.attributes["next_tick"]) == mk_local("2021-01-04 06:12")

        await exam.run_until("2021-01-04 06:29")
        sta = hass.states.get("irrigation_unlimited.coordinator")
        assert exam.lvt(sta.attributes["next_tick"]) == mk_local("2021-01-04 06:30")

        await exam.finish_test()

        tick_log: list[datetime] = []
        test = exam.coordinator.tester.last_test
        sta = hass.states.get("irrigation_unlimited.coordinator")
        for atime in sta.attributes["tick_log"]:
            tick_log.append(test.virtual_time(dt.as_utc(atime)))
        assert tick_log == [
            mk_local("2021-01-04 06:30:00"),
            mk_local("2021-01-04 06:24:00"),
            mk_local("2021-01-04 06:23:30"),
            mk_local("2021-01-04 06:23:00"),
            mk_local("2021-01-04 06:22:30"),
            mk_local("2021-01-04 06:22:00"),
            mk_local("2021-01-04 06:21:30"),
            mk_local("2021-01-04 06:21:00"),
            mk_local("2021-01-04 06:20:30"),
            mk_local("2021-01-04 06:20:00"),
            mk_local("2021-01-04 06:19:30"),
            mk_local("2021-01-04 06:19:00"),
            mk_local("2021-01-04 06:18:30"),
            mk_local("2021-01-04 06:18:00"),
            mk_local("2021-01-04 06:17:30"),
            mk_local("2021-01-04 06:17:00"),
            mk_local("2021-01-04 06:16:30"),
            mk_local("2021-01-04 06:16:00"),
            mk_local("2021-01-04 06:15:30"),
            mk_local("2021-01-04 06:15:00"),
            mk_local("2021-01-04 06:14:30"),
            mk_local("2021-01-04 06:14:00"),
            mk_local("2021-01-04 06:13:30"),
            mk_local("2021-01-04 06:13:00"),
            mk_local("2021-01-04 06:12:30"),
            mk_local("2021-01-04 06:12:00"),
            mk_local("2021-01-04 06:11:00"),
            mk_local("2021-01-04 06:10:30"),
            mk_local("2021-01-04 06:10:00"),
            mk_local("2021-01-04 06:09:30"),
            mk_local("2021-01-04 06:09:00"),
            mk_local("2021-01-04 06:08:30"),
            mk_local("2021-01-04 06:08:00"),
            mk_local("2021-01-04 06:07:30"),
            mk_local("2021-01-04 06:07:00"),
            mk_local("2021-01-04 06:06:30"),
            mk_local("2021-01-04 06:06:00"),
            mk_local("2021-01-04 06:05:30"),
            mk_local("2021-01-04 06:05:00"),
        ]
        exam.check_summary()
