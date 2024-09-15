## Question Answers

# Exercise 1
1. What are the "max_bright" and "min_bright" values you found?

The max_bright value I found when I shined a flashlight on the light sensor was on average 1300.
The min_bright value I found when I put my hand over the light sensor was 50000. 

# Exercise 2

1. Using the code in exercise_sound.py as a starting point, modify the code to play several notes in a sequence from a song of your choosing.

I added notes and frequencies for those notes in exercise_sound.py

# Exercise 3
I implemented the required calculations to obtain data for the game. I then decided to use Firebase and a Real-Time database as my cloud service to upload the data to. I obtained my Firebase URL and had the pico send a HTTP Post request to the URL. I also made sure to connect the Pico to the network so this request can be completed. I did this in the connect_wifi function to check if the network is connect and if not to connect to the wifi I am currently using. 

Below is a video of the whole process and the data being sent to Firebase (I skipped the first part of the video and just showed the end becasue the video was too long):

https://github.com/user-attachments/assets/c5ccbc9a-2178-4508-82c2-e9bbd880e014




