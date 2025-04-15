def human_friendly_time(seconds: float) -> str:
    """Convert seconds into a human-friendly format (hours, minutes, seconds)."""
    hours, remainder = divmod(int(seconds), 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}h {minutes}m {seconds}s"

def print_banner(message: str):
    """Print a stylized banner message."""
    banner = f"\n{'='*len(message)}\n{message}\n{'='*len(message)}\n"
    print(banner)
