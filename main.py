from pathlib import Path
from loader import load_events_from_json
from processor import process_events
from reporting import print_report
from validation import get_valid_events_list
from event_statistics import (
    create_stats,
    get_duplicate_event_ids,
    get_barcodes,
    get_unique_barcodes,
    get_events_dict_by_event_id,
)


def main():
    events_list = load_events_from_json(Path(__file__).parent / "data" / "events.json")
    events = get_valid_events_list(events_list)

    stats = create_stats()
    successful_events = stats["successful_events_list"]

    process_events(events, stats)

    barcodes = get_barcodes(successful_events)
    barcodes_unique = get_unique_barcodes(successful_events)
    events_dict = get_events_dict_by_event_id(successful_events)
    duplicate = get_duplicate_event_ids(successful_events)

    print_report(stats, barcodes, barcodes_unique, events_dict, duplicate)


if __name__ == "__main__":
    main()
