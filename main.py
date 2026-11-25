"""Midnight Fridge Roast — one-line entry.

The joke: a smart fridge that locks at midnight and flashes
"wellness mode" is acting like a smug life coach instead of an appliance.
The punchline turns the fridge's own health lecture back on it — it is a
fridge, not a therapist — so the midnight refusal itself is the target:
an appliance that bought into diet culture and now polices its owner
at the exact hour the cravings start.
"""

ENTRY = (
    "My smart fridge locks at midnight and flashes "
    "'wellness mode' \u2014 mate, you're a fridge, not my therapist."
)

if __name__ == "__main__":
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as fh:
            fh.write(ENTRY)
    except OSError:
        pass
    try:
        import os

        os.makedirs("output", exist_ok=True)
        with open("output/entry.txt", "w", encoding="utf-8") as fh:
            fh.write(ENTRY)
    except OSError:
        pass
    print(ENTRY, end="")
