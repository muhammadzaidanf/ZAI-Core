def clean_text(text: str) -> str:
    """Basic text cleaner function."""
    cleaned = text.lower().strip()
    print(f"[DataHandler] Cleaned text: {cleaned}")
    return cleaned
