import pytest
from src.engine import get_engine

def test_diskon_sepuluh_persen_dihitung_dengan_benar():
    receipt = get_engine().checkout(2, 60_000, 120_000)
    assert receipt.discount == 12_000
