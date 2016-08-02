import gpxpy
import gpxpy.gpx
import sys

# Parse filename and append all the points to gpx_segment.
def append_points(filename, gpx_segment):
    gpx_file = open(filename, 'r')

    gpx = gpxpy.parse(gpx_file)

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(point.latitude, point.longitude, point.elevation, point.time))

if len(sys.argv)<=4:
    print 'Merge n gpx tracks.\n'
    print 'Syntax:'
    print sys.argv[0]+' first.gpx second.gpx ... result.gpx\n'
    print 'With N args: first N-1 args are the gpx to be merged, last arg is the result.'
    sys.exit(0)

gpx = gpxpy.gpx.GPX()

# Create first track in our GPX:
gpx_track = gpxpy.gpx.GPXTrack()
gpx.tracks.append(gpx_track)

# Create first segment in our GPX track:
gpx_segment = gpxpy.gpx.GPXTrackSegment()
gpx_track.segments.append(gpx_segment)

for filename in sys.argv[1:-1]:
    append_points(filename,gpx_segment)

gpx_segment.points = sorted(gpx_segment.points, key=lambda p: p.time)

with open(sys.argv[-1], 'w') as the_file:
    the_file.write(gpx.to_xml())
