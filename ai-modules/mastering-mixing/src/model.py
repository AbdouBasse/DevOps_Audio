# model.py
import random

STYLES = ["Afro", "Trap", "House", "Jazz", "Rock"]

def adjust_parameters(style: str):
    """
    Ajuste les paramètres de mastering/mixage selon le style musical.
    """
    if style not in STYLES:
        style = random.choice(STYLES)

    params = {
        "eq": "bright" if style in ["House", "Jazz"] else "warm",
        "compression": "strong" if style == "Trap" else "medium",
        "reverb": "deep" if style == "Afro" else "light"
    }
    return style, params
