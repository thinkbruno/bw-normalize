# bw-normalize

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

A lightweight and efficient Python library designed to **normalize and format date and currency values**, making user input consistent, safe, and human‑readable.

---

## ✨ Features

* 🚀 **Input Normalization**: Sanitize and standardize user inputs before persisting them in your database.
* 🧑‍💻 **Human‑Readable Formatting**: Convert raw values into friendly, formatted strings.
* 🌍 **Multi‑Locale Support**: Easily handle different regional formats and currency symbols.
* ⚡ **Lightweight & Fast**: Minimal dependencies and simple API.

---

## 📦 Installation

Install the package via `pip`:

```bash
pip install bw-normalize
```

---

## 🚀 Quick Start

```python
from bw_normalize import format_currency, normalize_date
```

---

## 💱 Currency Formatting

```python
print(format_currency(1250.50, locale="en_US"))
# $1,250.50
```

You can easily adapt the locale to support different regions and currencies.

---

## 📅 Date Normalization

```python
print(normalize_date("12/25/2023"))
# 2023-12-25
```

Supports common date formats and converts them into a standardized ISO format (`YYYY-MM-DD`).

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to open a pull request or start a discussion.

---

## 👥 Authors

Developed with ❤️ to simplify data handling in Python.

<table border="0"> <tr> <td> <a href="https://www.linkedin.com/in/ramosbruno90/" target="_blank"> <img src="https://img.shields.io/static/v1?message=Bruno%20Ramos&logo=linkedin&label=&color=0077B5&logoColor=white&style=for-the-badge" height="35" alt="LinkedIn Bruno Ramos" /> </a> </td> <td> <a href="https://www.linkedin.com/in/wellington-alves-rosendo/" target="_blank"> <img src="https://img.shields.io/static/v1?message=Wellington%20Alves&logo=linkedin&label=&color=0077B5&logoColor=white&style=for-the-badge" height="35" alt="LinkedIn Wellington Alves" /> </a> </td> </tr> </table>

---

## 📄 License

This project is licensed under the **MIT License**.

---

⭐ If this project helped you, consider giving it a star!
