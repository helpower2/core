"""Constants for Synology DSM."""
from __future__ import annotations

from dataclasses import dataclass

from synology_dsm.api.surveillance_station.const import SNAPSHOT_PROFILE_BALANCED

from homeassistant.const import Platform
from homeassistant.helpers.entity import EntityDescription

DOMAIN = "synology_dsm"
PLATFORMS = [
    Platform.BINARY_SENSOR,
    Platform.BUTTON,
    Platform.CAMERA,
    Platform.SENSOR,
    Platform.SWITCH,
    Platform.UPDATE,
]
COORDINATOR_CAMERAS = "coordinator_cameras"
COORDINATOR_CENTRAL = "coordinator_central"
COORDINATOR_SWITCHES = "coordinator_switches"
SYSTEM_LOADED = "system_loaded"
EXCEPTION_DETAILS = "details"
EXCEPTION_UNKNOWN = "unknown"

# Entry keys
SYNO_API = "syno_api"
UNDO_UPDATE_LISTENER = "undo_update_listener"

# Configuration
CONF_SERIAL = "serial"
CONF_VOLUMES = "volumes"
CONF_DEVICE_TOKEN = "device_token"
CONF_SNAPSHOT_QUALITY = "snap_profile_type"

DEFAULT_USE_SSL = True
DEFAULT_VERIFY_SSL = False
DEFAULT_PORT = 5000
DEFAULT_PORT_SSL = 5001
# Options
DEFAULT_SCAN_INTERVAL = 15  # min
DEFAULT_TIMEOUT = 10  # sec
DEFAULT_SNAPSHOT_QUALITY = SNAPSHOT_PROFILE_BALANCED

ENTITY_UNIT_LOAD = "load"

# Services
SERVICE_REBOOT = "reboot"
SERVICE_SHUTDOWN = "shutdown"
SERVICES = [
    SERVICE_REBOOT,
    SERVICE_SHUTDOWN,
]


@dataclass
class SynologyDSMRequiredKeysMixin:
    """Mixin for required keys."""

    api_key: str


@dataclass
class SynologyDSMEntityDescription(EntityDescription, SynologyDSMRequiredKeysMixin):
    """Generic Synology DSM entity description."""
