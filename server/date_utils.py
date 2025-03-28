from datetime import datetime, timedelta

def calculate_date_time(data):
    input_str = data.get("input", "").lower().strip()
    if not input_str:
        raise ValueError("Missing or empty 'input'")

    number, unit, *_ = input_str.replace("ago", "").strip().split()
    number = int(number)

    now = datetime.now()

    match unit.rstrip("s"):
        case "minute" | "min":
            result = now - timedelta(minutes=number)
        case "hour":
            result = now - timedelta(hours=number)
        case "day":
            result = now - timedelta(days=number)
        case "week":
            result = now - timedelta(weeks=number)
        case "month":
            result = now - timedelta(days=30 * number)
        case _:
            raise ValueError(f"Unsupported time unit: {unit}")

    return result.isoformat()
