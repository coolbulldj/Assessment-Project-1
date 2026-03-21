from pygame import freetype as ft
from .GUIBase import GUIBase

fontCache = {}
seperator = " "  # allows for array of text lines to be combined


def GetFont(Name):
    if Name not in fontCache.keys():
        fontCache[Name] = ft.SysFont(Name, 1)
    return fontCache[Name]


def GetScaledTextSize(text: str, font: ft.SysFont, abSize):
    if not text or text == "":
        raise ValueError("text can't be none or ''")

    ab_xs, ab_ys = abSize
    # Start large
    base_size = 100
    font.size = base_size

    # Measure at base size
    ts = font.get_rect(text)
    text_width, text_height = ts.width, ts.height

    if text_width == 0 or text_height == 0:
        return 1

    # Calculate scale factors (scale is ratio of allowed pixels to measured pixels)
    scale_x = ab_xs / text_width
    scale_y = ab_ys / text_height

    # Pick smallest so text fits inside box
    scale = min(scale_x, scale_y)

    # Return an integer font size that will fit
    new_size = max(1, int(base_size * scale))
    return new_size


def DetermineWrap(
    text: str, font: ft.SysFont, absoluteSize: tuple
):  # returns a list of lines
    if not text:
        return []

    words = text.split(seperator)
    if len(words) == 1:
        return [text]

    xs, ys = absoluteSize

    # Try from 1 row up to number of words (worst case)
    for rows in range(1, len(words) + 1):
        # Compute a font size that fits vertically for this number of rows
        per_row_height = ys / rows
        # Use the whole text to get a conservative font size for vertical fit
        font_size_for_rows = GetScaledTextSize(text, font, (xs, per_row_height * rows))
        # But we need the font to fit vertically per row, so recompute using per-row height
        font_size_for_rows = GetScaledTextSize("Mg", font, (xs, per_row_height))
        font.size = font_size_for_rows

        lines = []
        current = []

        for w in words:
            candidate = seperator.join(current + [w]) if current else w
            rect = font.get_rect(candidate)

            # If candidate fits horizontally, accept it
            if rect.width <= xs:
                current.append(w)
            else:
                # If current is empty, the single word is wider than xs at this font size.
                # Force it into its own line (we could also reduce font size, but we already
                # chose a font size that fits vertically; this keeps behavior predictable).
                if not current:
                    lines.append(w)
                else:
                    lines.append(seperator.join(current))
                    current = [w]

            # If we've already exceeded the allowed number of rows, this rows count fails
            if len(lines) > rows:
                break

        if current:
            lines.append(seperator.join(current))

        # If the produced lines fit within the allowed rows, return them
        if len(lines) <= rows:
            return lines

    # Fallback: no wrap found (shouldn't happen), return original as single line
    return [text]


class TextLabel(GUIBase):
    def __init__(
        self,
        Pos,
        Size,
        BackgroundColor,
        BackgroundTransparency,
        TextColor,
        TextFont="monospace",
        TextSize: int = 1,
        zIndex=1,
        UIAspectRatio=None,
        TextScaled: bool = True,
    ):
        super().__init__(
            Pos,
            Size,
            BackgroundColor,
            BackgroundTransparency,  # BackgroundTransparency
            zIndex,
            UIAspectRatio,
            "TextLabel",
            [
                "TextScaled",
                "Text",
                "TextColor",
                "TextSize",
                "TextFont",
                "TextWrapped",
                "StartWrapSize",
            ],
            ["Text"],
        )
        self.TextScaled = TextScaled
        self.TextWrapped = True
        self.TextColor = TextColor
        self.TextSize = TextSize
        self.TextFont = TextFont
        self.Text = ""

    def refresh(self, screen):
        super().refresh(screen)
        if self.Text == "":
            return
        ab_xs, ab_ys = self.AbsoluteSize
        pos_x, pos_y = self.AbsolutePos
        wrapLines = [self.Text]

        font = GetFont(self.TextFont)

        if self.TextScaled:
            # First try to wrap the text into lines that fit
            wrapLines = (
                DetermineWrap(self.Text, font, self.AbsoluteSize)
                if self.TextWrapped
                else [self.Text]
            )

            # Compute a font size that fits vertically for the number of lines
            rows = max(1, len(wrapLines))
            per_row_height = ab_ys / rows
            # Determine a font size that fits the widest line horizontally and the per-row height vertically
            # Start with a candidate size that fits vertically
            candidate_size = GetScaledTextSize(
                self.Text, font, (ab_xs, per_row_height * rows)
            )
            # But better to compute per-line sizes and pick the minimum
            per_line_sizes = []
            for line in wrapLines:
                s = GetScaledTextSize(line, font, (ab_xs, per_row_height))
                per_line_sizes.append(s)
            # Use the smallest per-line size so all lines fit horizontally and vertically
            new_size = max(1, min(per_line_sizes))
            font.size = new_size
        else:
            font.size = self.TextSize

        # Render single-line centered
        if not wrapLines or len(wrapLines) == 1:
            ts = font.get_rect(self.Text)
            fx, fy = ts.width, ts.height
            pos = (pos_x + ab_xs / 2 - fx / 2), (pos_y + ab_ys / 2 - fy / 2)
            font.render_to(screen, pos, self.Text, fgcolor=self.TextColor, bgcolor=None)
            return

        # Render wrapped lines, centered horizontally and vertically distributed
        rows = len(wrapLines)
        sample_rect = font.get_rect("Mg")
        line_height = sample_rect.height
        total_text_height = line_height * rows
        start_y = pos_y + (ab_ys - total_text_height) / 2

        for index, line in enumerate(wrapLines):
            ts = font.get_rect(line)
            fx, fy = ts.width, ts.height
            x = pos_x + (ab_xs - fx) / 2
            y = start_y + index * line_height
            font.render_to(screen, (x, y), line, fgcolor=self.TextColor, bgcolor=None)
