import json
from pathlib import Path
from typing import Any


def load_events_from_json(path: Path) -> list[dict[str, Any]]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            print("Не удалось загрузить события: ожидался список событий")
            return []
        return data
    except FileNotFoundError as e:
        print(f"Ошибка чтения файла: {e.filename}")
        return []
    except json.JSONDecodeError as e:
        print(f"JSON поврежден: {e.msg} on {e.lineno};{e.colno}")
        return []
