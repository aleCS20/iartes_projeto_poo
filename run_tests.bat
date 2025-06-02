@echo off
call venv\Scripts\activate
python -m unittest discover -s inventario_produtos_tdd\tests
pause
