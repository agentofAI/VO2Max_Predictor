This readme.txt file was generated on 2020-03-23 by Ryan J. Larsen

GENERAL INFORMATION

1. Title of Dataset: Magnetic Resonance Spectroscopy Imaging, body composition, and cardiorespiratory fitness: Baseline data from a multimodal intervention study 

2. Author Information
	A. Principal Investigator Contact Information
		Name: Aron K. Barbey
		Institution: University of Illinois at Urbana-Champaign
		Email: barbey@illinois.edu

	B. Alternate Contact Information
		Name: Ryan J. Larsen
		Institution: University of Illinois at Urbana-Champaign
		Email: larsen@illinois.edu

3. Date of data collection:2015

4. Geographic location of data collection:  Champaign-Urbana, IL, USA

5. Information about funding sources that supported the collection of the data: The research is based upon work supported by the Office of the Director of National Intelligence (ODNI), Intelligence Advanced Research Projects Activity (IARPA), via Contract 2014-13121700004 to the University of Illinois at Urbana-Champaign (PI: Barbey). The views and conclusions contained herein are those of the authors and should not be interpreted as necessarily representing the official policies or endorsements, either expressed or implied, of the ODNI, IARPA, or the U.S. Government. The U.S. Government is authorized to reproduce and distribute reprints for Governmental purposes notwithstanding any copyright annotation thereon.


SHARING/ACCESS INFORMATION

1. Licenses/restrictions placed on the data: CC0 1.0 Universal public domain dedication

2. Links to publications that cite or use the data:  "Body mass and cardiorespiratory fitness are associated with altered brain metabolism." Ryan J. Larsen, Lauren B. Raine, Charles H. Hillman, Arthur F. Kramer, Neal J. Cohen, Aron K. Barbey.  Metabolic Brain Disease, 2020.

5. Was data derived from another source? no

6. Recommended citation for this dataset: Larsen, Ryan; Charles, Hillman; Kramer, Arthur; Cohen, Neal; Barbey, Aron (2021) Magnetic Resonance Spectroscopy Imaging, body composition, and cardiorespiratory fitness: Baseline data from a multimodal intervention study . University of Illinois at Urbana-Champaign. https://doi.org/10.13012/B2IDB-9371397_V1


DATA & FILE OVERVIEW

1. File List: 
Baseline_Data_Insight1b.csv:
Speadsheet of measures from Magnetic Resonance Spectroscopy Imaging, body composition, and cardiorespiratory fitness

2. Are there multiple versions of the dataset? no


METHODOLOGICAL INFORMATION

1. Description of methods used for collection/generation of data: 
 See "Body mass and cardiorespiratory fitness are associated with altered brain metabolism." Ryan J. Larsen, Lauren B. Raine, Charles H. Hillman, Arthur F. Kramer, Neal J. Cohen, Aron K. Barbey.  Metabolic Brain Disease, 2020.

2. Methods for processing the data: 

For a description of analysis performed using this data set, see "Body mass and cardiorespiratory fitness are associated with altered brain metabolism." Ryan J. Larsen, Lauren B. Raine, Charles H. Hillman, Arthur F. Kramer, Neal J. Cohen, Aron K. Barbey.  Metabolic Brain Disease, 2020.

For a more detailed description of the method used to process the MRSI data, see
Larsen RJ, Newman M, Nikolaidis A (2016) Reduction of variance in measurements of average metabolite concentration in anatomically-defined brain regions J Magn Reson 272:73-81 doi:10.1016/j.jmr.2016.09.005

3. Describe any quality-assurance procedures performed on the data:
For the following subjects, height data have been discarded due to inconsistency with post-intervention height measurement: 1297,1314,1350
For analysis in the cited article, when Confidence<5, VO2max data were discarded

4. People involved with sample collection, processing, analysis and/or submission: 
Ryan J. Larsen


DATA-SPECIFIC INFORMATION FOR: Baseline_Data_Insight1b

1. Number of variables: 45

2. Number of cases/rows: 435

3. Variable List: 

Subject Number, arbitrary identifier
Age, units: years
Sex
Height, body height, units: cm
Mass, body mass, units: kg
Total_Lean_Mass, total lean body mass, units: kg
BMI, body mass index, units: kg/m^2
WBTPF, Whole Body Total Percent Fat
VO2max_abs, VO2max_absolute, units: Liters/min
VO2max_rel, VO2max_relative, units: mL/kg/min
Confidence, a number indicating the degree of confidence in the accuracy of the measurement, a higher number indicates greater confidence   
Fat_Free_VO2max, Fat Free VO2max, VO2max_absolute divided by total lean body mass

MRS data
VOI_RL, the Volume of Interest in the Right-Left direction
VOI_AP, the Volume of Interest in the Anterior-Posterior direction
Tech, the technician who performed the scan

Five variables are given for each brain region:

tNAA_Cr is NAA/Cr
GM is gray matter fraction
WM is white matter fraction
CSF is cerebral spinal fluid fraction
scanfrac is the volume fraction of the region within the Volume of Interest 

Brain regions are indicated by appending the following indicators to variable names:

Ant_Right is right anterior gray matter
Ant_Left is left anterior gray matter  
Pstr_Right is right posterior gray matter
Pstr_Left is left posterior gray matter
WM_Right is right white matter
WM_Left is left white matter

4. Missing data codes: 
Missing numbers are coded as NaN
Missing categorical variables are coded as <undefined>

