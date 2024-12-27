import cv2
import mediapipe as mp
import time
from scipy.spatial import distance

def detect_blinks():
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )

    cap = cv2.VideoCapture(0)
    
 
    BLINK_THRESHOLD = 7.0  
    CONSECUTIVE_FRAMES = 2
    
    counter = 0
    total_blinks = 0
    start_time = time.time()
    
    LEFT_EYE_UPPER = 386  # Upper eyelid
    LEFT_EYE_LOWER = 374  # Lower eyelid
    RIGHT_EYE_UPPER = 159  # Upper eyelid
    RIGHT_EYE_LOWER = 145  # Lower eyelid

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Failed to capture frame")
            break

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = face_mesh.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_face_landmarks:
            face_landmarks = results.multi_face_landmarks[0]
            
    
            left_upper = (int(face_landmarks.landmark[LEFT_EYE_UPPER].x * image.shape[1]),
                         int(face_landmarks.landmark[LEFT_EYE_UPPER].y * image.shape[0]))
            left_lower = (int(face_landmarks.landmark[LEFT_EYE_LOWER].x * image.shape[1]),
                         int(face_landmarks.landmark[LEFT_EYE_LOWER].y * image.shape[0]))
            right_upper = (int(face_landmarks.landmark[RIGHT_EYE_UPPER].x * image.shape[1]),
                          int(face_landmarks.landmark[RIGHT_EYE_UPPER].y * image.shape[0]))
            right_lower = (int(face_landmarks.landmark[RIGHT_EYE_LOWER].x * image.shape[1]),
                          int(face_landmarks.landmark[RIGHT_EYE_LOWER].y * image.shape[0]))

        
            left_distance = distance.euclidean(left_upper, left_lower)
            right_distance = distance.euclidean(right_upper, right_lower)
            avg_distance = (left_distance + right_distance) / 2

            
            if avg_distance < BLINK_THRESHOLD:
                counter += 1
            else:
                if counter >= CONSECUTIVE_FRAMES:
                    total_blinks += 1
                counter = 0

            
            for point in [left_upper, left_lower, right_upper, right_lower]:
                cv2.circle(image, point, 2, (0, 255, 0), -1)
            
          
            cv2.putText(image, f"Distance: {avg_distance:.2f}", (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        
        elapsed_time = int(time.time() - start_time)
        cv2.putText(image, f"Blinks: {total_blinks}", (10, 60),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(image, f"Time: {elapsed_time}s", (10, 90),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

       
        cv2.imshow('Eye Blink Detection', image)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_blinks()