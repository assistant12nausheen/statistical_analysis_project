# 📊 Statistical Plots & Distribution Analysis

> **Internship Project — SyntecxHub**  
> A beginner-friendly data analysis project that explores sales distributions across two regions using Python's core data science libraries.

---

## 🔍 Project Overview

This project performs a complete statistical distribution analysis on sales data from **Region A** and **Region B**. It demonstrates how to visually inspect data, compare groups, detect outliers, and draw meaningful conclusions — all fundamental skills in data science and analytics.

---

## 📌 What This Project Does

| Task | Description |
|------|-------------|
| **Histogram** | Visualises how data is distributed across value ranges |
| **KDE Plot** | Smooth probability curve to compare both regions on one chart |
| **Boxplot** | Shows median, spread (IQR), and highlights outliers as dots |
| **Outlier Detection** | Uses the IQR method to identify extreme data points |
| **Skewness Analysis** | Measures symmetry of each distribution |
| **Interpretation** | Written summary of findings in plain English |

---

## 🗂️ Project Structure

```
statistical-analysis-project/
│
├── statistical_analysis.py      ← Plain Python script version
├── statistical_plots.png        ← All exported charts in one image
├── interpretation.txt           ← Written analysis paragraph
└── README.md                    ← This file
```

---

## 📈 Sample Output

The project generates 5 plots:

- Histogram for Region A (with mean and median lines)
- Histogram for Region B (with mean and median lines)
- KDE comparison curve (both regions overlaid)
- Boxplot comparison (outliers shown as dots)
- Overlaid histogram (Region A vs B side by side)

---

## 🧠 Key Concepts Covered

- **Histogram** — bar chart showing frequency of values in each range (bin)
- **KDE (Kernel Density Estimate)** — smooth continuous curve version of a histogram
- **Boxplot** — shows Q1, median, Q3, and flags outliers beyond 1.5×IQR
- **Skewness** — measures how asymmetric a distribution is (0 = symmetric, positive = right tail)
- **IQR (Interquartile Range)** — Q3 − Q1; used to define the boundary for outlier detection

---

## 📊 Results Summary

| Metric | Region A | Region B |
|--------|----------|----------|
| Mean | 56.9 | 75.8 |
| Median | 51.7 | 74.8 |
| Std Deviation | 28.3 | 25.2 |
| Skewness | 1.92 (right-skewed) | 1.01 (mild) |
| Outliers detected | 7 | 5 |

**Conclusion:** Region B consistently shows higher average sales. Region A is right-skewed, indicating a few very large sales events pulling the mean above the median. Both regions contain outliers worth investigating.

---

## 🛠️ Tech Stack

| Library | Purpose |
|---------|---------|
| `numpy` | Numerical arrays and random data generation |
| `pandas` | Data organisation using DataFrame |
| `matplotlib` | All chart creation and export |
| `scipy` | KDE estimation, skewness calculation |

---

## ▶️ How to Run

Python Script

```bash
pip install numpy pandas matplotlib scipy
python statistical_analysis.py
```

The chart image will be saved as `statistical_plots.png` in the same folder.

---

## 👤 Author

Nausheen Suhana  
Intern @ SyntecxHub  
[github.com/your-username](https://github.com/your-assistant12nausheen)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
