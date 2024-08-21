# SPFx File Condenser

SPFx File Condenser is a Python-based GUI tool designed to consolidate important files from a SharePoint Framework (SPFx) project into a single text file. This tool is particularly useful for creating context files for LLM programming projects or for quickly reviewing the key components of an SPFx project. It's particularly useful when starting new chats about a development project.

## Features

- User-friendly GUI built with PyQt5
- Condenses specific files from an SPFx project:
  - JSON files in the root directory (excluding package-lock.json)
  - All important files (.ts, .tsx, .js, .jsx, .json, .scss, .css, .html) in the 'src' folder and its subdirectories
- Outputs a single text file with the contents of all selected files, each preceded by its relative path

## Installation

1. Ensure you have Python 3.6+ installed on your system.
2. Clone this repository:
   ```
   git clone https://github.com/yourusername/spfx-file-condenser.git
   cd spfx-file-condenser
   ```
3. Install the required dependencies:
   ```
   pip install PyQt5
   ```

## Usage

1. Run the script:
   ```
   python spfx_condenser.py
   ```
2. In the GUI:
   - Click "Browse" next to "Project Path" to select your SPFx project directory.
   - Click "Browse" next to "Output File" to choose where to save the condensed file.
   - Click "Condense Project" to start the process.
3. The tool will create a single text file containing the contents of all important files from your SPFx project.

## File Selection Criteria

The tool selects files based on the following criteria:
- All JSON files in the root directory of the project, except for package-lock.json
- All files with the following extensions in the 'src' folder and its subdirectories:
  - .ts, .tsx, .js, .jsx, .json, .scss, .css, .html

## Contributing

Contributions to improve SPFx File Condenser are welcome! Please feel free to submit pull requests or create issues for bugs and feature requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the PyQt5 team for providing the GUI framework.
- Inspired by the need for quick context creation in SPFx projects for LLM programming tasks.

