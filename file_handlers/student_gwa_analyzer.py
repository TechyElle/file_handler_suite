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
        
        def _parse_records(self, lines: List[str]) -> List[StudentRecord]:
        """Parse raw lines into StudentRecord objects.

        Expected format per line: 'Full Name,GWA'

        Args:
            lines: Raw lines from the source file.

        Returns:
            A list of valid StudentRecord objects.
        """
        records = []
        for line in lines:
            parts = line.split(",", maxsplit=1)
            if len(parts) == 2:
                name = parts[0].strip()
                try:
                    gwa = float(parts[1].strip())
                    records.append(StudentRecord(name, gwa))
                except ValueError:
                    print(f"Warning: Invalid GWA in line '{line}'")
            else:
                print(f"Warning: Malformed line '{line}'")
        return records
        
        def _find_top_student(self) -> Optional[StudentRecord]:
        """Find the student with the best (lowest numeric) GWA.

        Returns:
            The StudentRecord with the lowest GWA value, or None if no records.
        """
        if not self.student_records:
            return None
        return min(
            self.student_records,
            key=lambda record: record.gwa
        )
        
        def process(self) -> None:
        """Execute the GWA analysis workflow."""
        raw_lines = self.read_all_lines()
        self.student_records = self._parse_records(raw_lines)
        self.top_student = self._find_top_student()
        
        def display_result(self) -> None:
        """Display the analysis results to the console."""
        self._print_header("STUDENT GWA ANALYSIS RESULTS")
        print(f"Total students processed: {len(self.student_records)}")

        if self.top_student:
            print(f"\nTop Performer:")
            print(f"  Name: {self.top_student.full_name}")
            print(f"  GWA:  {self.top_student.gwa:.2f}")
        else:
            print("\nNo valid student records found.")

        print("\nAll Records:")
        for record in sorted(self.student_records, key=lambda r: r.gwa):
            print(f"  {record.gwa:.2f} - {record.full_name}")
        print("=" * 50 + "\n")
