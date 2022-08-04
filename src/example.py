import csv
from midistats import song_stats
from mido import MidiFile

mozart = MidiFile("mozart_sonata_310_2.mid")

with open("mozart_summary.csv", "w", newline='') as csvfile:
    fieldnames = ["note", "count", "pct"]
    writer = csv.DictWriter(csvfile, fieldnames)

    writer.writeheader()
    for row in song_stats(mozart):
        writer.writerow(row)
