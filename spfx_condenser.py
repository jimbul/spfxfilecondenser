import sys
import os

try:
    from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QFileDialog, QMessageBox
except ImportError:
    print("PyQt5 is not installed. Please install it using: pip install PyQt5")
    sys.exit(1)

def is_important_file(file_name):
    important_extensions = ['.ts', '.tsx', '.js', '.jsx', '.json', '.scss', '.css', '.html']
    return any(file_name.endswith(ext) for ext in important_extensions)

def condense_spfx_project(project_path, output_file):
    with open(output_file, 'w', encoding='utf-8') as out_file:
        # Process JSON files in root
        for file in os.listdir(project_path):
            if file.endswith('.json') and file != 'package-lock.json':
                file_path = os.path.join(project_path, file)
                out_file.write(f"--- File: {file} ---\n\n")
                try:
                    with open(file_path, 'r', encoding='utf-8') as in_file:
                        out_file.write(in_file.read())
                except Exception as e:
                    out_file.write(f"Error reading file: {str(e)}\n")
                out_file.write("\n\n")

        # Process files in src folder
        src_folder = os.path.join(project_path, 'src')
        if os.path.exists(src_folder):
            for root, dirs, files in os.walk(src_folder):
                for file in files:
                    if is_important_file(file):
                        file_path = os.path.join(root, file)
                        relative_path = os.path.relpath(file_path, project_path)
                        out_file.write(f"--- File: {relative_path} ---\n\n")
                        try:
                            with open(file_path, 'r', encoding='utf-8') as in_file:
                                out_file.write(in_file.read())
                        except Exception as e:
                            out_file.write(f"Error reading file: {str(e)}\n")
                        out_file.write("\n\n")

class SPFxCondenserGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('SPFx Project File Condenser')
        self.setGeometry(300, 300, 400, 150)

        layout = QVBoxLayout()

        # Project Path
        project_layout = QHBoxLayout()
        self.project_path = QLineEdit()
        project_layout.addWidget(QLabel('Project Path:'))
        project_layout.addWidget(self.project_path)
        project_browse = QPushButton('Browse')
        project_browse.clicked.connect(self.browse_project)
        project_layout.addWidget(project_browse)
        layout.addLayout(project_layout)

        # Output File
        output_layout = QHBoxLayout()
        self.output_file = QLineEdit()
        output_layout.addWidget(QLabel('Output File:'))
        output_layout.addWidget(self.output_file)
        output_browse = QPushButton('Browse')
        output_browse.clicked.connect(self.browse_output)
        output_layout.addWidget(output_browse)
        layout.addLayout(output_layout)

        # Condense Button
        condense_button = QPushButton('Condense Project')
        condense_button.clicked.connect(self.condense_project)
        layout.addWidget(condense_button)

        self.setLayout(layout)

    def browse_project(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Project Directory")
        if folder:
            self.project_path.setText(folder)

    def browse_output(self):
        file, _ = QFileDialog.getSaveFileName(self, "Save Output File", "", "Text Files (*.txt);;All Files (*)")
        if file:
            self.output_file.setText(file)

    def condense_project(self):
        project_path = self.project_path.text()
        output_file = self.output_file.text()

        if not project_path or not output_file:
            QMessageBox.warning(self, "Error", "Please provide both project path and output file name.")
            return

        try:
            condense_spfx_project(project_path, output_file)
            QMessageBox.information(self, "Success", f"Condensed project files saved to {output_file}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

def main():
    app = QApplication(sys.argv)
    ex = SPFxCondenserGUI()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()