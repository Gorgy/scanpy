from dataclasses import dataclass
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


class Stats(TypedDict):
    total_events: int
    successful_events: int
    rejected_events: int
    successful_events_list: list[Event]
    error_stats: dict[str, int]
    unique_events_ids: set[str]
    events_by_device: dict[str, int]
    events_by_type: dict[str, int]


def event_from_dict(event: EventItem) -> Event:
    return Event(**event)
