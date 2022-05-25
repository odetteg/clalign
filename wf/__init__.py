"""
Clean and Interpret Multipple sequence Alignments
"""
import os
import shutil
import subprocess
from pathlib import Path
from typing import Optional, Tuple

from latch import small_task, workflow
from latch.types import LatchFile, LatchDir


@small_task
def align_task(
    align_file: LatchFile,
    config_file: LatchFile,
    output_dir: LatchDir,
    outfile_stem: str
    ) -> LatchDir:

    local_dir = "/root/cia_output/"
    local_prefix = os.path.join(local_dir, outfile_stem)

    # The function to run
    _align_cmd = [
        "CIAlign",
        "--infile",
        align_file.local_path,
        "--inifile",
        config_file.local_path,
        "--outfile_stem",
        str(local_prefix),
        "--all"
    ]

    subprocess.run(_align_cmd, check=True)

    return LatchDir(local_dir, output_dir.remote_path)


@ workflow
def CIAlign(align_file: LatchFile,
            config_file: LatchFile,
            output_dir: LatchDir,
            outfile_stem: str) -> LatchDir:

    """The workflow is the implementation of the CIAlign tool: Clean and analyse a multiple sequence alignment (MSA).

    ----


    # CIAlign

    CIAlign is a command line tool
          that allows users to remove specific issues from an MSA, visualise the MSA, and interpret the MSA.

    Users can perfom the followig functions:
    # Cleaning an MSA

              - Remove insertions which are not present in the majority of sequences
              - Remove sequences below a threshold number of bases or amino acids
              - Crop poorly aligned sequence ends
              - Remove columns containing only gaps
              - Remove sequences above a threshold level percentage of divergence from the majority
    # Visualise alignments

              - Generate image files showing the alignment before and after analysis using
              - showing which columns and rows have been removed
              - Draw sequence logos
              - Visualise coverage at each position in the alignment

    # Analyse alignment statistics

              - Generate a similarity matrix showing the percentage identity between each sequence pair

    # Usage

    For basic usage, user must input a fasta file with aligned sequence and a config file:

    Downlaod the config file [here](https://github.com/GeOdette/clalign/blob/ca26b2a208e83cb9ae25346d8c3a8c46c899ae48/my_configs.ini)

    Edit the config file according to your needs.

    The config file included in the description returns analysis with default values

    Downlaod an example fasta file [here](https://github.com/GeOdette/clalign/blob/ca26b2a208e83cb9ae25346d8c3a8c46c899ae48/data/example4.fasta)
              for dummy use

    Click [__Input File__](https://console.latch.bio/workflows/60653/parameters) to enter the input file and **Configs** to enter the config file

    Clck **Launch Workflow** button at [LatchBio](https://console.latch.bio/se/) to begin the run

    # Accessing files

    With a complete run, you can access the folowing files:

    # File with cleaned alignments

      "Cleaned" alignment as **cleaned.fasta**

    # Consensus Sequence
    > **consensus_sequence.fasta:**   containing consensus sequence only

    > **cleanedWconsensus_sequence.fasta**   containing the cleaned alignment plus the consensus

    # Mini Alignments

    > **view_input.jpg:**  with the the input alignment

    > **view_output.jpg:** with the  the cleaned output alignment

    > **view_markup.jpg:** with the the input alignment with deleted rows and columns marked

    # Logos

    > **logosBar.jpg:** the alignment represented as a bar chart

    > **logosTxt.jpg:**  the alignment represented as a standard sequence logo

    # Coverage Plots

    > **CPlots_in.jpg** :   image showing the input alignment coverage

    > **CPlots_out.jpg** :  image showing the output alignment coverage

    # Similarity Matrices

    > **stats_in.tsv:** similarity matrix for the input file

    > **stats_out.tsv:**    similarity matrix for the output file

    > Head to **Data** on the latch console to access various files




    __metadata__:
        display_name: Clean and Interpret Multipple sequence Alignments

        author: KatyBrown

            name: CIAlign

            email:

            github: https://github.com/KatyBrown/CIAlign.git

        repository:

        license:
            id: MIT

    Args:

        align_file: the file to be aligned
          __metadata__:
            display_name: Input File

        config_file: File containing configurations
          __metadata__:
            display_name: Configs

        output_dir: Output directory
          __metadata__:
            display_name: Output Directory
        outfile_stem: Output filename stem
          __metadata__:
            display_name: Output filename stem
    """

    return align_task(align_file=align_file,
                config_file=config_file,
                output_dir=output_dir,
                outfile_stem=outfile_stem)
