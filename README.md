# Rule-Based AI Chatbot | DecodeLabs Industrial Training
Developed a deterministic "White Box" chatbot designed for high-efficiency intent resolution. The system utilizes an IPO (Input-Process-Output) architecture with a Python dictionary backbone to achieve $O(1)$ constant-time lookup, avoiding the technical debt of linear if-elif ladders. Key features include a data sanitization pipeline for input normalization and an infinite conversational loop with an integrated exit strategy. 

## Industrial Insights
As part of the DecodeLabs curriculum, this project demonstrates the "Engineer's Mindset": mastering the precision of a logic engine before managing the chaos of probabilistic models (LLMs).

# SYSTEM ARCHITECTURE

USER INTERFACE ───────────────────────────────────────────────────────────────────────────> OUTPUT

┌───────────┐      ┌──────────────┐      ┌─────────────────┐      ┌──────────────────────┐
│ RAW INPUT │ ───> │ SANITIZATION │ ───> │  LOGIC ENGINE   │ ───> │  GENERATED RESPONSE  │
└───────────┘      └──────┬───────┘      └────────┬────────┘      └──────────────────────┘
                          │                       │
                ┌─────────┴─────────┐   ┌─────────┴─────────┐      ┌──────────────────────┐
                │ .lower().strip()  │   │  KNOWLEDGE BASE   │ ───> │  FALLBACK / DEFAULT  │
                │ Normalization     │   │ Dictionary / O(1) │      └──────────────────────┘
                └───────────────────┘   └───────────────────┘

EXIT FLOW ────────────────────────────────────────────────────────────────────────────────> SHUTDOWN

┌───────────────┐      ┌──────────────┐      ┌───────────────┐      ┌──────────────────────┐
│ 'exit' STRING │ ───> │ LOOP CHECKER │ ───> │ BREAK COMMAND │ ───> │  GRACEFUL TERMINATION│
└───────────────┘      └──────────────┘      └───────────────┘      └──────────────────────┘


### Quick Start
1. Clone the repository:

git clone <your-repo-url>

2. Run the assistant:

python main.py
