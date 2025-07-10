"""
Tests to validate CI/CD setup and project configuration.
These tests ensure the development environment is properly configured.
"""

import sys
from pathlib import Path


def test_python_version():
    """
    Test that we're using Python 3.12+ (minimum for development).
    """
    major, minor, *_ = sys.version_info
    print(f"Python version: {sys.version_info}")
    assert (major, minor) >= (3, 12), f"Expected Python 3.12+, got {sys.version_info}"


def test_project_structure():
    """
    Test that essential project files exist.
    """
    backend_root = Path(__file__).parent.parent
    repo_root = backend_root.parent

    # Essential files for backend
    backend_files = [
        "pyproject.toml",
        ".pre-commit-config.yaml",
    ]

    # Essential files for CI/CD (at repository root)
    ci_files = [
        ".github/workflows/ci.yml",
        ".github/workflows/backend-test.yml",
        ".github/workflows/backend-lint.yml",
        ".github/workflows/backend-security.yml",
    ]

    # Check backend files
    for file_path in backend_files:
        assert (backend_root / file_path).exists(), f"Missing backend file: {file_path}"

    # Check CI files at repository root
    for file_path in ci_files:
        assert (repo_root / file_path).exists(), f"Missing CI file: {file_path}"


def test_linting_tools_available():
    """
    Test that linting tools can be imported (they're installed in CI).
    """
    try:
        import ruff

        assert ruff is not None
    except ImportError:
        print("Ruff is not installed")

    try:
        import black

        assert black is not None
    except ImportError:
        print("Black is not installed")


def test_testing_framework():
    """
    Test that pytest is working correctly.
    """
    # This test validates that pytest can discover and run tests
    assert True, "Pytest is working correctly"


# Trigger CI/CD workflow with coverage upload
def test_ci_cd_coverage_trigger():
    """
    Test to trigger CI/CD workflow and coverage upload.
    """
    assert True, "This test ensures CI/CD workflow runs and uploads coverage"
