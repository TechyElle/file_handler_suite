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
        self.source_path = Path(source_file_path)
        self.output_dir = Path(output_directory or ".")
