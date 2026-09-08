from dataclasses import dataclass, field
from typing import TypedDict


class EventItem(TypedDict):
    device_id: str
    event_type: str
    barcode: str
    processing_time_ms: int
    event_id: str


@dataclass
class Event:
    device_id: str
    event_type: str
    barcode: str
    processing_time_ms: int
    event_id: str

    def is_successful_scan(self) -> bool:
        return self.event_type == "barcode_scanned"

    def has_barcode(self) -> bool:
        return bool(self.barcode)

    def is_slow(self) -> bool:
        return self.processing_time_ms > 100


@dataclass
class Stats:
    slow_events: int = 0
    total_events: int = 0
    successful_events: int = 0
    rejected_events: int = 0
    successful_events_list: list[Event] = field(default_factory=list)
    error_stats: dict[str, int] = field(default_factory=dict)
    unique_events_ids: set[str] = field(default_factory=set)
    events_by_device: dict[str, int] = field(default_factory=dict)
    events_by_type: dict[str, int] = field(default_factory=dict)


def event_from_dict(event: EventItem) -> Event:
    return Event(**event)
