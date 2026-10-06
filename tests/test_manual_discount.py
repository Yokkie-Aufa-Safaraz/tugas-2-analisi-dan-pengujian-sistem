from src.engine import get_engine

def test_diskon_manual_dapat_diisi_dalam_persen():
    receipt = get_engine().checkout(1, 20_000, 20_000, discount_percent=15)
    assert (receipt.discount, receipt.total) == (3_000, 17_000)
