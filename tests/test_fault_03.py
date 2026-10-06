from src.engine import get_engine

def test_kembalian_memperhitungkan_potongan_diskon():
    receipt = get_engine().checkout(2, 60_000, 120_000, discount_percent=10)
    assert receipt.change == 12_000
