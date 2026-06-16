from pathlib import Path


def save_commands(commands, filename):
    output_dir = Path("docs/generated")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / filename

    with open(output_file, "w", encoding="utf-8") as f:
        for command in commands:
            f.write(command + "\n")

    return output_file
