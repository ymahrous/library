def require_positive(value, name):
    if value <= 0:
        raise ValueError(f"{name} must be positive")