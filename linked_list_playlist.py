class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next = None


class PlayList:

    def __init__(self):
        self.head = None

    # Search an element
    def search(self, key):
        current = self.head
        while current is not None:
            if current.title == key:
                return True
            current = current.next
        return False
    
if __name__ == '__main__':

    play_list = PlayList()
    song1 = Song("Song 1", "Artist 1")
    song2 = Song("Song 2", "Artist 2")
    song3 = Song("Song 3", "Artist 3")
    play_list.head = song1
    play_list.head.next = song2
    song2.next = song3
    
    item_to_find = "Song 1"
    if play_list.search(item_to_find):
        print(str(item_to_find) + " is found")
    else:
        print(str(item_to_find) + " is not found")

    # Print the linked list item
    while play_list.head is not None:
        print("[", play_list.head.artist, "-", play_list.head.title, "]", end=" ")
        play_list.head = play_list.head.next