@echo ############################################################
@echo #             INSTALLING STARS... PLEASE WAIT              #
@echo ############################################################

@echo [+] Installing virtual env...
python -m pip install --disable-pip-version-check virtualenv
@echo [+] Creating a new venv...
python -m venv venv
@echo [+] Actiating venv...
cmd /k "cd /d venv\Scripts & activate & cd /d ../../ & @echo [+] Installing the required packages... & pip install --disable-pip-version-check -r requirements.txt & @echo [+] Creating the executable... & pyinstaller --onefile main.py -n STARS --icon bilkent-logo.ico --log-level ERROR & @echo [+] Cleaning up... & cd /d venv\Scripts & deactivate & @echo [*] STARS WAS SUCCESSFULY INSTALLED! NOW YOU MAY CLOSE THIS WINDOW."
pause

