@echo off
call venv\Scripts\activate
python -m unittest discover -s biblioteca\tests
pause
