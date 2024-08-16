from pathlib import Path

from mido import MidiFile, MidiTrack


def remove_redundant_events(input_path):
    mid = MidiFile(input_path)
    new_tracks = []
    for old_track in mid.tracks:
        new_track = MidiTrack()
        new_tracks.append(new_track)

        last_event = None
        for msg in old_track:
            new_track.append(msg)
            if msg.type == "note_on":
                if last_event is None:
                    last_event = msg
                else:
                    if (
                        msg.channel == last_event.channel
                        and msg.note == last_event.note
                        and msg.time == 0
                    ):
                        print("Last event:    ", last_event)
                        print("Removed event: ", new_track.pop())
                        last_event.velocity = msg.velocity
                    else:
                        last_event = msg
            else:
                last_event = None

    mid.save(input_path)


for file_path in Path("midi/alvinwong").iterdir():
    if file_path.is_file():
        remove_redundant_events(file_path)
