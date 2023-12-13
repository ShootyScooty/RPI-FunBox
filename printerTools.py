def center_text(text):
    text_width = len(text)
    if text_width >= 32:
        return text  # Text is wider than the line, can't center it

    padding = (32 - text_width) // 2
    centered_text = " " * padding + text
    return centered_text