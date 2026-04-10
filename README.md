🛡️ FinRecon Gateway: Razorpay & Cashfree Reconciliation
FinRecon Gateway is a specialized Streamlit-based financial tool designed to bridge the gap between payment gateway settlements (Razorpay/Cashfree) and Shopify order exports. It automates the tedious task of matching transaction emails to order numbers and generates ready-to-use accounting journals.

🚀 Features
Dual Gateway Support: Switch seamlessly between Razorpay and Cashfree processing portals.

Smart Header Detection: Automatically identifies relevant columns (Email, Amount, Date) even if the uploaded Excel file has summary rows or metadata at the top.

Automated Journal Entry: Generates formatted .xlsx files with:

Credit/Debit Logic: Properly categorized "Payments" vs "Refunds."

Settlement Dates: Captured directly from the gateway reports for accurate accrual accounting.

Reference ID Matching: Includes Merchant Reference IDs for easy auditing.

Persistence: Results and download buttons remain visible even after interaction, ensuring a smooth workflow.

🛠️ How it Works
The reconciliation process follows a "Fuzzy Match" logic based on customer identifiers:

Data Ingestion: The user uploads a Gateway Settlement Report and a Shopify Order Export.

Cleaning: The tool strips whitespace, normalizes email addresses to lowercase, and filters out non-transactional events.

The Merge: It performs a "Left Join" using the Email Address as the primary key. This allows the tool to pull the Shopify Order Number into the Gateway transaction list.

Journal Generation: * Payments: Debits Cashfree/Razorpay Receivable and Credits the Customer Email.

Refunds: Debits the Customer Email and Credits Cashfree/Razorpay Receivable.

📂 Project Structure
Plaintext
├── main_dashboard.py      # The entry point with Sidebar Navigation
├── app.py                 # Logic for Razorpay x Shopify reconciliation
└── cashfree.py            # Logic for Cashfree x Shopify reconciliation
📖 Usage Instructions
Launch the Dashboard: Run streamlit run main_dashboard.py.

Select Portal: Use the sidebar to choose between Razorpay or Cashfree.

Upload Files:

Settlement Report: The Excel file downloaded from your payment gateway dashboard.

Shopify Export: The "Orders" export (XLSX) from your Shopify admin.

Set Filename: Enter your desired name in the Output Journal File Name field.

Run & Download: Click Run Reconciliation. Once the metrics appear, verify the "Unmatched" count and click Download Journal.

📋 Requirements
To run this tool locally, ensure you have the following Python libraries installed:

Bash
pip install streamlit pandas openpyxl
⚠️ Important Notes
Email Matching: The tool relies on the customer email address matching between the gateway and Shopify. If a customer used a different email at checkout than they did for the payment, the "Order Number" will appear as N/A.

File Format: Ensure both files are in .xlsx format. Standard CSVs should be saved as Excel Workbooks before uploading for the best experience.
