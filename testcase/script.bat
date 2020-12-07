@echo off
if exist %CD%\src\test\testcases\ (
    echo "Cleaning testcases"
	rmdir /Q /S %CD%\src\test\testcases\
)
    echo "Creating testcases"
    mkdir %CD%\src\test\testcases\

if exist %CD%\src\test\solutions\ (
    echo "Cleaning solutions"
	rmdir /Q /S %CD%\src\test\solutions\
)
    echo "Creating solutions"
    mkdir %CD%\src\test\solutions\

if exist %CD%\output\ (
    echo "Cleaning Output..."
    rmdir /Q /S %CD%\output\
)
    echo "Creating Output..."
    mkdir %CD%\output\
    mkdir %CD%\output\test

if exist %CD%\src\test\CheckSuite.txt (
    echo "Deleting CheckSuite.txt"
    del %CD%\src\test\CheckSuite.txt /f /q
)

if exist %CD%\test\TestUtils.py (
    echo "Rename old TestUtils.py to TestUtils_old.py"
    ren %CD%\src\test\TestUtils.py TestUtils_old.py
    echo "Copying TestUtils.py"
    robocopy %CD%\test\ %CD%\src\test\ TestUtils.py /NFL /NDL /NJH /NJS /nc /ns /np
)

if exist %CD%\test\AST.py (
    echo "Rename old AST.py to AST_old.py"
    ren %CD%\src\main\bkit\utils\AST.py AST_old.py
    echo "Copying AST.py"
    robocopy %CD%\test\ %CD%\src\main\bkit\utils\ AST.py /NFL /NDL /NJH /NJS /nc /ns /np
)

if exist %CD%\test\StaticError.py (
    echo "Rename old StaticError.py to StaticError_old.py"
    ren %CD%\src\main\bkit\checker\StaticError.py StaticError_old.py
    echo "Copying StaticError.py"
    robocopy %CD%\test\ %CD%\src\main\bkit\checker\ StaticError.py /NFL /NDL /NJH /NJS /nc /ns /np
)

cd src

echo.
echo "=============================================="
echo "Testing Check..."
python run.py test CheckSuite

cd ..
if exist %CD%\src\test\CheckSuite.txt (
    robocopy %CD%\src\test\ %CD%\output\ CheckSuite.txt /move /NFL /NDL /NJH /NJS /nc /ns /np
)
cd src

cd ..

@echo off

if exist %CD%\src\main\bkit\utils\AST_old.py (
    robocopy %CD%\src\main\bkit\utils\ %CD%\output\test\ AST.py /move /NFL /NDL /NJH /NJS /nc /ns /np
    ren %CD%\src\main\bkit\utils\AST_old.py AST.py
)

if exist %CD%\src\main\bkit\checker\StaticError_old.py (
    robocopy %CD%\src\main\bkit\checker\ %CD%\output\test\ StaticError.py /move /NFL /NDL /NJH /NJS /nc /ns /np
    ren %CD%\src\main\bkit\checker\StaticError_old.py StaticError.py
)

if exist %CD%\src\test\TestUtils_old.py (
    robocopy %CD%\src\test\ %CD%\output\test\ TestUtils.py /move /NFL /NDL /NJH /NJS /nc /ns /np
    ren %CD%\src\test\TestUtils_old.py TestUtils.py
)

if exist %CD%\output\CheckSuite.txt (
    ren %CD%\output\CheckSuite.txt CheckSuite.py
)