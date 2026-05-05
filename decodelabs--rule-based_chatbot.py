# PROJECT 1: THE RULE-BASED AI CHATBOT
# Organization : DecodeLabs
# Architect : Nikil Abbishak

# 'datetime' is a standard library module. No pip install needed.
import datetime

# --- CONFIGURATION & KNOWLEDGE BASE ---
# Using a dictionary for fast lookup and easy maintenance
KNOWLEDGE_BASE = {
    "hello"        : "Hello! Welcome to DecodeLabs Assistant. How can I help you today?",
    "hi"           : "Hi there! Great to see you. What can I do for you?",
    "hey"          : "Hey! I'm your DecodeLabs Rule-Based AI. Ask me anything!",
    "good morning" : "Good Morning! Hope you're ready to build something amazing today.",
    "good evening" : "Good Evening! DecodeLabs Assistant is active and ready.",

# The bot reports its own operational status.
    "status"       : " System Status: ALL SYSTEMS OPERATIONAL. Running on Rule-Based Engine v1.0.",
    "are you alive": "Yes! I am fully operational. My logic engine is running at peak efficiency.",
    "how are you"  : "I am a deterministic system — I don't have feelings, but my uptime is 100%!",

# A structured help response guides the user experience.
    "help"         : (
        "\n DECODELABS ASSISTANT — HELP MENU\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "  Commands you can try:\n"
        "  → 'hello', 'status', 'time', 'project info', 'about', 'batch', 'exit'\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    ),

# Domain-specific knowledge about the project itself
    "project info" : (
        "\n PROJECT 1: THE RULE-BASED AI CHATBOT\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "  Type : White-Box Deterministic System\n"
        "  Logic: Dictionary-based intent resolution\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    ),

    "about"        : "DecodeLabs focuses on training the next generation of AI engineers.",
    "batch"        : "Batch 2026: 'Build it right before you build it smart.'",
}


#THE SANITIZER (Data Normalization Pipeline)
def sanitize_input(user_text: str) -> str:
    """Cleans input to ensure case and whitespace don't break lookups."""
    return user_text.lower().strip()

def get_response(intent: str) -> str:
    """Fetches response from KB with a default fallback."""
    return KNOWLEDGE_BASE.get(
        intent, 
        "❓ I don't recognize that command. Type 'help' for options."
    )

def handle_dynamic_intents(intent: str) -> str | None:
    """Handles intents that require real-time data (like time)."""
    if intent == "time":
        now = datetime.datetime.now()
        return f" Date: {now.strftime('%A, %B %d, %Y')} | Time: {now.strftime('%I:%M:%S %p')}"
    return None

def run_chatbot():
    """Main execution loop for the assistant."""
    print("\n" + "=" * 50)
    print("    DECODELABS AI ASSISTANT (Project 1)")
    print("   Type 'exit' to quit.")
    print("=" * 50 + "\n")

    while True:
        try:
            user_input = input("You → ")
        except (KeyboardInterrupt, EOFError):
            print("\nShutting down...")
            break

        clean_intent = sanitize_input(user_input)

        # 1. Check for empty input
        if not clean_intent:
            continue

        # 2. Check for exit command
        if clean_intent == "exit":
            print("Bot → Goodbye! Keep building. ")
            break

        # 3. Check for dynamic responses (e.g. Time)
        dynamic_reply = handle_dynamic_intents(clean_intent)
        if dynamic_reply:
            print(f"Bot → {dynamic_reply}\n")
            continue

        # 4. Standard Knowledge Base lookup
        response = get_response(clean_intent)
        print(f"Bot → {response}\n")

if __name__ == "__main__":
    run_chatbot()