import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUEZ2starSettings_cfi import *

generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    crossSection = cms.untracked.double(0.00009630),
    comEnergy = cms.double(8000.0),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring('MSEL=0            !User defined processes', 
                                        'MSUB(1)=1         !Incl Z0/gamma* production', 
                                        'MSTP(43)=3        !Both Z0 and gamma*', 
                                        'MDME(174,1)=0     !Z decay into d dbar', 
                                        'MDME(175,1)=0     !Z decay into u ubar', 
                                        'MDME(176,1)=0     !Z decay into s sbar', 
                                        'MDME(177,1)=0     !Z decay into c cbar', 
                                        'MDME(178,1)=0     !Z decay into b bbar', 
                                        'MDME(179,1)=0     !Z decay into t tbar', 
                                        'MDME(182,1)=1     !Z decay into e- e+', 
                                        'MDME(183,1)=0     !Z decay into nu_e nu_ebar', 
                                        'MDME(184,1)=0     !Z decay into mu- mu+', 
                                        'MDME(185,1)=0     !Z decay into nu_mu nu_mubar', 
                                        'MDME(186,1)=0     !Z decay into tau- tau+', 
                                        'MDME(187,1)=0     !Z decay into nu_tau nu_taubar', 
                                        'CKIN(1)=1600.     !Minimum sqrt(s_hat) value (=Z mass)'),
        # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )
)

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.3 $'),
    name = cms.untracked.string('$Source: /cvs/CMSSW/CMSSW/Configuration/GenProduction/python/EightTeV/DYToEE_M_1600_TuneZ2star_8TeV_pythia6_cff.py,v $'),
    annotation = cms.untracked.string('PYTHIA6 Z/gamma* to ee, M(e+e-) > 1600 GeV at sqrt(s) = 8TeV, Tune Z2*')
)
