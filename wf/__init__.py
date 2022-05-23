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

    # defining the output and outfile_stem
    out_put = Path("CIAlign.txt").resolve()

    # The function to run
    _align_cmd = [
        "CIAlign",
        "--infile",
        align_file.local_path,
        "--outfile_stem",
        CIAlign,
        "--inifile",
        str(Path(config_file).resolve())
    ]

    subprocess.run(_align_cmd, check=True)

    return LatchFile(str(out_put), "latch:///CIAlign.txt")


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


# if __name__ == "__main__":
# CN(align_file=LatchFile(r"C:\Users\Steve Odete\latch_wf\clalign\data\example1.fasta"),
#  config_file=LatchFile(r"C:\Users\Steve Odete\latch_wf\clalign\my_configs.ini"))
