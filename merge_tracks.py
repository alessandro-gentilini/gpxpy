import gpxpy
import gpxpy.gpx

# Parse filename and append all the points to gpx_segment.
def append_points(filename, gpx_segment):
    gpx_file = open(filename, 'r')

    gpx = gpxpy.parse(gpx_file)

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(point.latitude, point.longitude, point.elevation, point.time))


gpx = gpxpy.gpx.GPX()

# Create first track in our GPX:
gpx_track = gpxpy.gpx.GPXTrack()
gpx.tracks.append(gpx_track)

# Create first segment in our GPX track:
gpx_segment = gpxpy.gpx.GPXTrackSegment()
gpx_track.segments.append(gpx_segment)

append_points('1.gpx',gpx_segment)


with open('somefile.gpx', 'w') as the_file:
    the_file.write(gpx.to_xml())
