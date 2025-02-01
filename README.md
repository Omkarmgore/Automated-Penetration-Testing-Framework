# Linux Pentest Framework

This tool is a Linux-based penetration testing framework designed to automate and simplify network scanning, vulnerability detection, and penetration testing tasks using popular tools such as nmap, nikto, and hydra. It provides a user-friendly command-line interface with logging and reporting features, tailored specifically for Linux environments.
"

# Features
echo "
## Features

- Network Scanning: Uses nmap for detailed service and port scanning.
- Vulnerability Scanning: Includes nikto for web server vulnerability scanning.
- Brute-Force Attack Simulation: Supports hydra for password cracking attacks.
- Report Generation: Generates HTML reports of scan results for future reference.
- Rich CLI Interface: Provides easy-to-navigate terminal UI using rich.
- Multi-threaded Execution: For faster scans and tasks execution.
"

# Prerequisites
echo "
## Prerequisites

Ensure that the following dependencies are installed on your system:

- Python 3.6+
- nmap
- nikto
- hydra
- rich (Python package for terminal UI)
"

# Install required Python dependencies
echo "To install the required Python dependencies, run:
pip install rich bcrypt
"

# Install Linux tools
echo "You can install the Linux tools using apt-get:
sudo apt-get install nmap nikto hydra
"

# Installation steps
echo "
## Installation

1. Clone the repository:
   git clone https://github.com/yourusername/linux-pentest-framework.git
   cd linux-pentest-framework

2. Set up the framework:
   Ensure that you have all dependencies installed. If not, refer to the above section for the installation steps.
"

# Usage instructions
echo "
## Usage

To run the framework, you must execute the Python script. Root privileges are required for certain features such as scanning privileged ports.

1. Run the tool:
   sudo python3 pentest_framework.py

2. Available Options:
   - Linux Service Scan: Specialized scan for common Linux services (SSH, HTTP, MySQL, etc.).
   - View Reports: Display and open previously generated scan reports.
   - Run a full network scan: Advanced scan using nmap.
"

# Sample Workflow
echo "
### Sample Workflow

1. Scanning Linux Services:
   You can scan common Linux services on a target host by invoking the service scan:
   python3 pentest_framework.py

   You will be prompted to select a task or run an advanced network scan.

2. Viewing Reports:
   After scanning, generated reports can be viewed directly through the UI. The tool will display a list of reports to choose from.
"

# Logging and reporting
echo "
## Logging and Reporting

- Log Files: Logs are automatically generated in pentest_framework.log located in the root folder.
- Reports: Scan reports are saved in the reports folder as HTML files.
"

# Contributing section
echo "
## Contributing

Feel free to fork this repository and make changes to improve functionality or add features. Submit pull requests for any improvements or bug fixes.
"

# License section
echo "
## License

This project is licensed under the MIT License.
"

# Detailed Steps to Run the Tool
echo "
## Detailed Steps to Run the Tool

1. Ensure Linux Dependencies are Installed:
   Run the following command to check if nmap, nikto, and hydra are installed:
   which nmap nikto hydra

   If any tool is missing, install them via:
   sudo apt-get install nmap nikto hydra

2. Execute the Framework:
   Navigate to the directory where the framework is located, and run the tool as root:
   sudo python3 pentest_framework.py

3. Follow the Prompts:
   The tool will guide you through the options for scanning, logging, and viewing reports.

4. View Reports:
   After the scan is completed, you can view the generated reports. Reports are stored in the reports directory and can be opened using the UI or manually.
"

# Troubleshooting section
echo "
## Troubleshooting

- Missing Tools: If the tool reports missing dependencies, install them using apt-get install as shown above.
- Permissions Issues: Ensure that the script is run with root privileges for full functionality.
- Log Output: Check the log file pentest_framework.log in the root directory for any errors.
"

echo "README generation complete."
