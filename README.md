# GCampIntensityAnalysis
For determining calcium concentration in flagella from kymographs.

Procedure:
  1. Generate kymograph of GCamp activation using ImageJ. This program is designed to look for outputs from KymoClear. so you will need to edit the control module to look for files from other programs.
  2. Put the GCampControlModule and GCampAnalysis files in the folder containing your data. The program will search recursively for files, so it is alright if the files are within their own folders.
  3. Run the GCampControlModule
  4. Data will be recorded in a csv called Data.csv
  5. A sample R script is included in this project just for reference for possible analyses
