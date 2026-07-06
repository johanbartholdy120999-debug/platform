import py_compile
import glob


def test_all_python_files_compile():
    python_files = glob.glob("**/*.py", recursive=True)

    for file in python_files:
        py_compile.compile(file, doraise=True)
