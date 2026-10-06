import pytest
from src.engine import get_engine

def test_transaksi_normal_tanpa_diskon():
    receipt = get_engine().checkout(2, 20_000, 50_000)
    assert (receipt.subtotal, receipt.discount, receipt.total, receipt.change) == (40_000, 0, 40_000, 10_000)

def test_batas_subtotal_tepat_seratus_ribu_tidak_mendapat_diskon():
    receipt = get_engine().checkout(2, 50_000, 100_000)
    assert (receipt.discount, receipt.total) == (0, 100_000)

def test_pembayaran_kurang_ditolak():
    with pytest.raises(ValueError, match="Pembayaran kurang"):
        get_engine().checkout(1, 50_000, 49_999)
