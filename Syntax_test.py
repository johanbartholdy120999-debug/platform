import compileall
import os


def test_python_syntax():
    """
    Compiles all Python files in the repo.
    Fails if ANY syntax error exists.
    """
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    result = compileall.compile_dir(
        root_dir,
        force=True,
        quiet=1
    )

    assert result is True, "Python syntax error detected in repository"
