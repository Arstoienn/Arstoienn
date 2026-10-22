#!/usr/bin/env python3
"""Draw the contact pills next to this file: thin outline chips like a GitHub topic label.

  python3 assets/cards.py

Each pill gets a light and a dark SVG; the README picks one with <picture>.
"""
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
CHAR_W = 7.2  # width of one 12px monospace character

PILLS = [  # file slug, icon, icon color, text
    ("email", "mail", "#5a8aa6", "wushane316@gmail.com"),
    ("discord", "discord", "#5865f2", "arstoienn"),
]

ICONS = {
    "mail": "M3.5 5h17A1.5 1.5 0 0 1 22 6.5v11a1.5 1.5 0 0 1-1.5 1.5h-17A1.5 1.5 0 0 1 2 17.5v-11A1.5 1.5 0 0 1 3.5 5zm8.5 7.6L4.3 7.2v.9L12 13.5l7.7-5.4v-.9z",
    "discord": "M20.317 4.37a19.79 19.79 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.865-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.74 19.74 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.058a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994a.076.076 0 0 0-.041-.106 13.1 13.1 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.291.074.074 0 0 1 .077-.01c3.928 1.793 8.18 1.793 12.061 0a.074.074 0 0 1 .079.009c.12.099.246.198.373.292a.077.077 0 0 1-.006.127 12.3 12.3 0 0 1-1.873.892.077.077 0 0 0-.041.106c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.84 19.84 0 0 0 6.002-3.03.077.077 0 0 0 .032-.055c.5-5.177-.838-9.674-3.549-13.66a.06.06 0 0 0-.031-.029zM8.02 15.33c-1.183 0-2.157-1.086-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.095 2.157 2.42 0 1.332-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.086-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.095 2.157 2.42 0 1.332-.946 2.418-2.157 2.418z",
}

THEMES = {  # GitHub's own page, border and text colors
    "light": {"bg": "#ffffff", "border": "#d1d9e0", "fg": "#1f2328"},
    "dark": {"bg": "#0d1117", "border": "#3d444d", "fg": "#e6edf3"},
}


def pill(icon, color, text, t):
    tw = round(len(text) * CHAR_W)
    w, h = 32 + tw + 12, 28
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">
<title>{escape(text)}</title>
<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="{h / 2 - .5}" fill="{t['bg']}" stroke="{t['border']}"/>
<svg x="11" y="7" width="14" height="14" viewBox="0 0 24 24"><path fill="{color}" d="{ICONS[icon]}"/></svg>
<text x="32" y="18.5" font-family="{MONO}" font-size="12" fill="{t['fg']}" textLength="{tw}" lengthAdjust="spacing">{escape(text)}</text>
</svg>
"""


if __name__ == "__main__":
    for slug, icon, color, text in PILLS:
        for theme, colors in THEMES.items():
            (HERE / f"{slug}-{theme}.svg").write_text(pill(icon, color, text, colors))
