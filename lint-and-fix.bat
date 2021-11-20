REM lint-and-fix.bat - for python3 linting and formatting
REM uses black for formatting
REM uses flake8 for linting
REM
black searchApi
REM black --check searchApi
flake8 searchApi --max-line-length=120
