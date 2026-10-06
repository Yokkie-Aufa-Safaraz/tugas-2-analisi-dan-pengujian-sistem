import pytest
from src.engine import get_engine

@pytest.mark.parametrize("quantity", [0, -1])
def test_kuantitas_nol_dan_negatif_ditolak(quantity):
    with pytest.raises(ValueError, match="Kuantitas"):
        get_engine().checkout(quantity, 50_000, 100_000)
