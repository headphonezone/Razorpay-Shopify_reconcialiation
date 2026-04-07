# 📊 Excel Reconciliation Tool

A web-based tool built with **Streamlit** that automates the reconciliation between **Shopify** and **Razorpay** transaction data and generates formatted **Journal Entries** and **Lookup Reports** as Excel files.

---

## 🚀 Live App

👉 [Click here to open the app](https://your-app-link.streamlit.app)
> *(Replace this link after deploying on Streamlit Cloud)*

---

## 📋 Features

- Upload Shopify and Razorpay Excel files
- Automatically matches transactions using Payment ID
- Generates a **Lookup Sheet** with:
  - Customer Name, Order No, Payment ID
  - Amount, Fee, Tax, Gross Total
  - DR/CR classification
  - Amount verification (Matched / Mismatch)
- Generates a **Journal Entry Sheet** with:
  - Credit and Debit accounts
  - Order date, narration, gross total
  - CR rows (green) and DR rows (red) color-coded
- Supports **manual edits** via a lookup file
- Download both output files directly from the app

---

## 🗂️ Project Structure

```
reconciliation-tool/
│
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## ⚙️ Requirements

```
streamlit
pandas
openpyxl
```

---

## 🖥️ How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/reconciliation-tool.git
   cd reconciliation-tool
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   streamlit run app.py
   ```

4. Open `http://localhost:8501` in your browser

---

## 📤 How to Use

1. Upload your **Shopify Excel** file
2. Upload your **Razorpay Excel** file
3. Select the **Journal Entry Date**
4. Click process — two files will be ready to download:
   - `lookup.xlsx` — Reconciliation lookup report
   - `journal_final.xlsx` — Journal entry sheet

---

## 📌 Input File Requirements

### Shopify Excel
Must contain these columns:
- `Payment id`
- `Email`
- `Order Number`

### Razorpay Excel
Must contain these columns:
- `order_receipt`
- `payment_notes`
- `amount`
- `fee (exclusive tax)`
- `tax`
- `credit`
- `debit`
- `entity_created_at`

---

## 🛠️ Built With

- [Streamlit](https://streamlit.io/) — Web UI framework
- [Pandas](https://pandas.pydata.org/) — Data processing
- [OpenPyXL](https://openpyxl.readthedocs.io/) — Excel file generation

---

## 👤 Author

**Vijay**
> For any issues or suggestions, feel free to raise an Issue in this repository.
