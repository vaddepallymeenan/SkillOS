#!/usr/bin/env python3
"""
SkillOS Study Timer — frameless, always-on-top desktop widget.
Double-click → toggle compact strip (status-bar height).
Single-click drag → move window freely in both modes.
"""

import tkinter as tk
import json
import time
from datetime import datetime
from pathlib import Path

# ── Palette ───────────────────────────────────────────────────────────────────
BG          = "#0d0f14"
BG_PANEL    = "#13161e"
BORDER_DARK = "#1e2130"
TEXT_PRI    = "#e8eaf0"
TEXT_SEC    = "#5a607a"
TEXT_DIM    = "#2e3348"

AI_ACCENT = "#3b8bff"
AI_DIM    = "#0f2248"
AI_LABEL  = "AI"

CS_ACCENT = "#00e5a0"
CS_DIM    = "#002b1e"
CS_LABEL  = "CYBERSEC"

OUTPUT_PATH = Path(__file__).resolve().parent.parent / "current_session.json"  # served next to skillos.html

MONO_CANDIDATES = [
    "JetBrains Mono", "Fira Code", "Source Code Pro",
    "DejaVu Sans Mono", "Courier New", "monospace"
]

COMPACT_W = 170
COMPACT_H = 26


def best_mono(size=10, weight="normal"):
    import tkinter.font as tkf
    avail = set(tkf.families())
    for f in MONO_CANDIDATES:
        if f in avail:
            return (f, size, weight) if weight != "normal" else (f, size)
    return ("monospace", size)


# ── App ───────────────────────────────────────────────────────────────────────

