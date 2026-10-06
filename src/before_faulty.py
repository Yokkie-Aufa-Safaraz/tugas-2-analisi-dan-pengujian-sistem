"""Snapshot implementasi awal dengan tiga fault untuk demonstrasi RCA."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Receipt:
    subtotal: int
    discount: int
    total: int
    paid: int
    change: int

def checkout(quantity: int, unit_price: int, paid: int, discount_percent: int | None = None) -> Receipt:
    # F-02: quantity 0 atau negatif tidak diperiksa.
    subtotal = quantity * unit_price
    # F-01: rate otomatis 1% meski aturan menetapkan 10%.
    if discount_percent is None:
        discount = int(subtotal * 0.01) if subtotal > 100_000 else 0
    else:
        if not isinstance(discount_percent, int) or isinstance(discount_percent, bool) or not 0 <= discount_percent <= 100:
            raise ValueError("Diskon harus berupa bilangan bulat dari 0 sampai 100 persen.")
        discount = int(subtotal * discount_percent / 100)
    total = subtotal - discount
    if paid < total:
        raise ValueError("Pembayaran kurang dari total transaksi.")
    # F-03: menggunakan subtotal, bukan total sesudah diskon.
    change = paid - subtotal
    return Receipt(subtotal, discount, total, paid, change)
