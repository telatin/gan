"""GAN nomenclature package."""

from .generator import (
    GenerationResult,
    GeneratedName,
    combine_etymology,
    combine_roots,
    generate_entries,
    generate_outputs,
    join_two_roots,
)
from .io import read_root_table

__all__ = [
    "GenerationResult",
    "GeneratedName",
    "combine_etymology",
    "combine_roots",
    "generate_entries",
    "generate_outputs",
    "join_two_roots",
    "read_root_table",
]

__version__ = "0.1.0"
