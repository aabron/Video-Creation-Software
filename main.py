from video_recording.video_recording import record_video
from video_editing.video_editing import overlay_videos, overlay_transparent
from data_processing.google_sheets_processing import read_links_from_google_sheets, add_youtube_link_back
from automated_browsing.auto_browse import automate_browsing
from youtube_upload.youtube_upload import upload_to_youtube, authenticate_youtube
from threading import Thread
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QComboBox, QTextEdit, QVBoxLayout, QWidget, QHBoxLayout,QGroupBox
from PyQt5.QtGui import QIcon

class MyMainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Video Creation')
        self.setGeometry(400, 400, 800, 600)
        
        app_icon = QIcon("logo.png")
        self.setWindowIcon(app_icon)

        self.record_duration_input = QLineEdit(self)
        self.record_duration_input.setPlaceholderText("Enter Record Duration in Seconds")
        self.google_sheets_id = QLineEdit(self)
        self.google_sheets_id.setPlaceholderText("Enter Google Sheet ID")
        self.sheet_name = QLineEdit(self)
        self.sheet_name.setPlaceholderText("Enter Individual Sheet Name")
        self.sheet_column_number_input = QLineEdit(self)
        self.sheet_column_number_input.setPlaceholderText("Enter Column number for Youtube Links")
        self.youtube_title = QLineEdit(self)
        self.starting_row = QLineEdit(self)
        self.starting_row.setPlaceholderText("Enter Starting Row")
        self.youtube_title = QLineEdit(self)
        self.youtube_title.setPlaceholderText("Youtube Title")
        self.youtube_description = QTextEdit(self)
        self.youtube_description.setPlaceholderText("Enter Video Description")
        self.choice_box_label = QLabel('Selected Item: ',self)
        self.scroll_pattern = QComboBox(self)
        self.scroll_pattern.addItem("Scroll Up and Down")
        self.scroll_pattern.addItem("Scroll halfway down wait, click on post, wait, go back, scroll up")
        self.scroll_pattern.addItem("Scroll down wait, scroll up halfway, click post, wait, go back scroll up")
        self.scroll_pattern.currentIndexChanged.connect(self.on_item_selected)
        self.start_button = QPushButton(self)
        self.start_button.clicked.connect(self.start_loop)
        self.start_button.setGeometry(100,100,200,100)
        self.start_button.setText("Start Processing")
        
        main_layout = QVBoxLayout()
        sheets_group = QGroupBox("Google Sheets")
        sheets_layout = QVBoxLayout()
        sheets_layout.addWidget(QLabel("Google Sheet ID:"))
        sheets_layout.addWidget(self.google_sheets_id)
        sheets_layout.addWidget(QLabel("Individual Sheet Name:"))
        sheets_layout.addWidget(self.sheet_name)
        sheets_layout.addWidget(QLabel("Starting Row:"))
        sheets_layout.addWidget(self.starting_row)
        sheets_layout.addWidget(QLabel("Column Number:"))
        sheets_layout.addWidget(self.sheet_column_number_input)
        sheets_group.setLayout(sheets_layout)
        
        youtube_group = QGroupBox("YouTube Video")
        youtube_layout = QVBoxLayout()
        youtube_layout.addWidget(QLabel("YouTube Title:"))
        youtube_layout.addWidget(self.youtube_title)
        youtube_layout.addWidget(QLabel("Video Description:"))
        youtube_layout.addWidget(self.youtube_description)
        youtube_group.setLayout(youtube_layout)
        
        main_layout.addWidget(QLabel("Record Duration (Seconds):"))
        main_layout.addWidget(self.record_duration_input)
        main_layout.addWidget(youtube_group)
        main_layout.addWidget(sheets_group)
        main_layout.addWidget(QLabel("Scroll Action:"))
        main_layout.addWidget(self.scroll_pattern)
        main_layout.addWidget(self.choice_box_label)
        main_layout.addWidget(self.start_button)
        
        widget = QWidget(self)
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
        
        with open('styles.css', 'r') as f:
            style = f.read()
            self.setStyleSheet(style)
        
    def on_item_selected(self):
        selected_item = self.scroll_pattern.currentText()
        self.choice_box_label.setText("Selected Item: " + selected_item)
        return selected_item
        
    def start_loop(self):
        
        sheet_name = self.sheet_name.text() 
        credentials_file = "credentials.json"  
        sheet_key = self.google_sheets_id.text() 
        links = read_links_from_google_sheets(sheet_name, credentials_file, sheet_key)
        title = self.youtube_title.text()
        description = self.youtube_description.toPlainText()
        i = int(self.starting_row.text())
        
        for link in links:
            video_file = 'output.mp4'
            duration = int(self.record_duration_input.text()) # in seconds

            browsing_thread = Thread(target=automate_browsing, args=(link, duration, self.on_item_selected()))
            browsing_thread.start()

            record_video_thread = Thread(target=record_video, args=(video_file, duration))
            record_video_thread.start()

            browsing_thread.join()
            record_video_thread.join()

            overlay_file = "overlay_video.mp4"
            edited_file = "edited_video.mp4"
            overlay_transparent(video_file, overlay_file, edited_file)
        
            client_secret = 'client_secret.json'
            youtube = authenticate_youtube(client_secret)
            video_url = upload_to_youtube(edited_file, youtube, title, description)
            print(f"Video uploaded successfully! Video ID: {video_url}")
            add_youtube_link_back(sheet_name, credentials_file, sheet_key, video_url, i, int(self.sheet_column_number_input.text()))
            i += 1
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    app_icon = QIcon('logo.png')
    app.setWindowIcon(app_icon)
    
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())

