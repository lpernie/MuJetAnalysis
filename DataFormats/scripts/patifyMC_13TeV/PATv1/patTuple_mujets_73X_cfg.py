## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *

# verbose flags for the PF2PAT modules
process.options.allowUnscheduled = cms.untracked.bool(True)

### Add MuJet Dataformats
from MuJetAnalysis.DataFormats.EventContent_version10_cff import *
process = customizePatOutput(process)

process.load("MuJetAnalysis.DataFormats.RECOtoPAT_cff")
process.patMuons.addGenMatch = cms.bool(True)
process.patMuons.embedGenMatch = cms.bool(True)

## pick latest HLT process
process.patTrigger.processName = cms.string( "*" )
process.patTriggerEvent.processName = cms.string( "*" )

process.load("MuJetAnalysis.MuJetProducer.MuJetProducer_cff")

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(
		'file:/fdata/hepx/store/user/dildick/DarkSUSY_mH_125_mGammaD_0250_ctau_0_13TeV_madgraph452_bridge224_LHE_pythia8_731p2_GEN_TestMay11/DarkSUSY_mH_125_mGammaD_0250_ctau_0_13TeV_cT_000_madgraph452_bridge224_LHE_pythia8_731p2_RECO/10a99d6c872a53cc0f8d52992fbcebda/out_reco_1_1_cii.root'
  )
)

process.maxEvents.input = 100

process.p = cms.Path(
	process.MuJetProducers
)
