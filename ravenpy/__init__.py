"""Top-level package for RavenPy."""

import os
import sys
import warnings
from pathlib import Path

from .__version__ import __author__, __email__, __version__  # noqa: F401

# Note: all the binaries associated with this package are installed in the "bin"
#       folder of the target venv, which corresponds to `sys.prefix`.

if "DO_NOT_CHECK_EXECUTABLE_EXISTENCE" not in os.environ:
    raven_exec = Path(sys.prefix) / "bin" / "raven"
    if not raven_exec.exists():
        raise IOError("The raven executable is not installed.")

    ostrich_exec = Path(sys.prefix) / "bin" / "ostrich"
    if not ostrich_exec.exists():
        raise IOError("The ostrich executable is not installed.")

raven_simg = Path(sys.prefix) / "bin" / "hydro-raven-latest.simg"
if not raven_simg.exists():
    warnings.warn(
        "The Raven Singularity image has not been downloaded. Execute \n"
        "$ singularity pull shub://132.217.141.54/hydro/raven:latest \n"
        "and store the image in <your_venv>/bin/"
    )
