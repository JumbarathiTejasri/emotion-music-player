
# 🎧 Emotion-Aware Music Player

This is a real-time **AI Music Player** that uses your webcam to detect your facial **emotion** and plays a song that matches your mood. It uses the **FER (Facial Emotion Recognition)** library and OpenCV.

---

## 💡 Features

- Detects emotions like **Happy**, **Sad**, **Angry**, **Fear**, **Surprise**, and **Neutral**.
- Plays songs based on detected emotion.
- Shows emotion label and background color during music playback.
- Automatically stops the song after 10 seconds.
- Cooldown timer: waits 10 seconds before scanning again.
- Voice feedback (e.g., "You look happy") using `pyttsx3`.

---

## 🛠️ Tech Stack

- Python 3.10+
- OpenCV (`cv2`)
- [FER](https://github.com/justinshenk/fer)
- Pygame
- pyttsx3 (Text-to-speech)

---

## 📁 Folder Structure

```
emotion-music-player/
│
├── music/
│   ├── happy/
│   ├── sad/
│   ├── angry/
│   ├── fear/
│   ├── neutral/
│   └── surprise/
├── main.py
├── README.md
└── requirements.txt
```

Each folder inside `music/` should contain relevant `.mp3` songs for that emotion.

---

## 🚀 How to Run (with venv)

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/emotion-music-player.git
cd emotion-music-player
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv .venv
# Activate:
.venv\Scripts\activate     # on Windows
source .venv/bin/activate  # on macOS/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
python main.py
```

---

## 📝 Requirements

```
opencv-python
pygame
pyttsx3
fer
moviepy
```

To generate `requirements.txt`:
```bash
pip freeze > requirements.txt
```

---

## 🧠 Emotion Mapping (Examples)

| Emotion    | Songs Folder       |
|------------|--------------------|
| Happy      | `music/happy/`     |
| Sad        | `music/sad/`       |
| Angry      | `music/angry/`     |
| Fear       | `music/fear/`      |
| Neutral    | `music/neutral/`   |
| Surprise   | `music/surprise/`  |

---

## 🖼️ Sample Output

- Webcam opens
- Waits for 3s scanning face
- Emotion detected: *"Happy"*
- Voice: _"You look happy"_
- Plays a happy song
- Displays song title and colored label

---

## 📌 Notes

- Webcam access is required.
- Use `.mp3` files for songs.
- Make sure song folders are correctly named and not empty.

---

## 🙌 Credits

- Facial Emotion Recognition – [FER Library](https://github.com/justinshenk/fer)
- Pygame for audio
- OpenCV for real-time webcam input

---

## 📃 License

This project is for educational use. Customize it for your personal or portfolio projects.

---
