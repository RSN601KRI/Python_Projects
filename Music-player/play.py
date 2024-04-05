import pygame
import os

def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

def main():
    print("Welcome to the Python Music Player!")
    file_path = input("Enter the path to the music file: ")

    # Check if the file exists
    if not os.path.exists(file_path):
        print("File not found.")
        return

    play_music(file_path)

    while True:
        print("\nOptions:")
        print("1. Pause")
        print("2. Unpause")
        print("3. Stop")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            pause_music()
        elif choice == "2":
            unpause_music()
        elif choice == "3":
            stop_music()
        elif choice == "4":
            print("Exiting the Python Music Player. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
