"""Base module for file handling operations.

Provides an abstract base class that defines common file I/O
operations used across all problem-specific handlers.
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Optional
