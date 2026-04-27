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
