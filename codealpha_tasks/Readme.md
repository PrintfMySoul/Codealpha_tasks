# Stock Portfolio Tracker

A simple Python application that allows users to track their stock investments based on predefined stock prices. The program calculates individual stock holdings, sums the total portfolio value, and saves the final summary report to a text file.

## Features

- **Interactive Console Input**: Prompts users for stock tickers and share quantities.
- **Predefined Price List**: Uses a Python dictionary to retrieve stock prices.
- **Case-Insensitive Input**: Automatically converts stock ticker inputs to uppercase.
- **Total Calculation**: Calculates individual investment values and maintains a running total.
- **File Output**: Automatically exports the portfolio breakdown and grand total to `portfolio.txt`.

## Predefined Stocks & Prices

| Ticker | Price (USD) |
| :--- | :--- |
| **AAPL** | $180 |
| **TSLA** | $250 |
| **MSFT** | $420 |
| **GOOG** | $160 |

---

## How to Run

### Prerequisites
- Python 3.x installed on your machine.

### Execution

1. Clone or download this repository.
2. Open your terminal or command prompt.
3. Navigate to the project directory.
4. Run the Python script:

```bash
python main.py
```

---

## Usage Example

```text
Enter stock name: aapl
Enter quantity: 5
AAPL: 5 shares * $180 = $900 

Do you want to continue? (yes/no): yes
Enter stock name: tsla
Enter quantity: 2
TSLA: 2 shares * $250 = $500 

Do you want to continue? (yes/no): no

Total investment: $1400
```

---

## Output File (`portfolio.txt`)

After completing the inputs, a `portfolio.txt` file is generated in the root directory:

```
Total Investment: $1400
```

---

## Concepts Used

- **Python Dictionaries**: Key-value pairs for quick stock price lookup.
- **Control Flow**: `while` loops for continuous user entry and `if-else` condition checking.
- **Error Handling**: Inputs are normalized using `.upper()` and `.strip().lower()`.
- **File Handling**: File operations using `open()` with `w` mode to record portfolio reports.