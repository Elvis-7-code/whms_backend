def validate_required_fields(data, fields):
    for field in fields:
        if field not in data:
            raise ValueError(f"{field} is required")