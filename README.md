# Summary
Little Angel is an interactive Python-based reconnaissance tool built to inspect HTTP response headers during initial target profiling. By executing automated requests with redirection handling, it analyzes web targets to retrieve HTTP status codes, load balancers or Web Application Firewalls, CMS and framework signatures, client IP forwarding rules, and baseline XSS protection headers
<br>
<br>
# Target Audience
Little Angel is designed for anyone performing target profiling and reconnaissance, including:
* SOC Analysts and Blue Teams: Useful for initial incident triage, verifying web infrastructure behavior, inspecting security response headers, and analyzing external target signatures.
* Bug Bounty Hunters and Red Teams: Ideal for rapid, lightweight OSINT, WAF detection, and tech stack fingerprinting prior to deeper security assessment
* Cybersecurity Students and Enthusiasts: A clear, practical example of automation using Python for HTTP header extraction and network request handling

# <br>How to install
Clone this repository
```bash
git clone https://github.com/Mentolado/Little-Angel.git
```
Go to Little-Angel folder
```bash
cd Little-Angel
```
## Create a venv environment with venv module
> **Note for beginners:** In the command `python -m venv venv`, the first `venv` specifies the Python module used to create virtual environments, while the second `venv` is the name of the directory where the environment will be created.
```bash
python -m venv venv
```
## Activate the virtual environment
* On powershell
```bash
.\venv\Scripts\Activate.ps1
```
* On Linux/MacOS(Bash/Zsh)
```bash
source venv/bin/activate
```
## Install dependencies
```bash
pip install -r requirements.txt
```
## Run the tool
```bash
python Little Angel.py
```
> Additional notes for begginers: <br>
>* Deactivating the Virtual Environment: Regardless of whether you are using PowerShell, Bash, or Zsh, you can exit the virtual environment at any time by running:
deactivate
>* Execution Policy Error (Windows): If PowerShell blocks script execution when activating the environment, run this command in your PowerShell session:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
