#from pyAudioAnalysis import audioSegmentation as aS
#from pyAudioAnalysis import audioBasicIO as aIO
import audioSegmentation as aS
#[Fs, x] = aIO.readAudioFile("data/Open_Mic.wav")
#segments = aS.silenceRemoval(x, Fs, 0.020, 0.020, smoothWindow = 1.0, weight = 0.3, plot = True)
#print(segments)

#segments = aS.silenceRemoval("data/Open_Mic.wav",16000,0.020, 0.020,smoothWindow=0.5, weight=0.5, plot=True )
#print(segments)
#python audioAnalysis.py speakerDiarization -i data/diarizationExample.wav --num 0

#from pyAudioAnalysis import audioSegmentation as aS

#[flagsInd, classesAll, acc, CM] = aS.mtFileClassification("data/scottish.wav", "data/svmSM", "svm", True, 'data/scottish.segments')

#aS.speakerDiarization(filename="data/diarizationExample.wav", n_speakers=4, plot_res = True)

aS.speakerDiarization(filename="data/Open_Mic.wav", n_speakers=6, plot_res = True)