class SkillOSTimer(tk.Tk):
    def __init__(self):
        super().__init__()

        # fonts
        self.f_label        = best_mono(7)
        self.f_small        = best_mono(8)
        self.f_norm         = best_mono(9)
        self.f_clock        = best_mono(19, "bold")
        self.f_compact_tag  = best_mono(8)
        self.f_compact_clk  = best_mono(9, "bold")

        # per-track independent timer state
        self.track  = "AI"
        self.timers = {
            "AI":      {"elapsed": 0.0, "running": False, "start_ts": None},
            "CYBERSEC":{"elapsed": 0.0, "running": False, "start_ts": None},
        }
        self._acc = AI_ACCENT
        self._dim = AI_DIM

        # UI state
        self._compact       = False
        self._full_geometry = None   # stored as "WxH" string after first build
        self._drag_x        = 0
        self._drag_y        = 0
        self._click_job     = None   # debounce timer id

        # window
        self.overrideredirect(True)
        self.attributes("-topmost", True)
        self.config(bg=BG)
        self.resizable(False, False)
        try:
            self.attributes("-alpha", 0.93)
        except tk.TclError:
            pass

        self._build_full()
        self._build_compact()

        # show full first
        self.full_root.pack(fill="both", expand=True)
        self._apply_theme()

        # measure natural size after layout settles
        self.update_idletasks()
        self._full_geometry = f"{self.winfo_reqwidth()}x{self.winfo_reqheight()}"

        self._center_window()
        self._tick()

    # ── Full UI ───────────────────────────────────────────────────────────────

    def _build_full(self):
        self.full_root = tk.Frame(self, bg=BG, padx=1, pady=1)

        inner = tk.Frame(self.full_root, bg=BG_PANEL, padx=12, pady=10)
        inner.pack(fill="both", expand=True)

        # Top bar
        top = tk.Frame(inner, bg=BG_PANEL)
        top.pack(fill="x", pady=(0, 6))

        logo = tk.Label(top, text="SKILL·OS", font=self.f_small,
                        fg=TEXT_SEC, bg=BG_PANEL, anchor="w")
        logo.pack(side="left")

        btn_x = tk.Label(top, text="✕", font=self.f_small,
                         fg=TEXT_SEC, bg=BG_PANEL, cursor="hand2")
        btn_x.pack(side="right")
        btn_x.bind("<Button-1>", lambda e: self.destroy())
        btn_x.bind("<Enter>",    lambda e: btn_x.config(fg="#ff4060"))
        btn_x.bind("<Leave>",    lambda e: btn_x.config(fg=TEXT_SEC))

        # Track + date row
        track_row = tk.Frame(inner, bg=BG_PANEL)
        track_row.pack(fill="x", pady=(0, 8))

        self.btn_track = tk.Label(track_row, text="", font=self.f_label,
                                  padx=8, pady=2, cursor="hand2", relief="flat")
        self.btn_track.pack(side="left")
        self.btn_track.bind("<Button-1>", self._toggle_track)

        self.lbl_date = tk.Label(track_row, text=datetime.now().strftime("%d %b"),
                                 font=self.f_label, fg=TEXT_SEC, bg=BG_PANEL)
        self.lbl_date.pack(side="right")

        # Clock
        clk_frame = tk.Frame(inner, bg=BG_PANEL)
        clk_frame.pack(fill="x", pady=(0, 10))

        self.lbl_clock_full = tk.Label(clk_frame, text="00:00:00",
                                       font=self.f_clock, fg=TEXT_PRI,
                                       bg=BG_PANEL, anchor="center")
        self.lbl_clock_full.pack(fill="x")

        elapsed_row = tk.Frame(clk_frame, bg=BG_PANEL)
        elapsed_row.pack()

        lbl_el = tk.Label(elapsed_row, text="ELAPSED", font=self.f_label,
                          fg=TEXT_SEC, bg=BG_PANEL)
        lbl_el.pack(side="left")

        btn_rst = tk.Label(elapsed_row, text=" ⟳", font=self.f_label,
                           fg=TEXT_SEC, bg=BG_PANEL, cursor="hand2")
        btn_rst.pack(side="left")
        btn_rst.bind("<Button-1>", lambda e: self._reset_timer())
        btn_rst.bind("<Enter>",    lambda e: btn_rst.config(fg=TEXT_PRI))
        btn_rst.bind("<Leave>",    lambda e: btn_rst.config(fg=TEXT_SEC))

        # Separator
        sep = tk.Frame(inner, bg=BORDER_DARK, height=1)
        sep.pack(fill="x", pady=(0, 10))

        # Action buttons
        btn_row = tk.Frame(inner, bg=BG_PANEL)
        btn_row.pack(fill="x")

        self.btn_start = self._mk_btn(btn_row, "▶  START", self._toggle_start, True)
        self.btn_start.pack(side="left", expand=True, fill="x", padx=(0, 4))

        self.btn_end = self._mk_btn(btn_row, "■  END", self._end_session, False)
        self.btn_end.pack(side="left", expand=True, fill="x")

        # Status
        self.lbl_status = tk.Label(inner, text="ready", font=self.f_label,
                                   fg=TEXT_DIM, bg=BG_PANEL, anchor="w")
        self.lbl_status.pack(fill="x", pady=(6, 0))

        # Bind drag + double-click on all full-mode dragable surfaces
        self._bind_drag_and_toggle(
            self.full_root, inner, top, clk_frame, elapsed_row,
            logo, self.lbl_clock_full, lbl_el, self.lbl_date, sep
        )

    # ── Compact UI ────────────────────────────────────────────────────────────

    def _build_compact(self):
        # No padx/pady on root so entire 26px strip is a click target
        self.compact_root = tk.Frame(self, bg=BG_PANEL, padx=0, pady=0)

        self.lbl_tag_c = tk.Label(self.compact_root, text="",
                                  font=self.f_compact_tag,
                                  padx=8, pady=0, relief="flat", anchor="w")
        self.lbl_tag_c.pack(side="left", fill="y")

        sep_v = tk.Frame(self.compact_root, bg=BORDER_DARK, width=1)
        sep_v.pack(side="left", fill="y", padx=4)

        self.lbl_clock_c = tk.Label(self.compact_root, text="00:00:00",
                                    font=self.f_compact_clk, fg=TEXT_PRI,
                                    bg=BG_PANEL, anchor="w", pady=0, padx=4)
        self.lbl_clock_c.pack(side="left", fill="y")

        # bind all compact widgets + root self as catch-all
        self._bind_drag_and_toggle(
            self, self.compact_root, self.lbl_tag_c, self.lbl_clock_c, sep_v
        )

    # ── Event binding helpers ─────────────────────────────────────────────────

    def _bind_drag_and_toggle(self, *widgets):
        """
        Attach drag (single-click) and compact toggle (double-click) to widgets.
        Uses a 200ms debounce so that the two events don't conflict.
        """
        for w in widgets:
            w.bind("<ButtonPress-1>",   self._on_press)
            w.bind("<B1-Motion>",       self._drag_move)
            w.bind("<Double-Button-1>", self._on_double)

    def _on_press(self, event):
        """Record drag start. Cancel any pending single-click job."""
        self._drag_x = event.x_root - self.winfo_x()
        self._drag_y = event.y_root - self.winfo_y()
        # cancel any pending toggle from a previous single click
        if self._click_job:
            self.after_cancel(self._click_job)
            self._click_job = None

    def _drag_move(self, event):
        x = event.x_root - self._drag_x
        y = event.y_root - self._drag_y
        if self._compact:
            self.geometry(f"{COMPACT_W}x{COMPACT_H}+{x}+{y}")
        else:
            self.geometry(f"+{x}+{y}")

    def _on_double(self, event):
        """Double-click: cancel any pending single-click and toggle mode."""
        if self._click_job:
            self.after_cancel(self._click_job)
            self._click_job = None
        self._toggle_compact()
        return "break"   # stop event propagation

    # ── Compact toggle ────────────────────────────────────────────────────────

    def _toggle_compact(self):
        x = self.winfo_x()
        y = self.winfo_y()

        if not self._compact:
            # → go compact
            self._compact = True
            self.full_root.pack_forget()
            self.compact_root.pack(fill="both", expand=True)
            self.update_idletasks()
            self.geometry(f"{COMPACT_W}x{COMPACT_H}+{x}+{y}")
        else:
            # → restore full
            self._compact = False
            self.compact_root.pack_forget()
            self.full_root.pack(fill="both", expand=True)
            self.update_idletasks()
            geo = self._full_geometry or ""
            self.geometry(f"{geo}+{x}+{y}")

    # ── Button factory ────────────────────────────────────────────────────────

    def _mk_btn(self, parent, text, cmd, primary):
        btn = tk.Label(parent, text=text, font=self.f_norm,
                       padx=8, pady=5, cursor="hand2", relief="flat", bd=0)
        btn.bind("<Button-1>", lambda e: cmd())
        if primary:
            btn.bind("<Enter>", lambda e: btn.config(bg=TEXT_PRI, fg=BG))
            btn.bind("<Leave>", lambda e: btn.config(bg=self._acc, fg=BG))
        else:
            btn.bind("<Enter>", lambda e: btn.config(fg="#ff4060"))
            btn.bind("<Leave>", lambda e: btn.config(fg=TEXT_SEC))
        return btn

    # ── Theme ─────────────────────────────────────────────────────────────────

    def _apply_theme(self):
        is_ai = self.track == "AI"
        acc   = AI_ACCENT if is_ai else CS_ACCENT
        dim   = AI_DIM    if is_ai else CS_DIM
        label = AI_LABEL  if is_ai else CS_LABEL
        self._acc = acc
        self._dim = dim

        self.btn_track.config(text=f"◆ {label}", fg=acc, bg=dim)
        self.lbl_clock_full.config(fg=acc)
        self.btn_start.config(bg=acc, fg=BG)
        self.btn_end.config(bg=BORDER_DARK, fg=TEXT_SEC)

        self.lbl_tag_c.config(text=f"◆ {label}", fg=acc, bg=dim)
        self.lbl_clock_c.config(fg=acc, bg=BG_PANEL)

    # ── Session logic ─────────────────────────────────────────────────────────

    def _toggle_track(self, event=None):
        """Auto-pause current track then switch."""
        # Auto-pause current track if it's running
        cur = self.timers[self.track]
        if cur["running"]:
            cur["elapsed"] += time.monotonic() - cur["start_ts"]
            cur["running"]  = False
            cur["start_ts"] = None

        # Switch track
        self.track = "CYBERSEC" if self.track == "AI" else "AI"
        self._apply_theme()

        # Update button to reflect the new track's state
        t = self.timers[self.track]
        if t["running"]:
            self.btn_start.config(text="⏸  PAUSE")
        elif t["elapsed"] > 0:
            self.btn_start.config(text="▶  RESUME")
        else:
            self.btn_start.config(text="▶  START")
        self._set_status(f"switched → {self.track}")

    def _toggle_start(self):
        t = self.timers[self.track]
        if not t["running"]:
            t["running"]  = True
            t["start_ts"] = time.monotonic()
            self.btn_start.config(text="⏸  PAUSE")
            self._set_status("session active")
        else:
            t["elapsed"]  += time.monotonic() - t["start_ts"]
            t["running"]   = False
            t["start_ts"]  = None
            self.btn_start.config(text="▶  RESUME")
            self._set_status("paused")

    def _reset_timer(self):
        t = self.timers[self.track]
        t["running"]  = False
        t["elapsed"]  = 0.0
        t["start_ts"] = None
        self.btn_start.config(text="▶  START")
        self._refresh_clock()
        self._set_status("timer reset")

    def _end_session(self):
        t = self.timers[self.track]
        if t["running"]:
            t["elapsed"]  += time.monotonic() - t["start_ts"]
            t["running"]   = False
            t["start_ts"]  = None
        if t["elapsed"] < 1:
            self._set_status("nothing to save")
            return
        self._save_session()
        t["elapsed"] = 0.0
        self.btn_start.config(text="▶  START")
        self._refresh_clock()
        self._set_status("session saved ✓")

    def _save_session(self):
        t = self.timers[self.track]
        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        record = {
            "track":   self.track,
            "date":    datetime.now().strftime("%Y-%m-%d"),
            "time":    datetime.now().strftime("%H:%M:%S"),
            "hours":   round(t["elapsed"] / 3600, 4),
            "seconds": round(t["elapsed"], 2),
        }
        sessions = []
        if OUTPUT_PATH.exists():
            try:
                with open(OUTPUT_PATH) as f:
                    data = json.load(f)
                    sessions = data if isinstance(data, list) else [data]
            except (json.JSONDecodeError, ValueError):
                sessions = []
        sessions.append(record)
        with open(OUTPUT_PATH, "w") as f:
            json.dump(sessions, f, indent=2)

    # ── Clock tick ────────────────────────────────────────────────────────────

    def _tick(self):
        self._refresh_clock()
        self.after(200, self._tick)

    def _refresh_clock(self):
        t     = self.timers[self.track]
        total = t["elapsed"]
        if t["running"] and t["start_ts"]:
            total += time.monotonic() - t["start_ts"]
        h = int(total // 3600)
        m = int((total % 3600) // 60)
        s = int(total % 60)
        txt = f"{h:02d}:{m:02d}:{s:02d}"
        self.lbl_clock_full.config(text=txt)
        self.lbl_clock_c.config(text=txt)

    # ── Helpers ───────────────────────────────────────────────────────────────

    def _set_status(self, msg):
        self.lbl_status.config(text=msg)
        self.after(3000, lambda: self.lbl_status.config(text="ready"))

    def _center_window(self):
        self.update_idletasks()
        sw = self.winfo_screenwidth()
        w  = self.winfo_reqwidth()
        self.geometry(f"+{sw - w - 32}+48")


# ── Entry ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app = SkillOSTimer()
    app.mainloop()