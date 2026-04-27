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

class StudentGwaAnalyzer(FileHandler):
    """Analyze student GWA records to find the top performer.

    Reads student names and GWA values from a source file,
    identifies the student with the highest GWA, and displays
    the result.

    Attributes:
        student_records (List[StudentRecord]): All parsed records.
        top_student (Optional[StudentRecord]): The highest GWA student.
    """

    def __init__(
        self,
        source_file_path: str,
        output_directory: str = "."
    ) -> None:
        """Initialize the StudentGwaAnalyzer.

        Args:
            source_file_path: Path to the file with student data.
            output_directory: Directory for any output files.
        """
        super().__init__(source_file_path, output_directory)
        self.student_records: List[StudentRecord] = []
        self.top_student: Optional[StudentRecord] = None
