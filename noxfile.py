from typing import Any
import nox
from nox.sessions import Session
import os

nox.options.sessions = "flake8", "black", "mypy", "tests"
locations = "src", "tests", "noxfile.py"
temp_file_name = "temp.txt"


def install_with_constraints(session: Session, *args: str, **kwargs: Any) -> None:
    session.run(
        "poetry",
        "export",
        "--dev",
        "--format=requirements.txt",
        "--without-hashes",
        f"--output={temp_file_name}",
        external=True,
    )
    session.install(f"--constraint={temp_file_name}", *args, **kwargs)
    os.unlink(temp_file_name)


@nox.session(python="3.8")
def flake8(session: Session) -> None:
    """Run flake8 code linter."""
    args = session.posargs or locations
    install_with_constraints(session, "flake8")
    session.run("flake8", *args)


@nox.session(python="3.8")
def black(session: Session) -> None:
    """Run black code formatter."""
    args = session.posargs or locations
    install_with_constraints(session, "black")
    session.run("black", *args)


@nox.session(python="3.8")
def mypy(session: Session) -> None:
    """Type-check using mypy."""
    args = session.posargs or locations
    install_with_constraints(session, "mypy")
    session.run("mypy", *args)


@nox.session(python="3.8")
def tests(session: Session) -> None:
    """Run the test suite."""
    args = session.posargs
    session.run("poetry", "install", "--no-dev", external=True)
    install_with_constraints(session, "pytest")
    install_with_constraints(session, "faker")
    session.run("pytest", *args)
