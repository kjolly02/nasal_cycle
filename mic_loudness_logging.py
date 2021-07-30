import soundfile as sf
import pyloudnorm as pyln
import wav_data_smoothing as wv

while True:
	filepath = input("Enter a .wav file to get it's loudness: ")
	if (len(filepath) != 0):
		data, rate = sf.read(filepath) # load audio (with shape (samples, channels))
		# 44100 hz
		print(len(data))
		data = wv.moving_average(data[:-1])
		print(rate)
		rate /= 175
		# 7665 / 252 = 1341375 / 44100 = 30.416667
		print(len(data))
		meter = pyln.Meter(rate) # create BS.1770 meter
		loudness = meter.integrated_loudness(data) # measure loudness
		print("Loudness: ", loudness)
	else:
		break