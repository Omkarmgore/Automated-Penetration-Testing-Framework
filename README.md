# README.md generator for uploading to GitHub

# Create README.md file with the content for the Linux Pentest Framework

cat <<EOL > README.md
# Linux Pentest Framework

This tool is a Linux-based penetration testing framework designed to automate and simplify network scanning, vulnerability detection, and penetration testing tasks using popular tools such as \`nmap\`, \`nikto\`, and \`hydra\`. It provides a user-friendly command-line interface with logging and reporting features, tailored specifically for Linux environments.

## Features

- **Network Scanning**: Uses \`nmap\` for detailed service and port scanning.
- **Vulnerability Scanning**: Includes \`nikto\` for web server vulnerability scanning.
- **Brute-Force Attack Simulation**: Supports \`hydra\` for password cracking attacks.
- **Report Generation**: Generates HTML reports of scan results for future reference.
- **Rich CLI Interface**: Provides easy-to-navigate terminal UI using \`rich\`.
- **Multi-threaded Execution**: For faster scans and tasks execution.

## Prerequisites

Ensure that the following dependencies are installed on your system:

- **Python 3.6+**
- **nmap**
- **nikto**
- **hydra**
- **rich** (Python package for terminal UI)

To install the required Python dependencies, run:
\`\`\`bash
pip install rich bcrypt
\`\`\`

You can install the Linux tools using \`apt-get\`:
\`\`\`bash
sudo apt-get install nmap nikto hydra
\`\`\`

## Installation

1. **Clone the repository**:
   \`\`\`bash
   git clone https://github.com/yourusername/linux-pentest-framework.git
   cd linux-pentest-framework
   \`\`\`

2. **Set up the framework**:
   Ensure that you have all dependencies installed. If not, refer to the above section for the installation steps.

## Usage

To run the framework, you must execute the Python script. **Root privileges** are required for certain features such as scanning privileged ports.

1. **Run the tool**:
   \`\`\`bash
   sudo python3 pentest_framework.py
   \`\`\`

2. **Available Options**:
   - **Linux Service Scan**: Specialized scan for common Linux services (SSH, HTTP, MySQL, etc.).
   - **View Reports**: Display and open previously generated scan reports.
   - **Run a full network scan**: Advanced scan using \`nmap\`.

### Sample Workflow

1. **Scanning Linux Services**:
   You can scan common Linux services on a target host by invoking the service scan:
   \`\`\`bash
   python3 pentest_framework.py
   \`\`\`

   You will be prompted to select a task or run an advanced network scan.

2. **Viewing Reports**:
   After scanning, generated reports can be viewed directly through the UI. The tool will display a list of reports to choose from.

## Logging and Reporting

- **Log Files**: Logs are automatically generated in \`pentest_framework.log\` located in the root folder.
- **Reports**: Scan reports are saved in the \`reports\` folder as HTML files.

## Contributing

Feel free to fork this repository and make changes to improve functionality or add features. Submit pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
EOL

# Bash script to initialize a Git repository, commit the README.md, and upload to GitHub

# Initialize git repository
git init

# Add README.md to the staging area
git add README.md

# Commit the changes
git commit -m "Added README.md for Linux Pentest Framework"

# Set the remote URL (replace yourusername and reponame with your GitHub details)
git remote add origin https://github.com/yourusername/reponame.git

# Push the changes to GitHub
git branch -M main
git push -u origin main

echo "README.md uploaded to GitHub successfully!"
