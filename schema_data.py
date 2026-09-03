from typing import TypedDict


class EventItem(TypedDict):
    device_id: str
    event_type: str
    barcode: str
    processing_time_ms: int
    event_id: str


class Stats(TypedDict):
    total_events: int
    successful_events: int
    rejected_events: int
    successful_events_list: list[EventItem]
    error_stats: dict[str, int]
    unique_events_ids: set[str]
    events_by_device: dict[str, int]
    events_by_type: dict[str, int]
