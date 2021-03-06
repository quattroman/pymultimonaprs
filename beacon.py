#!/usr/bin/python2

def get_beacon_frame(lat, lng, callsign, symbol, comment):
	def encode_lat(lat):
		lat_dir = 'N' if lat > 0 else 'S'
		lat_abs = abs(lat)
		lat_deg = int(lat_abs)
		lat_min = (lat_abs % 1) * 60
		return "%i%.2f%c" % (lat_deg, lat_min, lat_dir)

	def encode_lng(lng):
		lng_dir = 'E' if lng > 0 else 'W'
		lng_abs = abs(lng)
		lng_deg = int(lng_abs)
		lng_min = (lng_abs % 1) * 60
		return "%03i%.2f%c" % (lng_deg, lng_min, lng_dir)

	pos = "%s/%s" % (encode_lat(lat), encode_lng(lng))
	payload = "=%s%s %s" % (pos, symbol, comment)
	return "%s>APRS,TCPIP*:%s" % (callsign, payload)
