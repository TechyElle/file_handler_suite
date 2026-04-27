"""Module for transforming integers into squares and cubes.

Implements Problem P-4: Read integers from a source file and create
two output files: double.txt with squares of even numbers, and
triple.txt with cubes of odd numbers.
"""

from typing import List, Tuple

from file_handler_base import FileHandler

class IntegerTransformer(FileHandler):
    """Transform even and odd integers into squares and cubes.

    Reads integers from the source file, computes the square of each
    even number and the cube of each odd number, then writes the
    results to separate output files.

    Attributes:
        even_squares (List[int]): Squares of even numbers.
        odd_cubes (List[int]): Cubes of odd numbers.
        double_output_path (str): Path to the squares output file.
        triple_output_path (str): Path to the cubes output file.
    """

    def __init__(
        self,
        source_file_path: str,
        output_directory: str = "."
    ) -> None:
        """Initialize the IntegerTransformer.

        Args:
            source_file_path: Path to the file containing integers.
            output_directory: Directory for output files.
        """
        super().__init__(source_file_path, output_directory)
        self.even_squares: List[int] = []
        self.odd_cubes: List[int] = []
        self.double_output_path: str = ""
        self.triple_output_path: str = ""
        
    def _transform_numbers(
        self,
        numbers: List[int]
    ) -> Tuple[List[int], List[int]]:
        """Compute squares for evens and cubes for odds.

        Args:
            numbers: List of integers to transform.

        Returns:
            Tuple of (even_squares, odd_cubes).
        """
        even_squares = [num ** 2 for num in numbers if num % 2 == 0]
        odd_cubes = [num ** 3 for num in numbers if num % 2 != 0]
        return even_squares, odd_cubes
        
    def process(self) -> None:
        """Execute the integer transformation workflow."""
        raw_lines = self.read_all_lines()
        all_numbers = self._parse_integers(raw_lines)

        self.even_squares, self.odd_cubes = self._transform_numbers(
            all_numbers
        )

        self.double_output_path = self.write_lines(
            "double.txt",
            [str(num) for num in self.even_squares]
        )
        self.triple_output_path = self.write_lines(
            "triple.txt",
            [str(num) for num in self.odd_cubes]
        )
