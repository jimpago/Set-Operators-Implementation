# Set Operators – Assignment 1 (ΜΥΕ041 / ΠΛΕ081)

This repository contains Python implementations of set operators over relational data stored in `.tsv` format. Developed as part of the _Διαχείριση Σύνθετων Δεδομένων_ course at the University of Ioannina.

## 👨‍💻 Author

**Dimitrios Pagonis**

## 📁 Repository Structure

Assignment_1/
│
├── ask1.1.py         # Merge Join
├── ask1.2.py         # Union
├── ask1.3.py         # Intersection
├── ask1.4.py         # Set Difference
├── ask1.5.py         # Group By and Aggregation (Sum)
│
├── Report.pdf        # Implementation explanation
├── Assignment1.pdf   # Official assignment description
└── README.md         # This file
```

## ⚙️ How to Run

All scripts are run via the terminal using Python 3. Each one expects input file paths and an output file path as arguments.

```bash
python3 ask1.1.py R_sorted.tsv S_sorted.tsv RjoinS.tsv
python3 ask1.2.py R_sorted.tsv S_sorted.tsv RunionS.tsv
python3 ask1.3.py R_sorted.tsv S_sorted.tsv RintersectionS.tsv
python3 ask1.4.py R_sorted.tsv S_sorted.tsv RdifferenceS.tsv
python3 ask1.5.py R.tsv Rgroupby.tsv
```

> ⚠️ **Important:** All input files must be placed in the same directory, or their full paths must be specified when running the scripts.

## 📌 Input Data

The input files `R.tsv`, `R_sorted.tsv`, `S.tsv`, and `S_sorted.tsv` are provided via the course platform (eCourse). They are **not included** in this repository to comply with submission guidelines:

> _“Μην υποβάλετε αρχεία δεδομένων.”_ – Assignment1.pdf

Please make sure to place the correct input files in the working directory before execution.

## 🛠️ Requirements

- Python 3.x
- No external libraries are used (e.g., pandas not allowed as per assignment rules)

## 🧠 Summary of Each Part

### 1. Merge Join (`ask1.1.py`)

- Performs merge join on the first field of sorted R and S files.
- Uses a buffer for matching entries from S.
- Outputs joined results with both values from R and S.

### 2. Union (`ask1.2.py`)

- Performs a union of R and S.
- Ensures no duplicates in the result, sorted lexicographically.

### 3. Intersection (`ask1.3.py`)

- Outputs only the tuples that are present in both R and S.
- Avoids duplicates.

### 4. Difference (`ask1.4.py`)

- Computes R - S by outputting elements present in R but not in S.

### 5. Group By & Aggregation (`ask1.5.py`)

- Groups `R.tsv` by the first field and sums values in the second.
- Uses in-memory merge sort and grouping.

## 📄 Notes

- Each script strictly follows single-pass and no-buffer (where required) constraints.
- The join script (`ask1.1.py`) prints the maximum buffer size used.
- Scripts were tested with the provided `.tsv` files on the eCourse platform.

---
