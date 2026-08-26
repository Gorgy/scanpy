events = {
    "device_id": "scanner-001",
    "event_type": "barcode_scanned",
    "barcode": "5901234123457",
    "processing_time_ms": 42
}

print(f"{'Устройство:':<20} {events["device_id"]}")
print(f"{'Событие:':<20} {events["event_type"]}")
print(f"{'Штрихкод:':<20} {events["barcode"]}")
print(f"{'Время обработки:':<20} {events["processing_time_ms"]} мс")