class Town:
    def __init__(self, name):
        self.name = name
        self.latitude = ""
        self.longitude = ""

    def set_latitude(self, latitude):
        self.latitude = latitude
        return self.latitude

    def set_longitude(self, longitude):
        self.longitude = longitude
        return self.longitude

    def __repr__(self):
        result = f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"
        return result


town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)
