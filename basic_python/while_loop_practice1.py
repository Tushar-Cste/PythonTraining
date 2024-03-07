# While loop practice with car game
# There should be an input field
# If we type help (lower or upper) it should the following text
# start - to start the car
# stop - to stop the car
# quit - to exit
# If we type start (lower or upper) it should show the following message
# Car started... Ready to go
# If we type stop after the start it should show the following message
# Car stopped
# If we type quit anytime it should termiate the program
# If we type start after typing the start it will show the following message
# Car is already started
# If we type stop before starting the car it will show the following message
# Car is already stopped.
# For any other input show the following message:
# Don't recognize the command

is_started = False

while True:
    input_val = input().lower()
    if input_val.lower() == 'help':
        val = '''
start - to start the car
stop - to stop the car
quit - to exit
        '''
        print(val)
    if input_val == 'start' and is_started:
        print('Car is already started.')
    elif input_val == 'start':
        is_started = True
        print('Car started... Ready to go')
    elif input_val == 'stop' and is_started:
        is_started = False
        print('Car stopped')
    elif input_val == 'stop':
        print('Car is already stopped.')
    elif input_val == 'quit':
        break
    else:
        print("Don't recognize the command.")

print('Game Over...')

