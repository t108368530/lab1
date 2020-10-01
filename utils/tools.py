import wave


def change_wav_hader(file,sampleRate):
    with wave.open(file, "r") as audio:
        params = audio.getparams()
        frames = audio.readframes(params.nframes)
        params = params._replace(framerate=sampleRate)

    with wave.open(file, "wb") as audio:
        audio.setparams(params)
        audio.writeframesraw(frames)
        audio.close()
