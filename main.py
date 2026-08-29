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


def create_stats():
    return {
        "total_events": 0,
        "successful_events": 0,
        "rejected_events": 0,
        "error_stats": {},
    }


def validate_event(event_item):
    errors = []
    valid_event_types = {"barcode_scanned", "scan_failed"}
    if not event_item["device_id"]:
        errors.append("device_id is required")
    if event_item["event_type"] not in valid_event_types:
        errors.append("event_type is invalid")
    if event_item["processing_time_ms"] < 0:
        errors.append("processing_time_ms is less than 0")
    if event_item["event_type"] == "barcode_scanned" and not event_item["barcode"]:
        errors.append("barcode is required")
    return errors


def print_event(event_item):
    print(
        f"{'='*5} Событие успешно: {'='*5}\n"
        f"{'Устройство:':<20} {event_item["device_id"]}\n"
        f"{'Событие:':<20} {event_item["event_type"]}\n"
        f"{'Штрихкод:':<20} {event_item["barcode"]}\n"
        f"{'Время обработки:':<20} {event_item["processing_time_ms"]} мс"
    )


def print_errors(errors_list):
    print(f"{'='*5} Событие отклонено: {'='*5}")
    for error_item in errors_list:
        print(f"- {error_item}")


def print_stats(stats_item):
    print(
        f"{'='*5} Статистика: {'='*5}\n"
        f"Всего событий: {stats_item["total_events"]}\n"
        f"Успешных: {stats_item["successful_events"]}\n"
        f"Отклонённых: {stats_item["rejected_events"]}\n"
    )


def update_error_stats(error_stats, errors_list):
    for error_item in errors_list:
        if error_item not in error_stats:
            error_stats[error_item] = 0

        error_stats[error_item] += 1


def print_error_stats(error_stats):
    print(f"{'='*5} Статистика ошибок {'='*5}")
    for error, count in error_stats.items():
        print(f"{error}: {count}")


def process_event(event_item, stats_dict):
    event_errors = validate_event(event_item)

    if event_errors:
        stats_dict["rejected_events"] += 1

        print_errors(event_errors)
        update_error_stats(stats_dict["error_stats"], event_errors)

    else:
        stats_dict["successful_events"] += 1
        print_event(event_item)

    print(f"\n{'='*50} \n")


def process_events(event_list, stats_dict):
    for event in event_list:
        stats_dict["total_events"] += 1
        process_event(event, stats_dict)


stats = create_stats()
process_events(events, stats)
print_stats(stats)
print_error_stats(stats["error_stats"])
