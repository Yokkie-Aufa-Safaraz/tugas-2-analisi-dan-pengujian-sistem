"""Selector untuk menjalankan tes yang sama pada versi before atau after."""
import os
from . import before_faulty, main

def get_engine():
    mode = os.getenv("RCA_MODE", "after").lower()
    if mode == "before":
        return before_faulty
    if mode != "after":
        raise ValueError("RCA_MODE harus 'before' atau 'after'.")
    return main
