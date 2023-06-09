import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QGridLayout, QWidget, QFileDialog, QTextEdit
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt, QSize 
from pathlib import Path


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Generator")
        self.setGeometry(100, 100, 400, 200)

        # Create a central widget and a grid layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QGridLayout(central_widget)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(20)

        # Create a title label
        title_label = QLabel("Desktop Application", self)
        title_label.setFont(QFont("Arial", 16, QFont.Bold))
        layout.addWidget(title_label, 0, 0, 1, 2)

        # Video Overlay Section
        video_overlay_label = QLabel("Import Video Overlay:", self)
        layout.addWidget(video_overlay_label, 1, 0)

        video_overlay_button = QPushButton("Browse", self)
        video_overlay_button.clicked.connect(self.import_video_overlay)
        layout.addWidget(video_overlay_button, 1, 1)

        # Excel Sheet Section
        excel_sheet_label = QLabel("Import Excel Sheet:", self)
        layout.addWidget(excel_sheet_label, 2, 0)

        excel_sheet_button = QPushButton("Browse", self)
        excel_sheet_button.clicked.connect(self.import_excel_sheet)
        layout.addWidget(excel_sheet_button, 2, 1)

        # User Input Section
        description_label = QLabel("Description:", self)
        layout.addWidget(description_label, 3, 0)

        self.description_entry = QTextEdit(self)  # Use QTextEdit for a multiline input
        self.description_entry.setFixedHeight(100)  # Set fixed height
        layout.addWidget(self.description_entry, 3, 1)

        title_label = QLabel("Title:", self)
        layout.addWidget(title_label, 4, 0)

        self.title_entry = QLineEdit(self)
        layout.addWidget(self.title_entry, 4, 1)

        # Submit Button
        submit_button = QPushButton("Submit", self)
        submit_button.clicked.connect(self.submit)
        layout.addWidget(submit_button, 5, 0, 1, 2)

        # Set the layout for the central widget
        central_widget.setLayout(layout)

    def import_video_overlay(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Video Overlay", "", "Video Files (*.mp4)")
        # Code to handle the imported video overlay

    def import_excel_sheet(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Excel Sheet", "", "Excel Files (*.xlsx)")
        # Code to handle the imported Excel sheet

    def submit(self):
        description = self.description_entry.text()
        title = self.title_entry.text()
        # Code to handle user input for description and title
        # Code to perform other operations, such as video recording, editing, YouTube upload, and spreadsheet logging

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Apply Fusion style

    # Apply additional style options
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor("#F0F0F0"))  # Set background color
    palette.setColor(QPalette.WindowText, QColor("#404040"))  # Set foreground color
    app.setPalette(palette)
    
    app.setStyleSheet(Path('main\styles.qss').read_text())



    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
