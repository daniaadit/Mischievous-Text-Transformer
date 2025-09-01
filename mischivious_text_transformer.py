import re
from datetime import datetime

def ordinal_suffix(day: int) -> str:
    if 11 <= day % 100 <= 13:
        return "th"
    return {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")

def transform_text(input_text: str) -> str:
    text = input_text

    # 1) Replace explicit phone patterns first (don't use a broad \d+)
    # common formats: 12345-67890 and 10-digit numbers like 9876543210
    text = re.sub(r'\b\d{5}-\d{5}\b', '[REDACTED]', text)
    text = re.sub(r'\b\d{10}\b', '[REDACTED]', text)

    # 2) Convert explicit ISO dates YYYY-MM-DD -> "23rd August 2025"
    date_pattern = r'\b(\d{4})-(\d{2})-(\d{2})\b'
    def date_repl(m):
        year, month, day = m.group(1), m.group(2), m.group(3)
        try:
            dt = datetime.strptime(f"{year}-{month}-{day}", "%Y-%m-%d")
        except ValueError:
            return m.group(0)  # if not a valid date, keep original
        day_int = dt.day
        suffix = ordinal_suffix(day_int)
        return f"{day_int}{suffix} {dt.strftime('%B %Y')}"
    text = re.sub(date_pattern, date_repl, text)

    # 3) Easter egg replacement (word boundary to avoid partial matches)
    text = re.sub(r'\bPython\b', '🐍Python', text)

    return text

if __name__ == "__main__":
    user_text = input("Enter your text: ")
    print("\nTransformed text:")
    print(transform_text(user_text))
