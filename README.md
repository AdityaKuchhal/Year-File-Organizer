# Organize Files by Year

Organize Files by Year is a user-friendly desktop application designed to help you efficiently organize your files into subfolders based on the year specified in their filenames. This application is perfect for managing date-based files such as invoices, receipts, reports, or photos.

---

## Features

### 🌟 Key Functionalities:

- **Year-Based Sorting**: Automatically moves files into subfolders named after the year extracted from their filenames.
- **Regex Date Support**: Supports two date formats for year extraction:
  - `31-DEC-2024` (DD-MMM-YYYY)
  - `24-12-31` (YY-MM-DD)
- **Progress Tracking**: Visual progress bar with percentage updates during the sorting process.
- **History Tracking**: Saves the paths of previously organized folders and allows you to view them.
- **Modern GUI**: Clean and interactive user interface built with Tkinter.
- **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux.
- **Custom Icon**: Displays a professional icon for the application in the taskbar and status bar.

---

## Installation

### Prerequisites

- Python 3.7+
- `pip` (Python package manager)

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/organize-files-by-year.git
cd organize-files-by-year
```

### Step 2: Install Dependencies

Install required libraries:

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

Execute the main script:

```bash
python file_year_organizr.py
```

---

## Usage

1. **Launch the Application**:

   - Open the application by running `file_year_organizr.py`.

2. **Organize Files**:

   - Click the `Browse Folder` button to select the folder containing the files you want to organize.
   - The application will sort files into subfolders based on the year in their filenames.

3. **View History**:

   - Click the `View History` button to see a list of previously organized folders.

4. **Exit**:
   - Click the `Exit` button to close the application.

---

## Build Executable

To create an executable file using **PyInstaller**, follow these steps:

1. Install PyInstaller:

   ```bash
   pip install pyinstaller
   ```

2. Run PyInstaller to package the application:

   ```bash
   pyinstaller --onefile --windowed --name AppName --icon=iconName.ico file_year_organizr.py
   ```

3. The executable will be located in the `dist` folder.

   - **`file_year_organizr.py`**: The Python source file.
   - **`iconName.ico`**: The icon file for the application.
   - **`AppName.spec`**: The PyInstaller spec file.
   - **`dist/`**: Folder containing the generated executable file.
   - **`build/`**: Temporary build files (can be ignored).

---

## Screenshots

![Main Interface](path-to-screenshot-main.png)
_The clean and simple main interface of the application._

![History View](path-to-screenshot-history.png)
_The history window displaying previously organized folders._

---

## Contributing

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes.
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to your fork and create a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Future Enhancements

- Add support for additional date formats.
- Implement drag-and-drop functionality.
- Add an option to clear history.
- Enable sorting by file creation or modification dates.

---

## Acknowledgments

Special thanks to the Python community for the libraries and resources that made this project possible!
