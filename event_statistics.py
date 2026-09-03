from schema_data import EventItem, Stats


def create_stats() -> Stats:
    return {
        "total_events": 0,
        "successful_events": 0,
        "successful_events_list": [],
        "rejected_events": 0,
        "error_stats": {},
        "unique_events_ids": set(),
        "events_by_device": {},
        "events_by_type": {},
    }


def get_duplicate_event_ids(events_list: list[EventItem]) -> set[str]:
    dict_events = {}
    for event in events_list:
        if event["event_id"] not in dict_events:
            dict_events[event["event_id"]] = 1
        else:
            dict_events[event["event_id"]] += 1
    return {key for key, value in dict_events.items() if value > 1}


def update_error_stats(error_stats: dict[str, int], errors_list: list[str]) -> None:
    for error_item in errors_list:
        if error_item not in error_stats:
            error_stats[error_item] = 0

        error_stats[error_item] += 1


def update_events(stats_dict_item: dict[str, int], event_item: str) -> None:
    if event_item:
        if event_item not in stats_dict_item:
            stats_dict_item[event_item] = 0
        stats_dict_item[event_item] += 1


def get_barcodes(events_list: list[EventItem]) -> list[str]:
    return [
        event["barcode"]
        for event in events_list
        if event["barcode"] and isinstance(event["barcode"], str)
    ]


def get_unique_barcodes(events_list: list[EventItem]) -> set[str]:
    return {
        event["barcode"]
        for event in events_list
        if event["barcode"] and isinstance(event["barcode"], str)
    }


def get_events_dict_by_event_id(
    events_list: list[EventItem],
) -> dict[str, EventItem]:
    return {event["event_id"]: event for event in events_list}
