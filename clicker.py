import re
from pydub import AudioSegment
from pydub.generators import Sine

def extract_tempo_from_filename(file_path):
    # Extract the number after the last underscore
    match = re.search(r'_([0-9]+)\.mp3$', file_path)
    if match:
        return int(match.group(1))
    else:
        raise ValueError("Tempo not found in the filename")

def generate_click_track(tempo, duration_ms, start_offset_ms):
    click = Sine(1000).to_audio_segment(duration=100) - 3  # A 100ms click at 1000 Hz
    beat_interval_ms = int(60000 / tempo)
    click_track = AudioSegment.silent(duration=start_offset_ms)
    
    while len(click_track) < duration_ms:
        click_track += click + AudioSegment.silent(duration=beat_interval_ms - 100)
    
    return click_track[:duration_ms]

def combine_tracks(original_path, output_path, start_offset_ms):
    original = AudioSegment.from_file(original_path)
    duration_ms = len(original)  # Get the duration of the original song in milliseconds
    tempo = extract_tempo_from_filename(original_path)
    print(f"Parsed tempo: {tempo} BPM")
    
    click_track = generate_click_track(tempo, duration_ms, start_offset_ms)  # Generate click track with offset
    
    # Ensure both tracks have the exact same length
    original = original[:duration_ms]
    click_track = click_track[:duration_ms]
    
    # Combine into stereo: original in left channel, click in right channel
    combined = AudioSegment.from_mono_audiosegments(original.set_channels(1), click_track.set_channels(1))
    combined = AudioSegment.from_mono_audiosegments(original.set_frame_rate(original.frame_rate).split_to_mono()[0],
                                                    click_track.set_frame_rate(original.frame_rate).split_to_mono()[0])
    
    combined.export(output_path, format="mp3")

if __name__ == "__main__":
    file_path = './Audio/My Jesus_F_76.mp3'
    start_offset_ms = 0  # Start with no offset, adjust this value to align the click track
    combine_tracks(file_path, './Audio/song_with_click.mp3', start_offset_ms)
