import numbers

EVENT_REQUIRED_FIELDS = {
    "device_id",
    "event_type",
    "barcode",
    "processing_time_ms",
    "event_id",
}

EVENT_STRING_FIELDS = {
    "device_id",
    "event_type",
    "barcode",
    "event_id",
}

VALID_EVENT_TYPES = {"barcode_scanned", "scan_failed"}


def get_missing_fields(event_item):
    event_fields = set(event_item.keys())

    return set(EVENT_REQUIRED_FIELDS.difference(event_fields))


def get_valid_events_list(events_list):
    valid_events = []
    for key, value in enumerate(events_list):
        if not isinstance(value, dict):
            print(f"Запись #{key} пропущена: ожидался объект события")
        else:
            missing_fields = get_missing_fields(value)
            if not missing_fields:
                valid_events.append(value)
            else:
                print(
                    f"Запись #{key} пропущена: пропущены обязательные поля {missing_fields} в словаре"
                )
    return valid_events


def validate_event(event_item):
    errors = []
    for key, value in event_item.items():
        if key in EVENT_STRING_FIELDS and not isinstance(value, str):
            errors.append(f"{key} is not a string")
    if not event_item["device_id"]:
        errors.append("device_id is required")
    if event_item["event_type"] not in VALID_EVENT_TYPES:
        errors.append("event_type is invalid")
    if (
        not isinstance(event_item["processing_time_ms"], numbers.Number)
        or event_item["processing_time_ms"] < 0
    ):
        errors.append(
            "processing_time_ms is less than 0"
            if isinstance(event_item["processing_time_ms"], numbers.Number)
            else "processing_time_ms is not a number"
        )
    if event_item["event_type"] == "barcode_scanned" and not event_item["barcode"]:
        errors.append("barcode is required")
    return errors
