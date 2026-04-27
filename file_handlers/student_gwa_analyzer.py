"""Module for analyzing student GWA records.

Implements Problem P-2: Read a file containing student names and their
GWA, then determine and display the student with the highest GWA.
"""

from typing import List, Tuple, Optional

from file_handler_base import FileHandler

class StudentRecord:
    """Represents a single student's academic record.

    Attributes:
        full_name (str): The student's full name.
        gwa (float): The student's General Weighted Average.
    """

    def __init__(self, full_name: str, gwa: float) -> None:
        """Initialize a StudentRecord.

        Args:
            full_name: The student's full name.
            gwa: The General Weighted Average.
        """
        self.full_name = full_name
        self.gwa = gwa

    def __repr__(self) -> str:
        """Return a string representation of the record."""
        return f"StudentRecord(name='{self.full_name}', gwa={self.gwa})"
