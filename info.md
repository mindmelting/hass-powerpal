[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]

[![hacs][hacsbadge]][hacs]
[![Project Maintenance][maintenance-shield]][user_profile]

_Component to integrate with [powerpal][powerpal]._

_This repository and integration is not affiliated with Powerpal._

**This component will set up the following platforms.**

Platform | Description
-- | --
`sensor` | Show info from Powerpal Readings API.

Entity | Description
-- | --
`sensor.powerpal_live_consumption` | Current reading from Powerpal Readings API (updated every minute).
`sensor.powerpal_total_consumption` | Total consumption recorded by Powerpal - entity can be used in Energy Dashboard.

![sensor][sensorimg]

![energy][energyimg]

{% if not installed %}

## Installation

1. Click install.
1. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Powerpal".

{% endif %}

## Configuration is done in the UI

<!---->

***

[powerpal]: https://github.com/mindmelting/powerpal
[commits-shield]: https://img.shields.io/github/commit-activity/y/mindmelting/hass-powerpal.svg?style=for-the-badge
[commits]: https://github.com/mindmelting/hass-powerpal/commits/master
[hacs]: https://hacs.xyz
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/mindmelting/hass-powerpal.svg?style=for-the-badge
[releases]: https://github.com/mindmelting/hass-powerpal/releases
[sensorimg]: sensor.png
[energyimg]: energy.png