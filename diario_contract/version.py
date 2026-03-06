from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("diario-contract")
except PackageNotFoundError:
    __version__ = "1.2.0"
