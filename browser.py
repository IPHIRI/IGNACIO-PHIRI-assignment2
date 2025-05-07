import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QTextBrowser, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon
class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon("assets/ignacio.jpg"))  
        self.setWindowTitle("Ignacio's search engine")
        self.setGeometry(100, 100, 600, 400)
        
        
        #background image referenced from chat gpt
        main_widget = QWidget(self)
        
        main_widget.setStyleSheet("""
            QWidget {
                 border-image: url(background.jpg);
            }
        """)
        

        self.setCentralWidget(main_widget)
        
        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        # make sure the server is running on port 8000, localhost for this to work
        self.local_server_address = "http://localhost:8000"

        
        self.search_input_box = QLineEdit()
        self.search_input_box.setPlaceholderText("Search...")
        self.search_input_box.returnPressed.connect(self.perform_search)

        
        self.results_display = QTextBrowser()
        self.results_display.setReadOnly(True)
        self.results_display.setOpenExternalLinks(True) 

        
        layout = QVBoxLayout()
        layout.addWidget(self.search_input_box)
        layout.addWidget(self.results_display)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def perform_search(self):
        
        user_input = self.search_input_box.text().strip().lower()

        
        html_result = "<h2>These are the results to your search</h2><ul>"

        
        if user_input == "index":
            html_result += f'<li><a href="{self.local_server_address}/">Click here to open index page</a></li>'
        elif user_input == "register":
            html_result += f'<li><a href="{self.local_server_address}/register">click here to open register page</a></li>'
        else:
            html_result += "<li>I could'nt find that in my server.</li>"
            google_link = f"https://www.google.com/search?q={user_input}"
            html_result += f'<li><a href="{google_link}">Search on Google</a></li>'

        html_result += "</ul>"

        
        self.results_display.setHtml(html_result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec_())
