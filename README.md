# DecodeLabs-AI-Project1

> **Project 1 — Rule-Based AI Chatbot** | DecodeLabs Industrial Training Kit

A deterministic **"White Box"** chatbot built for the DecodeLabs Industrial Training Kit. Implements an **IPO (Input → Process → Output)** model using a Python hash map for **O(1)** constant-time lookup to ensure performance at scale. Features include a sanitization pipeline (`.lower().strip()`) and zero-hallucination logic for industrial-grade precision.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Info](#project-info)

---

## Overview

This chatbot operates as a fully deterministic, rule-based system — every response is explicitly defined. There is no machine learning, no probabilistic guessing, and no hallucination. Input is normalized, matched against a knowledge base, and a precise response is returned.

---

## Features

- ⚡ **O(1) Lookup** — Python dictionary-based knowledge base for constant-time response retrieval
- 🧹 **Sanitization Pipeline** — `.lower().strip()` normalization ensures consistent intent matching
- 🕐 **Dynamic Intents** — Real-time data handling (e.g., current date and time)
- 🔒 **Zero-Hallucination** — All responses are explicitly defined; unknown inputs return a safe fallback
- 🚪 **Graceful Exit** — Clean shutdown via `exit` command or `Ctrl+C` / `EOF`

---

## Architecture

### Main Flow — USER INTERFACE → OUTPUT

```
┌───────────┐      ┌──────────────┐      ┌─────────────────┐      ┌──────────────────────┐
│ RAW INPUT │ ───> │ SANITIZATION │ ───> │  LOGIC ENGINE   │ ───> │  GENERATED RESPONSE  │
└───────────┘      └──────┬───────┘      └────────┬────────┘      └──────────────────────┘
                          │                       │
                ┌─────────┴─────────┐   ┌─────────┴─────────┐      ┌──────────────────────┐
                │ .lower().strip()  │   │  KNOWLEDGE BASE   │ ───> │  FALLBACK / DEFAULT  │
                │ Normalization     │   │ Dictionary / O(1) │      └──────────────────────┘
                └───────────────────┘   └───────────────────┘
```

### Exit Flow → SHUTDOWN

```
┌───────────────┐      ┌──────────────┐      ┌───────────────┐      ┌──────────────────────┐
│ 'exit' STRING │ ───> │ LOOP CHECKER │ ───> │ BREAK COMMAND │ ───> │  GRACEFUL TERMINATION│
└───────────────┘      └──────────────┘      └───────────────┘      └──────────────────────┘
```

---

## Getting Started

### Prerequisites

- Python 3.10 or higher (uses `str | None` union type syntax)

### Run the Chatbot

```bash
python decodelabs--rule-based_chatbot.py
```

---

## Usage

Once running, type any of the following commands at the `You →` prompt:

| Command        | Description                              |
|----------------|------------------------------------------|
| `hello`        | Greeting response                        |
| `hi` / `hey`   | Alternate greetings                      |
| `good morning` | Time-of-day greeting                     |
| `good evening` | Time-of-day greeting                     |
| `status`       | System operational status                |
| `are you alive`| Uptime check                             |
| `how are you`  | Bot self-report                          |
| `time`         | Returns current date and time            |
| `project info` | Details about this project               |
| `about`        | About DecodeLabs                         |
| `batch`        | Batch 2026 motto                         |
| `help`         | Lists all available commands             |
| `exit`         | Gracefully shuts down the assistant      |

---

## Project Info

| Field        | Detail                                      |
|--------------|---------------------------------------------|
| **Project**  | Project 1 — The Rule-Based AI Chatbot       |
| **Type**     | White-Box Deterministic System              |
| **Logic**    | Dictionary-based intent resolution          |
| **Author**   | Nikil Abbishak                              |
| **Org**      | DecodeLabs                                  |
| **Batch**    | 2026 — *"Build it right before you build it smart."* |
