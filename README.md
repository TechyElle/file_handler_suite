# Activity 5 - File Handling with Python (OOP Edition)

CMPE 103 - Module 2: File Handling in Python implemented with Object-Oriented Programming principles.

## Project Overview

This project implements four programming exercises using:
- **OOP Design**: Classes, inheritance, encapsulation, and abstraction
- **Coding Standard**: Descriptive snake_case for files/variables/methods, PascalCase for classes, PEP-8 compliant
- **Interactive Menu**: Clean console interface to run all exercises
- **Error Handling**: Graceful handling of file and input errors

## Architecture

```
FileHandler (ABC)
├── NumberSeparator      (P-1: Even/Odd separation)
├── StudentGwaAnalyzer   (P-2: Top student by GWA)
├── LifeWriter           (P-3: Interactive text writer)
└── IntegerTransformer   (P-4: Squares and cubes)

FileHandlerApp (Menu System)
└── main.py (Entry Point)
```

## Quick Start

```bash
python main.py
```

Select an option from the menu:
- `[1]` Separate Even & Odd Numbers
- `[2]` Find Top Student by GWA
- `[3]` Interactive Life Writer
- `[4]` Square Evens & Cube Odds
- `[5]` About
- `[0]` Exit

## Building From Scratch

See [BUILD_FROM_SCRATCH.md](BUILD_FROM_SCRATCH.md) for a step-by-step guide that maps each Git commit to the incremental development process. This shows exactly how the project was built from an empty repository to the complete application.

## File Structure

| File | Description |
|------|-------------|
| `file_handler_base.py` | Abstract base class with common I/O operations |
| `number_separator.py` | P-1: Separates integers into even.txt and odd.txt |
| `student_gwa_analyzer.py` | P-2: Finds student with highest GWA |
| `life_writer.py` | P-3: Interactively writes lines to mylife.txt |
| `integer_transformer.py` | P-4: Computes squares (evens) and cubes (odds) |
| `file_handler_app.py` | Interactive menu system |
| `main.py` | Application entry point |
| `numbers.txt` | Sample data for P-1 (20 integers) |
| `students_gwa.txt` | Sample data for P-2 (20 student records) |
| `integers.txt` | Sample data for P-4 (20 integers) |

## Sample Output Files

Running the exercises generates:
- `even.txt` / `odd.txt` — from NumberSeparator
- `mylife.txt` — from LifeWriter
- `double.txt` / `triple.txt` — from IntegerTransformer

## Commit History

This repository was built incrementally with 10+ commits showing the progression from repository setup → data preparation → base class → individual problems → menu integration → documentation.

Each commit represents a logical step in building the project from scratch. See `BUILD_FROM_SCRATCH.md` for the detailed mapping.

