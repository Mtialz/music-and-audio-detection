from pydub import AudioSegment
# Example usage
left_track_path = "C:\education-MS\DSP\project\left_channel.wav"
right_track_path = "C:\education-MS\DSP\project\Right_channel.wav"
output_path = "C:\education-MS\DSP\project\stereo_music.mp3"

def create_stereo_track(left_track_path, right_track_path, output_path):
    # Load mono tracks
    left_track = AudioSegment.from_file(left_track_path)
    right_track = AudioSegment.from_file(right_track_path)

    # Ensure both tracks have the same duration
    if len(left_track) > len(right_track):
        right_track += AudioSegment.silent(duration=len(left_track) - len(right_track))
    elif len(right_track) > len(left_track):
        left_track += AudioSegment.silent(duration=len(right_track) - len(left_track))

    # Combine tracks into stereo
    stereo_track = left_track.overlay(right_track)

    # Export the stereo track
    stereo_track.export(output_path, format="wav")



create_stereo_track(left_track_path, right_track_path, output_path)
