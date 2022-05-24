"""
Clean and Interpret Alignments
"""
import subprocess
from pathlib import Path
from typing import Optional, Tuple

from latch import small_task, workflow
from latch.types import LatchFile


@small_task
def align_task(
        align_file: LatchFile,
        config_file: LatchFile) -> Tuple[LatchFile, LatchFile, LatchFile, LatchFile, LatchFile, LatchFile, LatchFile, LatchFile, LatchFile, LatchFile, LatchFile, LatchFile, LatchFile, LatchFile]:

    # The function to run
    _align_cmd = [
        "CIAlign",
        "--infile",
        align_file.local_path,
        "--inifile",
        str(Path(config_file).resolve()),
        "--all",
    ]

    subprocess.run(_align_cmd, check=True)

    return (LatchFile(str(Path("CIAlign_removed.txt")), "latch:///removed.txt"),
            LatchFile(str(Path("CIAlign_log.txt")), "latch:///logs.txt"),
            LatchFile(str(Path("CIAlign_cleaned.fasta")),
                      "latch:///cleaned.fasta"),
            LatchFile(str(Path("CIAlign_consensus.fasta")),
                      "latch:///consensus_sequence.fasta"),
            LatchFile(str(Path("CIAlign_with_consensus.fasta")),
                      "latch:///cleanedWconsensus_sequence.fasta"),
            LatchFile(str(Path("CIAlign_input.jpg")),
                      "latch:///view_input.jpg"),
            LatchFile(str(Path("CIAlign_output.jpg")),
                      "latch:///view_output.jpg"),
            LatchFile(str(Path("CIAlign_markup.jpg")),
                      "latch:///view_markup.jpg"),
            LatchFile(str(Path("CIAlign_logo_bar.jpg")),
                      "latch:///logosBar.jpg"),
            LatchFile(str(Path("CIAlign_logo_text.jpg")),
                      "latch:///logosTxt.jpg"),
            LatchFile(str(Path("CIAlign_input_coverage.jpg")),
                      "latch:///CPlots_in.jpg"),
            LatchFile(str(Path("CIAlign_output_coverage.jpg")),
                      "latch:///CPlots_out.jpg"),
            LatchFile(str(Path("CIAlign_input_similarity.tsv")),
                      "latch:///stats_in.tsv"),
            LatchFile(str(Path("CIAlign_output_similarity.tsv")),
                      "latch:///stats_out.tsv")


            )


@ workflow
def CIAlign(align_file: LatchFile, config_file: LatchFile) -> Tuple[LatchFile, LatchFile, LatchFile, LatchFile, LatchFile, LatchFile, LatchFile, LatchFile, LatchFile, LatchFile, LatchFile, LatchFile, LatchFile, LatchFile]:
    """The workflow is the implementation of the CIAlign tool: Clean and analyse a multiple sequence alignment (MSA).

    ----


    # CIAlign
    CIAlign is a command line tool
    that allows users to remove specific issues from an MSA, visualise the MSA, and interpret the MSA.

    Users can perfom the followig functions:
    ## Cleaning an MSA

        - Remove insertions which are not present in the majority of sequences
        - Remove sequences below a threshold number of bases or amino acids
        - Crop poorly aligned sequence ends
        - Remove columns containing only gaps
        - Remove sequences above a threshold level percentage of divergence from the majority

    ## Visualise alignments

        - Generate image files showing the alignment before and after analysis using 
        - showing which columns and rows have been removed
        - Draw sequence logos
        - Visualise coverage at each position in the alignment

    ## Analyse alignment statistics 

        - Generate a similarity matrix showing the percentage identity between each sequence pair 

    # Usage 

        For basic usage, user must input a fasta file with aligned sequences
        and a config file: 

        Downlaod the config file [here](/KatyBrown/CIAlign/blob/100bd7b87a889c120435ed91035e0e27c497f964/templates/ini_template.txt)

        Edit the config file according to your needs. 

        The config file included in the description returns analysis with 
        default values

        <br>
        Downlaod an example fasta file [here](/KatyBrown/CIAlign/blob/100bd7b87a889c120435ed91035e0e27c497f964/example_files/example4.fasta)
        for dummy use

        Click __Input File__ to enter the input file and 

        **Configs** to enter the config file

        Clck **Launch Workflow** button to begin the rule

    # Accessing files 

        With a complete run, you can access the folowing files:

    > "Cleaned" alignment as **cleaned.fasta** 

    > Consensus Sequence
    #### **consensus_sequence.fasta** containing consensus sequence only
    #### **cleanedWconsensus_sequence.fasta** containing the cleaned alignment plus the consensus

    <br>
    > Mini Alignments 
    #### **view_input.jpg:**  with the the input alignment
    #### **view_output.jpg:** with the  the cleaned output alignment
    #### **view_markup.jpg:** with the the input alignment with deleted rows and columns marked

    <br>
    > Logos 
    ##### **logosBar.jpg:** the alignment represented as a bar chart
    #### **logosTxt.jpg:**  the alignment represented as a standard sequence logo 

    <br>
    > Coverage Plots 
    #### **CPlots_in.jpg** : image showing the input alignment coverage
    ##### **CPlots_out.jpg** : image showing the output alignment coverage

    <br>
    > Similarity Matrices 
    ##### **stats_in.tsv:**   similarity matrix for the input file
    ##### **stats_out.tsv:**  similarity matrix for the output file

    <br>
    > Head to **Data** on the latch console to access various files





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
