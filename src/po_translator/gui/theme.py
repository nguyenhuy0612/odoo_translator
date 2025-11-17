"""Modern theme system with light/dark mode support and professional styling."""

from __future__ import annotations

import customtkinter as ctk
from typing import Literal


class ModernTheme:
    """Professional theme system with light/dark mode support."""

    # Theme mode
    MODE: Literal["light", "dark"] = "light"

    # Light mode colors
    LIGHT = {
        # Base backgrounds - Modern gradient approach
        "BACKGROUND": "#f8fafc",  # Soft off-white
        "SURFACE": "#ffffff",  # Pure white cards
        "SURFACE_ALT": "#f1f5f9",  # Subtle gray
        "SURFACE_RAISED": "#ffffff",  # Elevated cards
        "SURFACE_HOVER": "#e2e8f0",  # Interactive hover
        "SURFACE_BORDER": "#e2e8f0",  # Subtle borders

        # Sidebar - Modern sidebar design
        "SIDEBAR_BG": "#ffffff",
        "SIDEBAR_BORDER": "#e2e8f0",
        "SIDEBAR_SCROLLBAR": "#cbd5e1",
        "SIDEBAR_SCROLLBAR_HOVER": "#94a3b8",

        # Typography - Better contrast and hierarchy
        "TEXT_PRIMARY": "#0f172a",  # Almost black
        "TEXT_SECONDARY": "#334155",  # Dark gray
        "TEXT_MUTED": "#64748b",  # Medium gray
        "TEXT_PLACEHOLDER": "#94a3b8",  # Light gray
        "TEXT_INVERSE": "#ffffff",  # White text

        # Accent colors - Modern, vibrant palette
        "ACCENT_PRIMARY": "#3b82f6",  # Bright blue
        "ACCENT_PRIMARY_HOVER": "#2563eb",  # Darker blue
        "ACCENT_PRIMARY_LIGHT": "#dbeafe",  # Light blue
        "ACCENT_SECONDARY": "#06b6d4",  # Cyan
        "ACCENT_SECONDARY_HOVER": "#0891b2",
        "ACCENT_SUCCESS": "#10b981",  # Emerald
        "ACCENT_SUCCESS_HOVER": "#059669",
        "ACCENT_SUCCESS_LIGHT": "#d1fae5",
        "ACCENT_WARNING": "#f59e0b",  # Amber
        "ACCENT_WARNING_HOVER": "#d97706",
        "ACCENT_WARNING_LIGHT": "#fef3c7",
        "ACCENT_DANGER": "#ef4444",  # Red
        "ACCENT_DANGER_HOVER": "#dc2626",
        "ACCENT_DANGER_LIGHT": "#fee2e2",

        # Table colors - Clean and readable
        "TABLE_HEADER_BG": "#f8fafc",
        "TABLE_HEADER_BORDER": "#e2e8f0",
        "TABLE_ROW_BG": "#ffffff",
        "TABLE_ROW_ALT_BG": "#f8fafc",
        "TABLE_ROW_SELECTED": "#dbeafe",
        "TABLE_ROW_HOVER": "#f1f5f9",
        "TABLE_SOURCE_MISMATCH": "#fee2e2",
        "TABLE_TRANSLATION_MISSING": "#fef3c7",
        "TABLE_TRANSLATION_MISMATCH": "#fce7f3",

        # Badges and chips - Modern pill design
        "BADGE_SOURCE": "#dbeafe",
        "BADGE_SOURCE_TEXT": "#1e40af",
        "BADGE_SOURCE_MISMATCH": "#fef3c7",
        "BADGE_SOURCE_MISMATCH_TEXT": "#92400e",
        "BADGE_TRANSLATION": "#d1fae5",
        "BADGE_TRANSLATION_TEXT": "#065f46",
        "BADGE_TRANSLATION_MISMATCH": "#fce7f3",
        "BADGE_TRANSLATION_MISMATCH_TEXT": "#9f1239",
        "MODULE_CHIP_BG": "#f1f5f9",
        "MODULE_CHIP_TEXT": "#3b82f6",
        "MODULE_CHIP_BORDER": "#cbd5e1",

        # Input fields - Modern input design
        "INPUT_BG": "#ffffff",
        "INPUT_BORDER": "#e2e8f0",
        "INPUT_HOVER": "#f1f5f9",
        "INPUT_FOCUS": "#3b82f6",
        "INPUT_FOCUS_BORDER": "#3b82f6",

        # Dividers and separators
        "DIVIDER": "#e2e8f0",
        "DIVIDER_LIGHT": "#f1f5f9",

        # Shadows (for future use with canvas)
        "SHADOW_COLOR": "#00000015",
        "SHADOW_COLOR_HOVER": "#00000025",
    }

    # Premium Dark Theme - Gucci Style (Luxury & Professional)
    DARK = {
        # Base backgrounds - Deep, rich tones
        "BACKGROUND": "#0a0e1a",  # Deep navy (almost black)
        "SURFACE": "#141b2d",  # Rich dark blue
        "SURFACE_ALT": "#1a2332",  # Slightly lighter
        "SURFACE_RAISED": "#1f2937",  # Elevated elements
        "SURFACE_HOVER": "#2d3748",  # Interactive hover
        "SURFACE_BORDER": "#2d3748",

        # Sidebar - Elegant separation
        "SIDEBAR_BG": "#0f1419",  # Darker than main for depth
        "SIDEBAR_BORDER": "#1f2937",
        "SIDEBAR_SCROLLBAR": "#374151",
        "SIDEBAR_SCROLLBAR_HOVER": "#4b5563",

        # Typography - Crystal clear hierarchy
        "TEXT_PRIMARY": "#ffffff",  # Pure white for maximum contrast
        "TEXT_SECONDARY": "#e5e7eb",  # Soft white
        "TEXT_MUTED": "#9ca3af",  # Medium gray
        "TEXT_PLACEHOLDER": "#6b7280",  # Subtle gray
        "TEXT_INVERSE": "#0a0e1a",

        # Accent colors - Vibrant and premium (always readable text)
        "ACCENT_PRIMARY": "#3b82f6",  # Electric blue
        "ACCENT_PRIMARY_HOVER": "#2563eb",  # Deeper blue
        "ACCENT_PRIMARY_LIGHT": "#1e40af",
        "ACCENT_SECONDARY": "#14b8a6",  # Teal (premium feel)
        "ACCENT_SECONDARY_HOVER": "#0d9488",
        "ACCENT_SUCCESS": "#10b981",  # Emerald green (better contrast)
        "ACCENT_SUCCESS_HOVER": "#059669",
        "ACCENT_SUCCESS_LIGHT": "#047857",
        "ACCENT_WARNING": "#f59e0b",  # Gold/amber
        "ACCENT_WARNING_HOVER": "#d97706",
        "ACCENT_WARNING_LIGHT": "#b45309",
        "ACCENT_DANGER": "#ef4444",  # Bright red
        "ACCENT_DANGER_HOVER": "#dc2626",
        "ACCENT_DANGER_LIGHT": "#b91c1c",

        # Table colors - Clean and elegant
        "TABLE_HEADER_BG": "#1a2332",
        "TABLE_HEADER_BORDER": "#2d3748",
        "TABLE_ROW_BG": "#141b2d",
        "TABLE_ROW_ALT_BG": "#0f1419",
        "TABLE_ROW_SELECTED": "#1e3a8a",  # Deep blue selection
        "TABLE_ROW_HOVER": "#1f2937",
        # Very subtle tints for status (barely visible, text is bright)
        "TABLE_SOURCE_MISMATCH": "#1a1414",  # Barely red
        "TABLE_TRANSLATION_MISSING": "#1a1814",  # Barely orange
        "TABLE_TRANSLATION_MISMATCH": "#1a1418",  # Barely pink

        # Badge colors - Bright and clear
        "BADGE_SOURCE": "#60a5fa",  # Bright blue
        "BADGE_SOURCE_TEXT": "#93c5fd",
        "BADGE_SOURCE_MISMATCH": "#fbbf24",  # Bright gold
        "BADGE_SOURCE_MISMATCH_TEXT": "#fcd34d",
        "BADGE_TRANSLATION": "#4ade80",  # Bright green
        "BADGE_TRANSLATION_TEXT": "#86efac",
        "BADGE_TRANSLATION_MISMATCH": "#f472b6",  # Bright pink
        "BADGE_TRANSLATION_MISMATCH_TEXT": "#f9a8d4",
        "MODULE_CHIP_BG": "#1f2937",  # Subtle background
        "MODULE_CHIP_TEXT": "#60a5fa",  # Bright blue text
        "MODULE_CHIP_BORDER": "#374151",

        # Input fields - Clean and modern
        "INPUT_BG": "#1a2332",
        "INPUT_BORDER": "#374151",
        "INPUT_HOVER": "#1f2937",
        "INPUT_FOCUS": "#3b82f6",
        "INPUT_FOCUS_BORDER": "#60a5fa",

        # Dividers - Subtle separation
        "DIVIDER": "#2d3748",
        "DIVIDER_LIGHT": "#1f2937",

        # Shadows - Depth and elevation
        "SHADOW_COLOR": "#00000050",
        "SHADOW_COLOR_HOVER": "#00000070",
    }

    # Typography settings - Premium fonts
    FONT_FAMILY = "Inter"  # Modern, clean font (fallback to Segoe UI)
    FONT_FAMILY_FALLBACK = "Segoe UI"  # Windows standard
    FONT_FAMILY_MONO = "JetBrains Mono"  # Modern monospace (fallback to Consolas)
    FONT_FAMILY_MONO_FALLBACK = "Consolas"

    def __init__(self, mode: Literal["light", "dark"] = "light"):
        """Initialize theme with specified mode."""
        self.MODE = mode
        self._colors = self.LIGHT if mode == "light" else self.DARK

    @property
    def colors(self) -> dict:
        """Get current color palette."""
        return self._colors

    def get(self, key: str, default: str = "#000000") -> str:
        """Get color value by key."""
        return self._colors.get(key, default)

    def set_mode(self, mode: Literal["light", "dark"]):
        """Switch theme mode."""
        self.MODE = mode
        self._colors = self.LIGHT if mode == "light" else self.DARK
        # Update CustomTkinter appearance mode immediately
        ctk.set_appearance_mode(mode)

    def toggle_mode(self):
        """Toggle between light and dark mode."""
        new_mode = "dark" if self.MODE == "light" else "light"
        self.set_mode(new_mode)
        return new_mode

    @staticmethod
    def font(size: int = 12, weight: str = "normal", family: str = None) -> ctk.CTkFont:
        """Create a themed font instance with fallback."""
        if family is None:
            # Try Inter first, fallback to Segoe UI
            try:
                return ctk.CTkFont(family="Inter", size=size, weight=weight)
            except:
                return ctk.CTkFont(family="Segoe UI", size=size, weight=weight)
        return ctk.CTkFont(family=family, size=size, weight=weight)

    @staticmethod
    def font_mono(size: int = 12, weight: str = "normal") -> ctk.CTkFont:
        """Create a monospace font instance."""
        return ctk.CTkFont(family=ModernTheme.FONT_FAMILY_MONO, size=size, weight=weight)

    def darken_color(self, hex_color: str, amount: int = 20) -> str:
        """Darken a hex color by specified amount."""
        hex_color = hex_color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        r = max(0, r - amount)
        g = max(0, g - amount)
        b = max(0, b - amount)
        return f"#{r:02x}{g:02x}{b:02x}"

    def lighten_color(self, hex_color: str, amount: int = 20) -> str:
        """Lighten a hex color by specified amount."""
        hex_color = hex_color.lstrip('#')
        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        r = min(255, r + amount)
        g = min(255, g + amount)
        b = min(255, b + amount)
        return f"#{r:02x}{g:02x}{b:02x}"

    def get_button_text_color(self, bg_color: str) -> str:
        """Determine appropriate text color for button background."""
        hex_color = bg_color.lstrip('#')
        if len(hex_color) != 6:
            return self.get("TEXT_PRIMARY")

        r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        brightness = (0.299 * r) + (0.587 * g) + (0.114 * b)
        return self.get("TEXT_INVERSE") if brightness < 160 else self.get("TEXT_PRIMARY")

    def __getattr__(self, name: str):
        """Support attribute access for backward compatibility."""
        if name in self._colors:
            return self.get(name)
        if hasattr(super(), name):
            return getattr(super(), name)
        raise AttributeError(f"Theme has no attribute '{name}'")


# Global theme instance - always dark mode
THEME = ModernTheme("dark")
# Ensure CustomTkinter uses dark mode
ctk.set_appearance_mode("dark")


def apply_root_theme(root) -> None:
    """Apply the base theme colors to the root window."""
    root.configure(fg_color=THEME.get("BACKGROUND"))


def switch_theme_mode(mode: Literal["light", "dark"] = None):
    """Switch theme mode globally and update CustomTkinter."""
    if mode is None:
        mode = THEME.toggle_mode()
    else:
        THEME.set_mode(mode)
    # Force CustomTkinter to update appearance
    ctk.set_appearance_mode(mode)
    return mode


def get_theme() -> ModernTheme:
    """Get the current theme instance."""
    return THEME
