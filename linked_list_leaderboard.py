# https://www.programiz.com/dsa/linked-list-operations
# for linked list operations
class Player:
    def __init__(self, name, points, wins):
        self.name = name
        self.points = points
        self.wins = wins
        self.next = None


class Leaderboard:

    def __init__(self):
        self.head = None

    # Sort the leaderboard by player names in alphabetical order
    def sort_by_name(self):
        if self.head is None:
            return

        # Convert the linked list to a list of players
        players = []
        current = self.head
        while current is not None:
            players.append(current)
            current = current.next

        # Sort the list by player names
        players.sort(key=lambda player: player.name)

        # Reconstruct the linked list
        self.head = players[0]
        current = self.head
        for i in range(1, len(players)):
            current.next = players[i]
            current = current.next
        current.next = None

    # Sort the leaderboard by player points in descending order
    def sort_by_points(self):
        if self.head is None:
            return

        # Convert the linked list to a list of players
        players = []
        current = self.head
        while current is not None:
            players.append(current)
            current = current.next

        # Sort the list by player points (in descending order)
        players.sort(key=lambda player: player.points, reverse=True)

        # Reconstruct the linked list
        self.head = players[0]
        current = self.head
        for i in range(1, len(players)):
            current.next = players[i]
            current = current.next
        current.next = None

    # Sort the leaderboard by player wins in descending order
    def sort_by_wins(self):
        if self.head is None:
            return

        # Convert the linked list to a list of players
        players = []
        current = self.head
        while current is not None:
            players.append(current)
            current = current.next

        # Sort the list by player wins (in descending order)
        players.sort(key=lambda player: player.wins, reverse=True)

        # Reconstruct the linked list
        self.head = players[0]
        current = self.head
        for i in range(1, len(players)):
            current.next = players[i]
            current = current.next
        current.next = None

    # Search an element
    def search(self, key):
        current = self.head
        while current is not None:
            if current.title == key:
                return True
            current = current.next
        return False

    # Print the leaderboard
    def print_leaderboard(self):
        current = self.head
        while current is not None:
            print("[", current.name, "-", current.points, "-", current.wins, "]", end=" ")
            current = current.next
        print()

if __name__ == '__main__':

    leaderboard = Leaderboard()
    player1 = Player("Alice", 1000, 5)
    player2 = Player("Bob", 800, 3)
    player3 = Player("Charlie", 1200, 7)
    player4 = Player("Jack", 1100, 5)

    leaderboard.head = player1
    leaderboard.head.next = player2
    player2.next = player3
    player3.next = player4

    print("Leaderboard default:")
    leaderboard.print_leaderboard()

    # Sort and print the leaderboard by name
    leaderboard.sort_by_name()
    print("Leaderboard sorted by name:")
    leaderboard.print_leaderboard()

    # Sort and print the leaderboard by points
    leaderboard.sort_by_points()
    print("Leaderboard sorted by points:")
    leaderboard.print_leaderboard()

    # Sort and print the leaderboard by wins
    leaderboard.sort_by_wins()
    print("Leaderboard sorted by wins:")
    leaderboard.print_leaderboard()