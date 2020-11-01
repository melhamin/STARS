@echo OFF

@echo ############################################################
@echo #             INSTALLING STARS... PLEASE WAIT              #
@echo ############################################################

@echo [+] Installing virtual env...
python -m pip install --disable-pip-version-check pip
python -m pip install --disable-pip-version-check virtualenv

IF %ERRORLEVEL% == 9009 (
    @echo [*] ERROR: IT SEEMS THAT PYTHON IS NOT INSTALLED. INSTALL PYTHON AND RETRY...
    GOTO END
)

@echo [+] Creating a new venv...
python -m venv venv
@echo [+] Actiating venv...
cmd /k "cd /d venv\Scripts & activate & cd /d ../../ & @echo [+] Installing the required packages... & pip install --disable-pip-version-check -r requirements.txt & @echo [+] Creating the executable... & pyinstaller --onefile src/main.py -n STARS --icon src/bilkent-logo.ico --log-level ERROR & @echo [+] Cleaning up... & cd /d venv\Scripts & deactivate & cd /d ../../ & rmdir /S /Q build & rmdir /S /Q venv & del STARS.spec & @echo [*] STARS WAS SUCCESSFULY INSTALLED! NOW YOU MAY CLOSE THIS WINDOW."

:END
pause

