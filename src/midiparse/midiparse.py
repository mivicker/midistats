from typing import List, Dict
from collections import Counter

def squish_octaves(c: Counter) -> Dict:
    root, _ = c.most_common()[0]
    return {((note - root) % 12): count for note, count in c.items()}

def song_stats(track: MidiFile) -> List[Dict[str, int]]:
    c = Counter(message.note % 12 for message in track if message.type == "note_on")
    num_notes = sum(c.values())
    return [
        {
            "note": note,
            "count": num,
            "pct": int(num/num_notes * 100),
        } for note, num in sorted(squish_octaves(c).items())
    ]

