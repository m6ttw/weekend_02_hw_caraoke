class Room:
    
    def __init__(self, name):
        self.name = name
        self.guests = []
        self.songs = []


    def check_in_guest(self, guest):
        self.guests.append(guest)


    def check_out_guest(self, guest):
        for guest in self.guests:
            if len(self.guests) >= 1:
                self.guests.remove(guest)


    def guest_count(self):
        return len(self.guests) 


    def add_song_to_room(self, song):
        self.songs.append(song)


    def song_count(self):
        return len(self.songs)
