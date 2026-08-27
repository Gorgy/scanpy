events = [
    {
        "device_id": "scanner-001",
        "event_type": "barcode_scanned",
        "barcode": "5901234123457",
        "processing_time_ms": 42,
    },
    {
        "device_id": "",
        "event_type": "unknown",
        "barcode": "",
        "processing_time_ms": -5,
    },
    {
        "device_id": "scanner-002",
        "event_type": "scan_failed",
        "barcode": "5901234123457",
        "processing_time_ms": -5,
    },
    {
        "device_id": "scanner-003",
        "event_type": "barcode_scanned",
        "barcode": "",
        "processing_time_ms": 500,
    },
]


def validate_event(event_item):
    errors = []

    if not event_item["device_id"]:
        errors.append("device_id is required")

    if event_item["event_type"] not in {"barcode_scanned", "scan_failed"}:
        errors.append("event_type is invalid")

    if event_item["processing_time_ms"] < 0:
        errors.append("processing_time_ms is less than 0")

    if event_item["event_type"] == "barcode_scanned" and not event_item["barcode"]:
        errors.append("barcode is required")

    return errors


for event in events:
    event_errors = validate_event(event)

    if event_errors:
        print("Событие отклонено:")

        for error in event_errors:
            print(f"- {error}")

    else:
        print("Событие успешно:")
        print(f"{'Устройство:':<20} {event["device_id"]}")
        print(f"{'Событие:':<20} {event["event_type"]}")
        print(f"{'Штрихкод:':<20} {event["barcode"]}")
        print(f"{'Время обработки:':<20} {event["processing_time_ms"]} мс")

    print(f"\n{'='*50} \n")
