"""Module for separating even and odd numbers from a file.

Implements Problem P-1: Read 20 integers from a text file and create
two separate files containing even and odd numbers respectively.
"""

from typing import List, Tuple
from file_handler_base import FileHandler

class NumberSeparator(FileHandler):
    """Separate even and odd integers from a source file.

    Reads integers from the source file, classifies them as even or odd,
    and writes the results to two separate output files.

    Attributes:
        even_numbers (List[int]): Even numbers extracted from source.
        odd_numbers (List[int]): Odd numbers extracted from source.
        even_output_path (str): Path to the even numbers output file.
        odd_output_path (str): Path to the odd numbers output file.
    """

    def __init__(
        self,
        source_file_path: str,
        output_directory: str = "."
    ) -> None:
        """Initialize the NumberSeparator.

        Args:
            source_file_path: Path to the file containing integers.
            output_directory: Directory for output files.
        """
        super().__init__(source_file_path, output_directory)
        self.even_numbers: List[int] = []
        self.odd_numbers: List[int] = []
        self.even_output_path: str = ""
        self.odd_output_path: str = ""
