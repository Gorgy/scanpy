from models import Event, Stats


def print_header(title: str) -> None:
    print(f"\n{'='*5} {title} {'='*5}")


def print_stats(stats_item: Stats) -> None:
    print_header("Статистика:")
    print(
        f"Всего событий: {stats_item["total_events"]}\n"
        f"Успешных: {stats_item["successful_events"]}\n"
        f"Отклонённых: {stats_item["rejected_events"]}"
    )


def print_event(event_item: Event) -> None:
    print_header("Событие успешно:")
    print(
        f"{'Устройство:':<20} {event_item.device_id}\n"
        f"{'Событие:':<20} {event_item.event_type}\n"
        f"{'Штрихкод:':<20} {event_item.barcode}\n"
        f"{'Время обработки:':<20} {event_item.processing_time_ms} мс"
    )


def print_errors(errors_list: list[str]) -> None:
    print_header("Событие отклонено:")
    for error_item in errors_list:
        print(f"- {error_item}")


def print_barcodes(
    barcodes_list: list[str] | set[str], title: str = "Штрихкоды:"
) -> None:
    if len(barcodes_list) != 0:
        print_header(title)
        for barcode in barcodes_list:
            print(f"- {barcode}")


def print_error_stats(stats_dict: Stats) -> None:
    error_stats = stats_dict["error_stats"]
    if error_stats:
        print_header("Статистика ошибок")
    for error, count in error_stats.items():
        print(f"{error}: {count}")


def print_events_by_device(stats_dict: Stats) -> None:
    events_by_device = stats_dict["events_by_device"]
    events_by_type = stats_dict["events_by_type"]
    events_ids = stats_dict["unique_events_ids"]

    print(f"\nУникальных событий: {len(events_ids)}")
    if events_by_device:
        print_header("Событий по устройствам:")
    for key, value in events_by_device.items():
        print(f"{key}: {value}")

    if events_by_type:
        print_header("Событий по типу:")
    for key, value in events_by_type.items():
        print(f"{key}: {value}")


def print_duplicate_events(duplicate_ids: set[str]) -> None:
    if len(duplicate_ids) > 0:
        print(f"Дубликаты: {duplicate_ids}")
    else:
        print("Дубликатов нет")


def print_events_len(events_dict: dict[str, Event]) -> None:
    print(f"Событий по ID: {len(events_dict)}")


def print_report(
    stats: Stats,
    barcodes: list[str],
    barcodes_unique: set[str],
    events_dict: dict[str, Event],
    duplicate: set[str],
) -> None:
    print_stats(stats)
    print_error_stats(stats)
    print_events_by_device(stats)
    print_barcodes(barcodes)
    print_barcodes(barcodes_unique, "Уникальные штрихкоды")
    print_events_len(events_dict)
    print_duplicate_events(duplicate)
