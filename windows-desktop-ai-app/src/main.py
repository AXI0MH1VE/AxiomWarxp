"""

Desktop AI Application - Main Entry Point

Production-grade Windows desktop application with embedded AI

"""

import sys

import os

from pathlib import Path

from PyQt6.QtWidgets import QApplication

from PyQt6.QtCore import Qt, QSettings

from PyQt6.QtGui import QIcon

from ui.main_window import MainWindow

from core.config import AppConfig

# Enable high DPI scaling for modern displays

if hasattr(Qt.ApplicationAttribute, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)

if hasattr(Qt.ApplicationAttribute, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)

class DesktopAIApplication:
    """Main application controller"""
    
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.app.setOrganizationName("AxiomHive")
        self.app.setOrganizationDomain("axiomhive.co")
        self.app.setApplicationName("Desktop AI Assistant")
        self.app.setApplicationVersion("1.0.0")
        
        # Set application icon
        icon_path = self._get_resource_path("resources/icons/app_icon.ico")
        if os.path.exists(icon_path):
            self.app.setWindowIcon(QIcon(icon_path))
        
        # Initialize configuration
        self.config = AppConfig()
        
        # Create main window
        self.main_window = MainWindow(self.config)
        
    def _get_resource_path(self, relative_path):
        """Get absolute path to resource, works for dev and PyInstaller"""
        if hasattr(sys, '_MEIPASS'):
            # Running as compiled executable
            base_path = Path(sys._MEIPASS)
        else:
            # Running in development
            base_path = Path(__file__).parent
        return str(base_path / relative_path)
    
    def run(self):
        """Start the application"""
        self.main_window.show()
        return self.app.exec()

def main():
    """Application entry point"""
    app = DesktopAIApplication()
    sys.exit(app.run())

if __name__ == "__main__":
    main()