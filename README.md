# HybExe: Hybrid Desktop App Framework For Python

Welcome to HybExe, a powerful framework for creating cross-platform hybrid desktop apps in Python. Built over pywebview, HybExe provides a seamless integration of web technologies with native desktop components. Let's dive into the details of how to use it.

<div align="center">
  <a href="https://github.com/tejasnayak25/hybexe">
    <img src="https://img.shields.io/github/stars/tejasnayak25/hybexe?style=social" alt="GitHub stars" width="100">
  </a>
  <a href="https://github.com/tejasnayak25/hybexe/fork">
    <img src="https://img.shields.io/github/forks/tejasnayak25/hybexe?style=social" alt="GitHub forks" width="100">
  </a>
</div>

## Prerequisites

Before you start using HybExe, make sure you have the following prerequisites installed on your system:

- [Python](https://www.python.org/downloads/): Make sure you have Python 3.x installed on your system. You can check by running `python --version` in your terminal or command prompt.

## Setting Up the Environment

To get started with HybExe, you need to set up a virtual environment and install the required packages within it. Follow these steps:

```bash
# Clone the GitHub repository
git clone https://github.com/tejasnayak25/hybexe.git

# Change into the project directory
cd hybexe

# Create a virtual environment (Windows)
python -m venv venv

# Activate the virtual environment (Windows)
venv\Scripts\activate

# Create a virtual environment (macOS & Linux)
python3 -m venv venv

# Activate the virtual environment (macOS & Linux)
source venv/bin/activate

# Install the required packages
pip install -r requirements.txt
```

## Required Packages
- [pywebview](https://pywebview.flowrl.com/): A lightweight cross-platform library to create a web-based GUI using native WebView components.

- [pyinstaller](http://www.pyinstaller.org/): For building standalone executables of your hybrid desktop app.

- [plyer](https://plyer.readthedocs.io/): A library for accessing platform-specific features such as notifications.


## Example

Below is a full example of how to use HybExe to create a hybrid desktop app, handle events, and display notifications:

```python
from modules.browser import createWindow
from modules.back import back
from modules.notification import notify

# Event handler function
def func(data):
    back.send("Hi", "Hello from back!")

# Register the event handler
back.on(event="Bye", callback=func)

# Create a browser window
window = createWindow(title="Hello World", url="./src/index.html", resizable=True, draggable=True, text_select=True)

# Notification function (commented out for demonstration)
# notify("Hello There", "Cool", "", 10)

# Start function for the window
def start():
    back.send("Bye", "Cool")

# Start the window with the start function
window.start(function=start, debug=False)
```

## Building Standalone Executable

To create a standalone executable for your hybrid desktop app, you need to make sure to include the `src` and `image` folders in the `datas` array of the `main.spec` file. Open the `main.spec` file and modify the `datas` array to include the necessary folders:

```python
# main.spec

# ... (Other configurations)

a = Analysis(['main.py'],
             pathex=['path/to/your/app'],
             binaries=[],
             datas=[
                 ('path/to/your/app/src', 'src'),
                 ('path/to/your/app/image', 'image')
             ],
             # ... (Other configurations)
            )

# ... (Other configurations)

```

After updating the `main.spec` file, you can run the following command in the terminal or command prompt to build the standalone executable:

```bash
pyinstaller main.spec --clean
```

The `--clean` option will remove any previously generated build files before building.

After the build process completes, you will find the standalone executable in the `dist` directory. This executable can be distributed and run on other systems without the need for Python or any dependencies.

## Creating an Installer

To create an installer for the generated executable using NSIS (Nullsoft Scriptable Install System), follow these steps:

### Prerequisites

Before you can create the installer, make sure you have NSIS installed on your system. You can download NSIS from their official website: [NSIS Website](https://nsis.sourceforge.io/Download).

### Building the Installer

Once you have NSIS installed, you can use it to create an installer for your hybrid desktop app. Here's how you can do it:

1. Generate the standalone executable: Follow the steps mentioned earlier to generate the standalone executable using `pyinstaller`.

2. Create an NSIS script: Create a new text file with the extension `.nsi` (e.g., `installer_script.nsi`) and include the following content:

```nsis
; installer_script.nsi

; Set the name and output directory for the installer
Outfile "YourAwesomeAppInstaller.exe"

; Default section
Section

; Set the installation directory
SetOutPath "$INSTDIR"

; Copy the files to the installation directory
File /r "path\to\your\app\dist\*.*"

; Create shortcuts if needed
CreateShortCut "$DESKTOP\Your Awesome App.lnk" "$INSTDIR\your_executable_name.exe"

; Add other installation tasks as needed

; End of section
SectionEnd
```

Replace `"YourAwesomeAppInstaller.exe"` with the desired name for your installer, and `"path\to\your\app\dist\*.*"` with the path to the directory containing the generated executable.

3. Compile the NSIS script: Open a terminal or command prompt, navigate to the directory containing your NSIS script, and run the following command:

```bash
makensis installer_script.nsi
```

This will compile the NSIS script and generate the installer file (`YourAwesomeAppInstaller.exe`).

4. Distribute the installer: Now you have the installer for your hybrid desktop app. You can distribute this installer to your users, allowing them to install and run your app easily on their systems.

## Version Settings

The version information for your hybrid desktop app is defined in the `version.rc` file. Make sure to update the version number and other details accordingly before building the app.

## Summary

Congratulations! You've learned how to create an installer for your hybrid desktop app using NSIS. This will make it easier for your users to install and run your app on their systems.

Explore the documentation and have fun building amazing cross-platform applications with your new HybExe framework!

If you encounter any issues or have questions, don't hesitate to reach out to us.

Happy coding and distributing! 😎🚀

<div align="center">
  <a href="https://github.com/tejasnayak25/hybexe">
    <img src="https://img.shields.io/github/stars/tejasnayak25/hybexe?style=social" alt="GitHub stars" width="100">
  </a>
  <a href="https://github.com/tejasnayak25/hybexe/fork">
    <img src="https://img.shields.io/github/forks/tejasnayak25/hybexe?style=social" alt="GitHub forks" width="100">
  </a>
</div>
