base_path="/home/jovyan/work"

event_listing_path="/Event_List/Event_Listing.csv"

event_locations_path="/Event_Location/data/Event_Locations.csv"

parking_violations_path="/Parking_Violations/data/full/"
warehouse_dir='/home/jovyan/work/spark/spark-warehouse'
#2023 Year
parking_violations_full_path=base_path+parking_violations_path+"2023.csv"

#Violation code source:    
#https://www.nyc.gov/site/finance/vehicles/services-violation-codes.page
#Registration class codes
#https://dmv.ny.gov/registration/registration-class-codes

violation_code=[i for i in range(1,100,1)]
registration_class_code=["""PAS
SRF
COM
MOT
HSM
LMA
LMB
LMC
BOB
ORG
ORC
RGL
RGC
SPO
CSP
HIR
CHC
THC
OML
OMT
OMF
OMR
OMV
TRC
SCL
OMS
TOW
VPL
ARG
AYG
CMH
FPW
GSM
JWV
MCL
NLM
HAM
HAC
SOS
VAS
EDU
MED
SRN
AGR
ATV
ATD
DLR
MCD
FAR
HIS
LUA
LOC
BOT
SNO
SPC
HOU
LTR
TRL
SEM
WUG
CME
CBS
CCK
CLG
JCA
JCL
NYC
NYA
NYS
SUP
JSC
USC
USS"""]
registration_class_code=registration_class_code[0].split('\n')