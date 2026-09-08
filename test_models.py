from models import Event


def test_successful_event_methods() -> None:
    event = Event(
        **{
            "device_id": "scanner-003",
            "event_type": "barcode_scanned",
            "barcode": "5901234123567",
            "processing_time_ms": 500,
            "event_id": "evt-005",
        }
    )
    assert event.is_successful_scan() is True
    assert event.is_slow() is True
    assert event.has_barcode() is True


def test_failed_event_methods() -> None:
    event2 = Event(
        **{
            "device_id": "scanner-002",
            "event_type": "scan_failed",
            "barcode": "",
            "processing_time_ms": 100,
            "event_id": "evt-006",
        }
    )
    assert event2.is_successful_scan() is False
    assert event2.is_slow() is False
    assert event2.has_barcode() is False


if __name__ == "__main__":
    test_successful_event_methods()
    test_failed_event_methods()
    print("All tests passed")
