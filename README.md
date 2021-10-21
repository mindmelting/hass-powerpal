# Powerpal custom component for Home Assistant

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]

[![hacs][hacsbadge]][hacs]

_Component to integrate with [powerpal][powerpal]._

_This repository and integration is not affiliated with Powerpal._

**This component will set up the following platforms and entities.**

Platform | Description
-- | --
`sensor` | Show info from Powerpal Readings API.

Entity | Description
-- | --
`sensor.powerpal_live_consumption` | Current reading from Powerpal Readings API (updated every minute).
`sensor.powerpal_total_consumption` | Total consumption recorded by Powerpal - entity can be used in Energy Dashboard.

⚠️ Please note ⚠️

For the entities to display up-to-date information - it requires your Powerpal app (which can be running in the background) to be connected to the Powerpal device continuously for it to report near realtime usage information. The current implementation does not retrospectively use historical data - this may come in a future release.

![sensor][sensorimg]

![energy][energyimg]

## Automatic Installation

1. Install HACS
2. Within HA go to HACS > Integrations > ... (in top right corner) > Custom Repositories
3. Add URL: `https://github.com/mindmelting/hass-powerpal`, Category: `Integration`
4. Go to the integrations page inside your home assistant install
5. Search for `Powerpal`
6. Install, enter your Powerpal API Authorization Key and Powerpal Device ID.

## Manual Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `powerpal`.
4. Download _all_ the files from the `custom_components/powerpal/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for `Powerpal`

Using your HA configuration directory (folder) as a starting point you should now also have this:

```text
custom_components/powerpal/translations/en.json
custom_components/powerpal/__init__.py
custom_components/powerpal/config_flow.py
custom_components/powerpal/const.py
custom_components/powerpal/manifest.json
custom_components/powerpal/sensor.py
```

## Configuration is done in the UI

<!---->

## Contributions are welcome

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

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
