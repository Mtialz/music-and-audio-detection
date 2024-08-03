import soundfile as sf
import librosa

def split_and_save_channels(input_file, output_left, output_right):
    # Load the stereo audio file
    y, sr = librosa.load(input_file, sr=None, mono=False)

    # Extract left and right channels
    left_channel = y[0]
    right_channel = y[1]

    # Save left and right channels as separate audio files
    sf.write(output_left, left_channel, sr)
    sf.write(output_right, right_channel, sr)

# Example usage:
input_file = 'C:\education-MS\DSP\project\massive-riser-2-SBA-300420795-preview (1).wav'  # Replace with your stereo music file path
output_left = 'C:\education-MS\DSP\project\left_channel.wav'
output_right = 'C:\education-MS\DSP\project\Right_channel.wav'

split_and_save_channels(input_file, output_left, output_right)
