from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests
from tkmacosx import Button


# --- шрифты ---
FONT_HEADER = ('Arial', 11)
FONT_CODE = ('Courier', 11)

# криптовалюты и как они называются на сайте CoinGecko
COINS = {
    'BTC': 'bitcoin', 'ETH': 'ethereum', 'BNB': 'binancecoin',
    'USDT': 'tether', 'SOL': 'solana', 'ADA': 'cardano'
}


def get_usd_price(code):
    """сколько долларов стоит 1 единица, без интерфейса"""
    pass


def exchange():
    """расчет курса и показ результата"""
    pass


def update_base_label(event):
    """полное название базовой валюты"""
    pass


def update_base2_label(event):
    """полное название второй базовой валюты"""
    pass


def update_currency_label(event):
    """полное название целевой валюты"""
    pass


currencies = {
    'BNB': 'BNB', 'USDT': 'Tether USDt', 'ETH': 'Ethereum', 'BTC': 'Bitcoin',
    'SOL': 'Solana', 'ADA': 'Cardano',
    'EUR': 'Евро', 'USD': 'Доллар США', 'RUB': 'Российский рубль',
    'JPY': 'Японская йена', 'GBP': 'Фунт стерлингов', 'AUD': 'Австралийский доллар',
    'CAD': 'Канадский доллар', 'CHF': 'Швейцарский франк', 'CNY': 'Китайский юань'
}

root = Tk()
root.title('COINFLOW — Курсы обмена криптовалют')
root.geometry('380x360')

# блок 1: базовая валюта
ttk.Label(root, text='Базовая валюта', font=FONT_HEADER).pack(anchor='w', padx=10, pady=(15, 0))
base_combobox = ttk.Combobox(root, values=list(currencies.keys()), font=FONT_CODE, state='readonly')
base_combobox.pack(pady=3, padx=10, fill='x')
base_combobox.bind('<<ComboboxSelected>>', update_base_label)
base_label = ttk.Label(root, font=FONT_HEADER, foreground='gray')
base_label.pack()

# блок 2: вторая базовая валюта
ttk.Label(root, text='Вторая базовая валюта', font=FONT_HEADER).pack(anchor='w', padx=10, pady=(15, 0))
base2_combobox = ttk.Combobox(root, values=list(currencies.keys()), font=FONT_CODE, state='readonly')
base2_combobox.pack(pady=3, padx=10, fill='x')
base2_combobox.bind('<<ComboboxSelected>>', update_base2_label)
base2_label = ttk.Label(root, font=FONT_HEADER, foreground='gray')
base2_label.pack()

# блок 3: целевая валюта
ttk.Label(root, text='Целевая валюта', font=FONT_HEADER).pack(anchor='w', padx=10, pady=(15, 0))
target_combobox = ttk.Combobox(root, values=list(currencies.keys()), font=FONT_CODE, state='readonly')
target_combobox.pack(pady=3, padx=10, fill='x')
target_combobox.bind('<<ComboboxSelected>>', update_currency_label)
target_label = ttk.Label(root, font=FONT_HEADER, foreground='gray')
target_label.pack()

btn = Button(root,
             text='Получить курс обмена',
             bg='#467ef0', fg='white',
             font=FONT_HEADER,
             command=exchange)
btn.pack(pady=20, padx=10, fill='x')

root.mainloop()
