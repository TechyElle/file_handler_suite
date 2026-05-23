# Activity 5 - File Handling with Python (OOP Edition)

**CMPE 103 - Module 2: File Handling in Python** implemented using **Object-Oriented Programming (OOP)**.

---

## What this project does
This repository provides an interactive, menu-driven Python application that demonstrates file handling concepts using an OOP design.

It includes **four activities (P-1 to P-4)**, each implemented as a dedicated class built on a shared abstract base.

---

## Key Concepts Used
- **OOP Design**: classes, inheritance, encapsulation, abstraction
- **Clean console UI**: a menu to run each activity
- **Robust error handling**: handles common file/input failures gracefully
- **Consistent naming & style**: snake_case for functions/variables, PascalCase for classes, PEP-8 friendly formatting

---

## Architecture (High-level)
```text
FileHandler (ABC)
├── NumberSeparator      (P-1: Even/Odd separation)
├── StudentGwaAnalyzer   (P-2: Top student by GWA)
├── LifeWriter           (P-3: Interactive text writer)
└── IntegerTransformer   (P-4: Squares and cubes)

FileHandlerApp (Menu System)
└── main.py (Entry Point)
```

---

## Quick Start
Run the application from the project root:

```bash
python main.py
```

Then choose an option from the menu:
- `[1]` Separate Even & Odd Numbers (P-1)
- `[2]` Find Top Student by GWA (P-2)
- `[3]` Interactive Life Writer (P-3)
- `[4]` Square Evens & Cube Odds (P-4)
- `[5]` About
- `[0]` Exit

---

## Activities Details

### P-1 — Number Separator
**Input:** `numbers.txt`

**Output:**
- `even.txt` (even numbers)
- `odd.txt` (odd numbers)


---

### P-2 — Student GWA Analyzer
**Input:** `students_gwa.txt`

**Output:** The program displays the student with the **highest GWA**.

---

### P-3 — Life Writer
**Input:** Interactive user text (entered via the console)

**Output:**
- `mylife.txt`

The program repeatedly prompts you for lines until you stop, then writes all collected lines to `mylife.txt`.

---

### P-4 — Integer Transformer
**Input:** `integers.txt`

**Outputs:**
- `double.txt` (squares of even numbers)
- `triple.txt` (cubes of odd numbers)


---

## File Structure
| Path | Description |
|------|-------------|
| `main.py` | Application entry point |
| `file_handler_app.py` | Menu system that runs activities |
| `file_handlers/file_handler_base.py` | Abstract base class with shared I/O helpers |
| `file_handlers/number_separator.py` | Implements P-1 |
| `file_handlers/student_gwa_analyzer.py` | Implements P-2 |
| `file_handlers/life_writer.py` | Implements P-3 |
| `file_handlers/integer_transformer.py` | Implements P-4 |
| `sample_data/` | Provided sample input files |

> Note: Output files are written to the project’s working directory by default (e.g., `even.txt`, `odd.txt`, `mylife.txt`, `double.txt`, `triple.txt`).

---

## Sample Data
The repository includes sample inputs under:
- `sample_data/integers.txt`
- `sample_data/numbers.txt`
- `sample_data/students_gwa.txt`

---

## Outputs Summary
Running the exercises generates:
- `even.txt` / `odd.txt` (P-1)
- `mylife.txt` (P-3)
- `double.txt` / `triple.txt` (P-4)

---

## Commit History
This repository was built incrementally with 40+ commits, progressing from setup → data preparation → base class → individual problems → menu integration → documentation.
