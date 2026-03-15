"""
SEC EDGAR 10-K parser for Starbucks filings.

Supports three format patterns:
  - "xbrl"  : Inline XBRL HTM (FY2019-FY2025), minified with <span> tags
  - "html"  : Standard HTML (FY2001-FY2018), various formatting styles
  - "txt"   : Plain text with SGML wrapper (FY1996-FY2000)
"""

import re
from pathlib import Path
from bs4 import BeautifulSoup


def detect_format(filepath: str | Path) -> str:
    """Detect the 10-K file format: 'xbrl', 'html', or 'txt'."""
    filepath = Path(filepath)
    text = filepath.read_text(encoding="utf-8", errors="replace")[:10000]

    if filepath.suffix == ".txt":
        return "txt"
    if "ix:nonnumeric" in text.lower() or "ix:header" in text.lower() or "xmlns:ix" in text:
        return "xbrl"
    return "html"


def _normalize_whitespace(text: str) -> str:
    """Collapse whitespace and blank lines."""
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"^\s+$", "", text, flags=re.MULTILINE)
    return text.strip()


def _soup_to_text(html: str) -> str:
    """Parse HTML with BeautifulSoup, return clean rendered text."""
    soup = BeautifulSoup(html, "html.parser")
    # Remove hidden elements (XBRL headers, etc.)
    for hidden in soup.find_all(style=re.compile(r"display\s*:\s*none")):
        hidden.decompose()
    text = soup.get_text(separator="\n")
    return _normalize_whitespace(text)


def _find_item1_boundaries(text: str) -> tuple[int, int]:
    """Find start/end positions of Item 1 in rendered text.

    Returns (start, end) character positions, or (-1, -1) if not found.
    """
    # Match "Item 1" or "ITEM 1" followed by "Business" (with optional dot/spaces)
    pattern_start = re.compile(
        r"Item\s+1\.?\s*[.\u2014\u2013\-]?\s*Business",
        re.IGNORECASE,
    )
    # End marker: Item 1A or Item 2
    pattern_end = re.compile(
        r"Item\s+1A\.?\s",
        re.IGNORECASE,
    )

    matches = list(pattern_start.finditer(text))
    if not matches:
        return (-1, -1)

    # Skip TOC: find the match followed by >5000 chars before next Item marker
    for m in reversed(matches):
        start = m.end()
        end_match = pattern_end.search(text, start)
        if end_match:
            section_len = end_match.start() - start
            if section_len > 5000:
                return (start, end_match.start())

    # Fallback: use last match
    start = matches[-1].end()
    end_match = pattern_end.search(text, start)
    end_pos = end_match.start() if end_match else len(text)
    return (start, end_pos)


def _extract_item1_txt(text: str) -> str:
    """Extract Item 1 from plain-text 10-K (FY1996-FY2000)."""
    # Remove SGML tags (<PAGE>, <PAGE 4>, etc.)
    text = re.sub(r"<[A-Z]+[^>]*>\s*", "", text)

    pattern_start = re.compile(
        r"^\s*ITEM\s+1\.?\s+BUSINESS",
        re.MULTILINE | re.IGNORECASE,
    )
    pattern_end = re.compile(
        r"^\s*ITEM\s+(?:1A|2)\.?\s",
        re.MULTILINE | re.IGNORECASE,
    )

    matches = list(pattern_start.finditer(text))
    if not matches:
        return ""

    start = matches[-1].end()
    end_match = pattern_end.search(text, start)
    if end_match:
        return text[start : end_match.start()].strip()
    return text[start:].strip()


def _extract_item1_html(text: str) -> str:
    """Extract Item 1 from HTML 10-K (FY2001-FY2018)."""
    rendered = _soup_to_text(text)
    start, end = _find_item1_boundaries(rendered)
    if start == -1:
        return ""
    return rendered[start:end].strip()


def _extract_item1_xbrl(text: str) -> str:
    """Extract Item 1 from Inline XBRL 10-K (FY2019-FY2025)."""
    rendered = _soup_to_text(text)
    start, end = _find_item1_boundaries(rendered)
    if start == -1:
        return ""
    return rendered[start:end].strip()


def extract_item1(filepath: str | Path) -> str:
    """Extract Item 1 (Business) text from a 10-K filing."""
    filepath = Path(filepath)
    fmt = detect_format(filepath)
    text = filepath.read_text(encoding="utf-8", errors="replace")

    if fmt == "txt":
        return _extract_item1_txt(text)
    elif fmt == "html":
        return _extract_item1_html(text)
    elif fmt == "xbrl":
        return _extract_item1_xbrl(text)
    else:
        raise ValueError(f"Unknown format: {fmt}")


def extract_items(filepath: str | Path) -> dict[str, str]:
    """Extract major Items from a 10-K filing. Currently only Item 1."""
    return {"item1": extract_item1(filepath)}
