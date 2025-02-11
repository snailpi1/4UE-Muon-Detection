# 4UE Muon Detection

This repository contains the tools used as part of the 2024 4UE+ collaborative research project on cosmic muon detection. The project relies data collected by teams in Milan, Paris, and Prague using stacks of scintillators. 

The main tool is used to find coincidences between detection events in different data sets based on a given granularity which is determined to be optimal for the detection of cosmic muons emminating from the same atmospheric event. A supplementary log tool is used to log detection events and accurately timestamp them using GPS coordination.
 
# Dependencies

The project relies on the _numpy_, _pandas_, and _pyplot_ libraries, as well as _datetime_ for timestamp reading and conversion. The logging tool requires a serial interface with a GPS enabled Arduino.

# Credits

The project is developed under the supervision of Prof. Matthew Charles, Prof. Matthieu Guigue, and Prof. Olivier Martineau of Sorbonne Univeristy, Jussieu, by Aeden Leal, Rodolphe Ghommid,  Monija Sivarajah, Gabriel Martin, Jean-David Menye, and Alice Lesne.
