# Write a program that works with this hotel data:
hotel = {
  '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
  },
  '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
  },
  '3': {
    '333': ['Neo', 'Trinity', 'Morpheus']
  }
}

# Display a menu asking whether to check in or check out.
def displayMenu():
    print()
    print(20 * '*')
    print('*                  *')
    print('*   1 - Check In   *')
    print('*   2 - Check Out  *')
    print('*   0 - Exit       *')
    print('*                  *')
    print(20 * '*')
    print()

# Prompt the user for a floor number, then a room number.
# If checking in, ask for the number of occupants and what their names are.
# If checking out, remove the occupants from that room.
# Do not allow anyone to check into a room that is already occupied.
# Do not allow checking out of a room that isn't occupied.

while True:
    displayMenu()
    choice = int(input("How may I help you? "))

    if choice == 0:
        break
print("\nHave a nice day!")
