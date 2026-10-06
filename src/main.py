"""Logika bisnis kasir mini dan entry point aplikasi desktop."""
from dataclasses import dataclass

DISCOUNT_THRESHOLD = 100_000
DISCOUNT_RATE = 0.10

@dataclass(frozen=True)
class Receipt:
    subtotal: int
    discount: int
    total: int
    paid: int
    change: int

def checkout(quantity: int, unit_price: int, paid: int, discount_percent: int | None = None) -> Receipt:
    if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
        raise ValueError("Kuantitas harus bilangan bulat lebih dari nol.")
    if not isinstance(unit_price, int) or isinstance(unit_price, bool) or unit_price < 0:
        raise ValueError("Harga satuan tidak boleh negatif.")
    subtotal = quantity * unit_price
    if discount_percent is not None and (
        not isinstance(discount_percent, int)
        or isinstance(discount_percent, bool)
        or not 0 <= discount_percent <= 100
    ):
        raise ValueError("Diskon harus berupa bilangan bulat dari 0 sampai 100 persen.")
    if discount_percent is None:
        discount = int(subtotal * DISCOUNT_RATE) if subtotal > DISCOUNT_THRESHOLD else 0
    else:
        discount = int(subtotal * discount_percent / 100)
    total = subtotal - discount
    if paid < total:
        raise ValueError("Pembayaran kurang dari total transaksi.")
    change = paid - total
    return Receipt(subtotal, discount, total, paid, change)

def main() -> None:
    from .gui import run
    run()

if __name__ == "__main__":
    main()

