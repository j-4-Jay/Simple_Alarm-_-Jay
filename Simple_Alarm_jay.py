import winsound
import time

#* Set the duration and frequency of the alarm sound
duration = 1000 # millisecond
frequency = 220 # Hz

#* Get the current time and desired alarm time
current_time = time.strftime("%H:%M:%S")
desired_time = input("Enter alarm time in 24Hr format: ")

#* Loop until the current time matches the alarm time
while current_time != desired_time:
    current_time = time.strftime("%H:%M:%S")
    time.sleep(1)

#* When the alarm time is reached, Play the alarm sound
winsound.Beep(frequency, duration)

# End of program....