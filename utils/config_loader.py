import json
from pathlib import Path
from typing import Any, Dict


def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    path = Path(config_path)

    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with path.open("r", encoding="utf-8") as file:
        config = json.load(file)

    return config
