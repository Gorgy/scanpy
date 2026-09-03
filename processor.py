from reporting import print_errors, print_event
from event_statistics import update_error_stats, update_events
from schema_data import EventItem, Stats
from validation import validate_event


def process_event(event_item: EventItem, stats_dict: Stats) -> None:
    event_errors = validate_event(event_item)
    if event_errors:
        stats_dict["rejected_events"] += 1
        print_errors(event_errors)
        update_error_stats(stats_dict["error_stats"], event_errors)

    else:
        stats_dict["successful_events"] += 1
        stats_dict["successful_events_list"].append(event_item)
        stats_dict["unique_events_ids"].add(event_item["event_id"])
        update_events(stats_dict["events_by_device"], event_item["device_id"])
        update_events(stats_dict["events_by_type"], event_item["event_type"])
        print_event(event_item)


def process_events(event_list: list[EventItem], stats_dict: Stats) -> None:
    for value in event_list:
        stats_dict["total_events"] += 1
        process_event(value, stats_dict)
