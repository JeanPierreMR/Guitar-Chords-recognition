from ChordsExtractor.src.model import CNN
from chordSplit import splitSecs

class Classifier():

    def get_chords_ls(self, song_path):
        chords_ls = []
        audio_path_ls = splitSecs(song_path)

        for audio_path in audio_path_ls:
            chords_ls.append(self.get_chord(audio_path))

        return chords_ls

    def get_chord(self, song_path):
        cnn = CNN((128, 87))
        cnn.load_model()
        cnn = cnn
        '''file should be wav and more tan 3 seconds'''
        chord = cnn.predict(song_path, False)
        if chord == 'N/A':
            return False
        return chord

    def get_song_chords(self):
        pass


#example of use
def main():

    classifier = Classifier()
    chord = classifier.get_chord("C:\\Users\\JPMR0\\Guitar-Chords-recognition\\output\\recording\\am.wav")
    # chord = classifier.get_chord("C:\\Users\\JPMR0\\Desktop\\brb.wav")
    return(chord)


if __name__ == "__main__":
    main()
