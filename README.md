# DecodeLabs-AI-Project1
Deterministic "White Box" chatbot built for the DecodeLabs Industrial Training Kit. Implements an IPO model using a Python hash map for $O(1)$ constant-time lookup to ensure performance at scale. Features include a sanitization pipeline (.lower().strip()) and zero-hallucination logic for industrial-grade precision.



STRCUTURE

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
