import cv2
from fer import FER
import pygame
import os
import random
import time
import pyttsx3

# Initialize emotion detector
detector = FER(mtcnn=True)  # Use mtcnn=True for better face detection

# Init music and text-to-speech
pygame.mixer.init()
engine = pyttsx3.init()

# Emotion color map
emotion_colors = {
    'angry': (0, 0, 255),
    'fear': (255, 0, 255),
    'happy': (0, 255, 255),
    'sad': (255, 0, 0),
    'surprise': (255, 255, 0),
    'neutral': (128, 128, 128)
}

# State variables
current_emotion = ""
song_name = "None"
lock_duration = 10  # 10 seconds before next emotion scan
last_play_time = 0
scan_delay = 3
face_detected_time = 0
song_started_time = None

def speak(text):
    engine.say(text)
    engine.runAndWait()

def play_music(emotion):
    folder = f'music/{emotion.lower()}'
    if os.path.exists(folder):
        songs = os.listdir(folder)
        if songs:
            song = random.choice(songs)
            pygame.mixer.music.load(os.path.join(folder, song))
            pygame.mixer.music.play()
            print(f"🎵 Playing: {song}")
            return song
    return "No music found"

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    current_time = time.time()
    time_left = max(0, int(lock_duration - (current_time - last_play_time)))

    # Stop music after 10 seconds
    if song_started_time and time.time() - song_started_time >= 10:
        pygame.mixer.music.stop()
        song_name = "None"
        song_started_time = None

    # FER detection (only if song not playing and cooldown over)
    if time_left == 0 and not pygame.mixer.music.get_busy():
        if face_detected_time == 0:
            face_detected_time = current_time

        elapsed = current_time - face_detected_time

        if elapsed >= scan_delay:
            result = detector.detect_emotions(frame)
            if result:
                face_data = result[0]
                emotions = face_data["emotions"]
                top_emotion = max(emotions, key=emotions.get)

                current_emotion = top_emotion.lower()
                color = emotion_colors.get(current_emotion, (255, 255, 255))

                speak(f"You look {current_emotion}")
                song_name = play_music(current_emotion)
                last_play_time = time.time()
                song_started_time = time.time()
                face_detected_time = 0
        else:
            cv2.putText(frame, f"Scanning... ({int(scan_delay - elapsed)}s)", (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100, 100, 255), 2)
    else:
        face_detected_time = 0

    # Show now playing
    cv2.putText(frame, f"Now Playing: {song_name}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    # Mood box while playing
    if current_emotion and song_started_time:
        color = emotion_colors.get(current_emotion, (255, 255, 255))
        cv2.rectangle(frame, (10, 60), (300, 110), color, -1)
        cv2.putText(frame, f"{current_emotion.title()}", (20, 95),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    # Cooldown timer
    if time_left > 0:
        cv2.putText(frame, f"Next Emotion Scan in: {time_left}s", (10, 140),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.imshow("Emotion-Aware Music Player (FER)", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
pygame.mixer.music.stop()
cv2.destroyAllWindows()
