__all__ = [
    "__version__",
]

try:
    # Read version from SCM metadata
    # This will only exist in a development environment
    from setuptools_scm import get_version

    __version__ = get_version("../..", relative_to=__file__)
except (ModuleNotFoundError, LookupError):
    # If setuptools_scm isn't in the environment, the call to import will fail.
    # If it *is* in the environment, but the code isn't a git checkout (e.g.,
    # it's been pip installed non-editable) the call to get_version() will fail.
    # If either of these occurs, read version from the installer metadata.
    from importlib.metadata import version

    __version__ = version("briefcase")
