from pathlib import Path
from typing import Any

from loader import load_events_from_json
from processor import process_events
from reporting import print_report
from schema_data import EventItem, Stats
from validation import get_valid_events_list
from event_statistics import (
    create_stats,
    get_duplicate_event_ids,
    get_barcodes,
    get_unique_barcodes,
    get_events_dict_by_event_id,
)


def main() -> None:
    events_list: list[dict[str, Any]] = load_events_from_json(
        Path(__file__).parent / "data" / "events.json"
    )
    events: list[EventItem] = get_valid_events_list(events_list)

    stats: Stats = create_stats()
    successful_events: list[EventItem] = stats["successful_events_list"]

    process_events(events, stats)

    barcodes: list[str] = get_barcodes(successful_events)
    barcodes_unique: set[str] = get_unique_barcodes(successful_events)
    events_dict: dict[str, EventItem] = get_events_dict_by_event_id(successful_events)
    duplicate: set[str] = get_duplicate_event_ids(successful_events)

    print_report(stats, barcodes, barcodes_unique, events_dict, duplicate)


if __name__ == "__main__":
    main()
