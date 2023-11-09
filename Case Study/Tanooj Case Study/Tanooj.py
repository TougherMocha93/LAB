import cv2
import numpy as np
from sklearn.svm import SVC
from sklearn.decomposition import PCA

# Function to collect training data - replace this with your actual data collection method
def collect_training_data():
    # Load or collect training images and labels
    return images, labels

# Function to perform face recognition
def recognize_faces(classifier, pca_transformer):
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            face_roi = gray[y:y+h, x:x+w]
            resized = cv2.resize(face_roi, (100, 100))  # Resize the face region

            # Perform PCA transformation on the detected face
            flattened = resized.flatten()
            pca_data = pca_transformer.transform([flattened])

            # Perform face recognition using the classifier
            predicted_label = classifier.predict(pca_data)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, str(predicted_label), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        cv2.imshow('Face Recognition', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    images, labels = collect_training_data()
    data = np.array(images)

    # Flatten images
    num_samples, height, width = data.shape
    data = data.reshape((num_samples, height * width))

    # Perform PCA
    num_components = 100
    pca_transformer = PCA(n_components=num_components)
    reduced_data = pca_transformer.fit_transform(data)

    # Train a basic classifier (SVM in this case)
    classifier = SVC(kernel='linear')
    classifier.fit(reduced_data, labels)

    recognize_faces(classifier, pca_transformer)