import re
from typing import Optional, List

SECTION_HEADERS = [
    "requirements",
    "qualifications",
    "skills",
    "what you will need",
    "what you’ll need",
    "must have",
    "nice to have",
    "experience",
]

STOP_HEADERS = [
    "responsibilities",
    "about the role",
    "about you",
    "benefits",
    "what we offer",
    "company overview",
]

def normalize_text(text: str) -> str:
    text = re.sub(r"<[^>]+>", "\n", text)
    text = re.sub(r"\n{2,}", "\n\n", text)
    return text.strip().lower()

def extract_by_heading(text: str) -> Optional[str]:
    lines = text.split("\n")

    start_idx = None
    for i, line in enumerate(lines):
        clean = line.strip(": ").lower()

        if any(h in clean for h in SECTION_HEADERS):
            start_idx = i + 1
            break

    if start_idx is None:
        return None

    extracted = []
    for line in lines[start_idx:]:
        clean = line.strip().lower()

        if any(h in clean for h in STOP_HEADERS):
            break

        extracted.append(line)

    result = "\n".join(extracted).strip()
    return result if len(result) > 50 else None

def extract_bullet_block(text: str) -> Optional[str]:
    blocks = text.split("\n\n")

    bullet_blocks = []
    for block in blocks:
        lines = block.split("\n")
        bullet_count = sum(1 for l in lines if l.strip().startswith(("-", "•", "*")))

        if bullet_count >= 3:
            bullet_blocks.append(block)

    if not bullet_blocks:
        return None

    return max(bullet_blocks, key=len)

def extract_requirements(description: str) -> str:
    text = normalize_text(description)

    for extractor in (extract_by_heading, extract_bullet_block):
        result = extractor(text)
        if result:
            return result

    return text