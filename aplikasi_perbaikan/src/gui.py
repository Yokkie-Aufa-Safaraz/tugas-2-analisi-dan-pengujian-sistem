"""Aplikasi desktop kasir mini menggunakan Tkinter (standard library)."""
import tkinter as tk
from tkinter import ttk

from .main import checkout

BG = "#F3F6F8"
NAVY = "#142B43"
TEAL = "#087E78"
MUTED = "#5D7183"
WHITE = "#FFFFFF"
RED = "#B42318"
GREEN = "#16724A"


def rupiah(value: int) -> str:
    return f"Rp{value:,}".replace(",", ".")


class CashierApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        root.title("Kasir Mini | Aplikasi Kasir")
        root.geometry("920x740")
        root.minsize(820, 700)
        root.configure(bg=BG)

        style = ttk.Style(root)
        style.theme_use("clam")
        style.configure("TEntry", padding=(10, 9), font=("Segoe UI", 12))
        style.configure("TButton", font=("Segoe UI", 11), padding=(14, 10))
        style.configure("Primary.TButton", background=TEAL, foreground=WHITE, borderwidth=0)
        style.map("Primary.TButton", background=[("active", "#066B66")])
        style.configure("Secondary.TButton", background="#E7EDF1", foreground=NAVY, borderwidth=0)
        style.map("Secondary.TButton", background=[("active", "#D8E1E8")])

        page = tk.Frame(root, bg=BG, padx=34, pady=26)
        page.pack(fill="both", expand=True)

        tk.Label(page, text="KASIR MINI", bg=BG, fg=TEAL,
                 font=("Segoe UI", 11, "bold")).pack(anchor="w")
        tk.Label(page, text="Aplikasi Kasir", bg=BG, fg=NAVY,
                 font=("Segoe UI", 28, "bold")).pack(anchor="w", pady=(5, 0))
        tk.Label(page, text="Masukkan barang dan pembayaran untuk menghitung total transaksi.",
                 bg=BG, fg=MUTED, font=("Segoe UI", 11)).pack(anchor="w", pady=(3, 20))

        content = tk.Frame(page, bg=BG)
        content.pack(fill="both", expand=True)
        content.columnconfigure(0, weight=1)
        content.columnconfigure(1, weight=1)

        form = tk.Frame(content, bg=WHITE, padx=23, pady=22,
                        highlightbackground="#D9E2E8", highlightthickness=1)
        form.grid(row=0, column=0, sticky="nsew", padx=(0, 12))
        tk.Label(form, text="Detail transaksi", bg=WHITE, fg=NAVY,
                 font=("Segoe UI", 16, "bold")).pack(anchor="w", pady=(0, 18))

        self.entries: dict[str, ttk.Entry] = {}
        fields = [
            ("Nama barang (opsional)", "item", "Contoh: Buku"),
            ("Jumlah barang", "quantity", "Bilangan bulat, minimal 1"),
            ("Harga satuan (Rp)", "price", "Contoh: 60000"),
            ("Diskon (%)", "discount", "Opsional, 0 sampai 100"),
            ("Uang pembayaran (Rp)", "paid", "Contoh: 120000"),
        ]
        for label, key, hint in fields:
            block = tk.Frame(form, bg=WHITE)
            block.pack(fill="x", pady=(0, 12))
            tk.Label(block, text=label, bg=WHITE, fg=NAVY,
                     font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(0, 5))
            entry = ttk.Entry(block)
            entry.pack(fill="x")
            entry.insert(0, hint if key == "item" else "")
            if key == "item":
                entry.bind("<FocusIn>", lambda _event, widget=entry: self._clear_hint(widget))
                entry.bind("<FocusOut>", lambda _event, widget=entry: self._restore_hint(widget))
            self.entries[key] = entry

        actions = tk.Frame(form, bg=WHITE)
        actions.pack(fill="x", pady=(4, 0))
        ttk.Button(actions, text="Hitung transaksi", style="Primary.TButton",
                   command=self.calculate).pack(side="left", fill="x", expand=True)
        ttk.Button(actions, text="Reset", style="Secondary.TButton",
                   command=self.reset).pack(side="left", padx=(9, 0))
        self.message = tk.Label(form, text="Isi diskon (%) untuk nilai manual, atau kosongkan agar aturan otomatis berlaku.",
                                bg=WHITE, fg=MUTED, wraplength=340, justify="left",
                                font=("Segoe UI", 9))
        self.message.pack(anchor="w", pady=(15, 0))

        receipt = tk.Frame(content, bg=NAVY, padx=25, pady=24)
        receipt.grid(row=0, column=1, sticky="nsew", padx=(12, 0))
        tk.Label(receipt, text="RINGKASAN", bg=NAVY, fg="#A7DCD7",
                 font=("Segoe UI", 10, "bold")).pack(anchor="w")
        self.item_title = tk.Label(receipt, text="Belum ada transaksi", bg=NAVY, fg=WHITE,
                                   font=("Segoe UI", 18, "bold"), wraplength=330, justify="left")
        self.item_title.pack(anchor="w", pady=(7, 23))
        self.amounts: dict[str, tk.Label] = {}
        for key, label in [("subtotal", "Subtotal"), ("discount", "Diskon"),
                           ("total", "Total belanja"), ("paid", "Dibayar"),
                           ("change", "Kembalian")]:
            row = tk.Frame(receipt, bg=NAVY)
            row.pack(fill="x", pady=7)
            tk.Label(row, text=label, bg=NAVY, fg="#CFD9E2",
                     font=("Segoe UI", 11)).pack(side="left")
            value = tk.Label(row, text="—", bg=NAVY, fg=WHITE,
                             font=("Segoe UI", 11, "bold"))
            value.pack(side="right")
            self.amounts[key] = value
            if key == "total":
                tk.Frame(receipt, bg="#496176", height=1).pack(fill="x", pady=(5, 2))
        self.amounts["total"].configure(fg="#D8F36A", font=("Segoe UI", 15, "bold"))
        self.amounts["change"].configure(fg="#A7DCD7", font=("Segoe UI", 15, "bold"))
        tk.Label(receipt, text="Kasir Mini · Software Testing RCA", bg=NAVY, fg="#AAB9C7",
                 font=("Segoe UI", 9)).pack(side="bottom", anchor="w", pady=(20, 0))

        self.entries["quantity"].focus_set()
        root.bind("<Return>", lambda _event: self.calculate())

    def _clear_hint(self, entry: ttk.Entry) -> None:
        if entry.get() == "Contoh: Buku":
            entry.delete(0, "end")

    def _restore_hint(self, entry: ttk.Entry) -> None:
        if not entry.get().strip():
            entry.insert(0, "Contoh: Buku")

    def calculate(self) -> None:
        try:
            quantity_text = self.entries["quantity"].get().strip()
            price_text = self.entries["price"].get().strip()
            paid_text = self.entries["paid"].get().strip()
            if not quantity_text or not price_text or not paid_text:
                raise ValueError("Jumlah, harga satuan, dan pembayaran wajib diisi.")
            quantity, price, paid = int(quantity_text), int(price_text), int(paid_text)
            discount_text = self.entries["discount"].get().strip()
            discount_percent = int(discount_text) if discount_text else None
            receipt = checkout(quantity, price, paid, discount_percent)
        except ValueError as error:
            self.message.configure(text=str(error), fg=RED)
            self.entries["quantity"].focus_set()
            return

        name = self.entries["item"].get().strip()
        if not name or name == "Contoh: Buku":
            name = "Transaksi berhasil"
        else:
            name = f"Transaksi berhasil · {name}"
        self.item_title.configure(text=name)
        for key in self.amounts:
            self.amounts[key].configure(text=rupiah(getattr(receipt, key)))
        self.message.configure(text="Transaksi berhasil dihitung.", fg=GREEN)

    def reset(self) -> None:
        for key, entry in self.entries.items():
            entry.delete(0, "end")
            if key == "item":
                entry.insert(0, "Contoh: Buku")
        for label in self.amounts.values():
            label.configure(text="—")
        self.item_title.configure(text="Belum ada transaksi")
        self.message.configure(text="Isi diskon (%) untuk nilai manual, atau kosongkan agar aturan otomatis berlaku.", fg=MUTED)
        self.entries["quantity"].focus_set()


def run() -> None:
    root = tk.Tk()
    CashierApp(root)
    root.mainloop()

