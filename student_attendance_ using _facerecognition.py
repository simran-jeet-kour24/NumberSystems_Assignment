import cv2
import numpy as np
import os
import pandas as pd
from datetime import datetime

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# ---------------- FACE DETECTION ----------------
def detect_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return faces


# ---------------- GENERATE DATASET ----------------
def generate_dataset():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Camera not detected!")
        return

    user_id = input("Enter student ID (number only): ")
    name = input("Enter student Name: ")

    if not user_id.isdigit():
        print("❌ ID must be numeric!")
        return

    os.makedirs(f"dataset/{user_id}", exist_ok=True)

    # Create labels.csv if not exists
    if not os.path.exists("labels.csv"):
        pd.DataFrame(columns=["ID", "Name"]).to_csv("labels.csv", index=False)

    labels = pd.read_csv("labels.csv")

    if int(user_id) not in labels["ID"].values:
        labels.loc[len(labels)] = [int(user_id), name]
        labels.to_csv("labels.csv", index=False)

    sampleNum = 0
    print("📸 Look at camera... Press Q to stop early.")

    while True:
        ret, img = cap.read()
        if not ret:
            break

        faces = detect_face(img)

        for (x, y, w, h) in faces:
            sampleNum += 1
            face_img = img[y:y+h, x:x+w]
            cv2.imwrite(f"dataset/{user_id}/{sampleNum}.jpg", face_img)

            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(img, f"Samples: {sampleNum}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Generating Dataset", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if sampleNum >= 30:
            print("✅ 30 samples collected.")
            break

    cap.release()
    cv2.destroyAllWindows()
    print("✅ Dataset Generation Completed!")


# ---------------- TRAIN MODEL ----------------
def train_model():
    if not os.path.exists("dataset"):
        print("❌ Dataset folder not found!")
        return

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    faces = []
    ids = []

    for root, dirs, files in os.walk("dataset"):
        for file in files:
            path = os.path.join(root, file)
            gray_img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

            if gray_img is None:
                continue

            user_id = int(os.path.basename(root))
            faces.append(gray_img)
            ids.append(user_id)

    if len(faces) == 0:
        print("❌ No images found in dataset!")
        return

    recognizer.train(faces, np.array(ids))
    recognizer.save("face_trainer.yml")

    print("✅ Model Trained Successfully!")


# ---------------- MARK ATTENDANCE ----------------
def mark_attendance(name):
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    if not os.path.exists("attendance.csv"):
        pd.DataFrame(columns=["Name", "Date", "Time", "Status"]).to_csv("attendance.csv", index=False)

    df = pd.read_csv("attendance.csv")

    if not ((df["Name"] == name) & (df["Date"] == date)).any():
        df.loc[len(df)] = [name, date, time, "Present"]
        df.to_csv("attendance.csv", index=False)
        print(f"✅ Attendance marked for {name}")
    else:
        print(f"ℹ {name} already marked today")


# ---------------- START ATTENDANCE ----------------
def attendance():
    if not os.path.exists("face_trainer.yml"):
        print("❌ Please train the model first (Option 2)")
        return

    if not os.path.exists("labels.csv"):
        print("❌ labels.csv not found. Generate dataset first (Option 1)")
        return

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("face_trainer.yml")

    labels = pd.read_csv("labels.csv")
    id_name = dict(zip(labels["ID"], labels["Name"]))

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Camera not detected!")
        return

    print("🎥 Attendance Started... Press Q to Exit")

    while True:
        ret, img = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detect_face(img)

        for (x, y, w, h) in faces:
            face_gray = gray[y:y+h, x:x+w]
            user_id, confidence = recognizer.predict(face_gray)

            if confidence < 60:
                name = id_name.get(user_id, "Unknown")
                mark_attendance(name)
            else:
                name = "Unknown"

            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(img, name, (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                        (0, 255, 0), 2)

        cv2.imshow("Attendance System", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("✅ Attendance Stopped")


# ---------------- MAIN MENU ----------------
if __name__ == "__main__":
    print("\n====== FACE RECOGNITION ATTENDANCE SYSTEM ======")
    print("1. Generate Dataset")
    print("2. Train Model")
    print("3. Start Attendance")

    choice = input("Enter choice: ")

    if choice == "1":
        generate_dataset()
    elif choice == "2":
        train_model()
    elif choice == "3":
        attendance()
    else:
        print("❌ Invalid choice")