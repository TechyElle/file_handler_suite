"""Main entry point for the File Handler Application.

Imports the FileHandlerApp and starts the interactive menu system.
"""

from file_handler_app import FileHandlerApp

def main() -> None:
    """Application entry point."""
    app = FileHandlerApp()
    app.run()

if __name__ == "__main__":
    main()
