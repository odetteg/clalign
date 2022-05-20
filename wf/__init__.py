"""
Clean and Interpret Alignments
"""
import subprocess
from pathlib import Path
from typing import Optional

from latch import small_task, workflow
from latch.types import LatchFile


@small_task
def align_task(
        align_file: LatchFile,
        config_file: LatchFile) -> LatchFile:

    _align_cmd = [
        "CIAlign",
        "--infile",
        align_file.local_path,
        "--inifile",
        str(Path(config_file).resolve())
    ]
    # defining the output
    file_align = Path("align.txt").resolve()
    subprocess.run(_align_cmd, check=True)

    return LatchFile(str(file_align), "latch:///align.txt")


@workflow
def CIAlign(align_file: LatchFile, config_file: LatchFile) -> LatchFile:
    """The workflow is the implementation of the CIAlign tool.

    ----


    # Introduction 
    CIAlign is a command line tool
    that allows users to remove specific issues from an MSA, visualise the MSA, and interpret the MSA.
    The tool will remove regions of low coverage due to insertions, gaps
    crop poorly aligned sequence ends and remove sequences that are too divergent or too short.
    Compared to other tools, user have the opportunity to distinguish between gaps within 
    the body of a sequence, that should be removed and gaps padding the ends of sequences of different lengths
    CIAlign will first remove divergent sequences and consider shorter sequences towards the end of the
    Cleaning stages. Mini alignments can be generated and visualised using coloured rectangles. 
    Areas removed are marked up with different colors. The tool can also generate 
    Sequence logos to show the information and base/amino acid content at each position

    Args:

        align_file: the file to be aligned


          __metadata__:
            display_name: Input File
        config_file: File containing configurations


          __metadata__:
            display_name: Configs

        output_file: The file used to write output


          __metadata__:
            display_name: Output File
    """
    return align_task(align_file=align_file, config_file=config_file)
