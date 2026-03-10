from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("diario-contract")
except PackageNotFoundError:
    __version__ = "2.0.0"
