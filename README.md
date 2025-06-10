# MasterThesis
This is the repository of used code for the Master Thesis of Yarne Thijs named "Privacy Preserving Systems using FHE-friendly Ciphers".

Attached is all generated, used (and unused) code. Among them are a few folders of interest:


Note: I wanted to have the full files and directory tree in GitHub. But I only could upload 100 files at a time, which would take ages. 
I apologise for this crude use of Github.


-   Within HybridHE are all files of this library. Particularily hybrid-HE-framework is important. Then the following folders have heavy modifications:
    +   YARNE (Created from scratch)
    +   build (Build folder of the library)
    +   Ciphers (Changed important files where necessary)
        +   he_only
        +   pasta_3
        +   pasta2_3
        +   pasta2_4
        +   common_Zp
        +   hera_5
-   Within OpenFHE are the files I used for that library
    +   Important is the main file
    +   Also the runPython.sh
-   Visualise Is the directory for the visualisation of the simulations/Timings
    +   Important is the process and Recreate2 py-files