# SkillOS — AI Learning Mission Control

A single-page study OS for two learning tracks — **AI/ML Engineering** and **Cybersecurity** — with an AI mentor, skill tracking and a desktop focus timer.

## Features
- **Roadmap + skill levels** — a curated curriculum ([Full_map.md](Full_map.md)) with per-topic progress
- **AI mentor** — Gemini (with backup key fallback) / Groq-powered explanations, practice sessions and discussions ([mentor_flow.md](mentor_flow.md))
- **Practice tracker** — saved sessions, completed topics, hands-on cyber labs (recon, scanning, exploitation)
- **Study timer widget** — frameless, always-on-top Tkinter timer that syncs the active session into the dashboard

## Tech
Vanilla HTML/CSS/JS · Gemini & Groq APIs · Python/Tkinter · localStorage

## Run
```bash
python -m http.server 8080          # then open http://localhost:8080/skillos.html
python timer-widget/timer.py        # optional desktop timer
```
Add your Gemini/Groq API keys in **Settings** (stored only in your browser).

## Structure
```
skillos.html              # the app
timer-widget/timer.py     # desktop study timer
Full_map.md, Full_pipline.md, mentor_flow.md   # curriculum + mentor design
```
