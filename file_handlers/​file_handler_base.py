"""Base module for file handling operations.

Provides an abstract base class that defines common file I/O
operations used across all problem-specific handlers.
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Optional

    
class FileHandler(ABC):
    """Abstract base class for all file handling operations.

    Attributes:
        source_path (Path): Path to the input file.
        output_dir (Path): Directory where output files are written.
    """

    def __init__(
        self,
        source_file_path: str,
        output_directory: Optional[str] = None
    ) -> None:
        """Initialize the FileHandler with source and output paths.

        Args:
            source_file_path: Path to the input file to process.
            output_directory: Optional directory for output files.
                              Defaults to current directory if None.
        """
        self.source_path = Path(source_file_path)
        self.output_dir = Path(output_directory or ".")

    def read_all_lines(self) -> List[str]:
        """Read all lines from the source file.

        Returns:
            A list of strings, each representing a line from the file.

        Raises:
            FileNotFoundError: If the source file does not exist.
            PermissionError: If the source file cannot be read.
        """
        try:
            with self.source_path.open("r", encoding="utf-8") as file:
                return [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            print(f"Error: File '{self.source_path}' not found.")
            raise
        except PermissionError:
            print(f"Error: Permission denied for '{self.source_path}'.")
            raise

    def write_lines(self, file_name: str, lines: List[str]) -> str:
        """Write a list of lines to a file in the output directory.

        Args:
            file_name: Name of the output file.
            lines: List of strings to write.

        Returns:
            The full path to the written file as a string.
        """
        full_path = self.output_dir / file_name
        self.output_dir.mkdir(parents=True, exist_ok=True)
        with full_path.open("w", encoding="utf-8") as file:
            for line in lines:
                file.write(f"{line}\n")
        return str(full_path)
        
    def _parse_integers(self, lines: List[str]) -> List[int]:
        """Convert string lines to integers, skipping invalid entries.

        Args:
            lines: Raw lines from the source file.

        Returns:
            A list of valid integers.
        """
        valid_integers = []
        for line in lines:
            try:
                valid_integers.append(int(line))
            except ValueError:
                print(f"Warning: Skipping non-integer value '{line}'")
        return valid_integers

    def _print_header(self, title: str) -> None:
        """Print a formatted header for the results display.

        Args:
            title: The title to display in the header.
        """
        print("\n" + "=" * 50)
        print(title.upper())
        print("=" * 50)
