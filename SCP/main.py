import atexit
import os
import sys

import requests
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow
from PyQt5.QtGui import QPixmap
import mysql.connector


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # connecting to my sql down
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Neptunia",
            database="scp"
        )
        print("Connected to database")
        self.setupUi()

        self.description_timer = QTimer(self)
        self.class_timer = QTimer(self)

    # Register the connection close function with atexit
        atexit.register(self.close_connection)

    def close_connection(self):
        if self.conn.is_connected():
            self.conn.close()
            print("Database connection closed")

    def typewriter_effect(self, text, label, delay=20):
        self.current_text = ""
        self.full_text = text
        self.current_label = label
        self.index = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_text)
        self.timer.start(delay)

    def update_text(self):
        if self.index < len(self.full_text):
            self.current_text += self.full_text[self.index]
            self.current_label.setText(self.current_text)
            self.index += 1
        else:
            self.timer.stop()

    def update_ui(self, scp_data):
        if scp_data:
            self.ui.Number.setText(str(scp_data[0]))
            self.ui.Class.setText(str(scp_data[1]))
            self.ui.ClearnaceNo.setText(str(scp_data[2]))
            self.typewriter_effect(scp_data[3], self.ui.Detail)

            # Load image from URL
            image_url = scp_data[4]
            if image_url:
                image_path = os.path.join("Image", f"{scp_data[0]}.jpg")  # Save image with SCP number as filename
                try:
                    # Download image from URL
                    response = requests.get(image_url)
                    with open(image_path, "wb") as f:
                        f.write(response.content)
                    pixmap = QPixmap(image_path)
                    self.ui.Image.setPixmap(pixmap)
                except Exception as e:
                    print(f"Failed to download and save image: {e}")
                    pixmap = QPixmap("Image/Default.gif")
                    self.ui.Image.setPixmap(pixmap)
            else:
                pixmap = QPixmap("Image/Default.gif")
                self.ui.Image.setPixmap(pixmap)

        else:
            print("SCP not found in database")

    def get_scp_info(self, scp_number):
        cursor = self.conn.cursor()
        print(f"Searching for SCP: {scp_number}")
        cursor.execute("SELECT number, class, clearance_level, description, image_url FROM scp_data WHERE number=%s",
                       (scp_number,))

        data = cursor.fetchone()
        return data

    def SearchSCP(self):
        search_text = self.ui.Search.text()
        try:
            # Convert search text to integer (assuming SCP number)
            scp_number = int(search_text)
            scp_data = self.get_scp_info(scp_number)
            self.update_ui(scp_data)
        except ValueError:
            print("Invalid search input. Please enter an SCP number.")

    def setupUi(self):
        # Load default SCP (SCP-001)
        scp_data = self.get_scp_info("1")
        self.update_ui(scp_data)

        pixmap = QPixmap("Image/Default.gif")  # Replace with default image
        self.ui.Image.setPixmap(pixmap)

        # button->function connection
        self.ui.Searchbutton.clicked.connect(self.SearchSCP)
        self.ui.Search.returnPressed.connect(self.SearchSCP)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
