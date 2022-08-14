import pyttsx3
import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,960)
# text_speech=pyttsx3.init()
# rate=text_speech.setProperty("rate",120)
# #volume=text_speech.setProperty("volume",0.5)#max=1,min=0
# voices=text_speech.getProperty("voices")
# voices=text_speech.setProperty("voice", voices[1].id)#male=0,female=1

# answer=input("insert text:")
# text_speech.say(answer)
# text_speech.runAndWait()

def curl_counter(goal_curls):
    # Curl counter variables
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            # Recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #converting BGR to RGB so that it becomes easier for library to read the image
            image.flags.writeable = False #this step is done to save some memoery
            results = pose.process(image) #We are using the pose estimation model 
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            # Extract landmarks
            try:
                landmarks = results.pose_landmarks.landmark
                
                # Get coordinates
                shoulder_l = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                elbow_l = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                wrist_l = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                # Calculate angle
                angle = calculate_angle(shoulder_l, elbow_l, wrist_l)
                
                
                # Get coordinates of right hand
                shoulder_r = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                elbow_r = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                wrist_r = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
                # Calculate angle
                angle_r = calculate_angle(shoulder_r, elbow_r, wrist_r)
                
                # Visualize angle
                cv2.putText(image, str(angle),
                            tuple(np.multiply(elbow_l, [640, 480]).astype(int)), 
                            cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                
                # Curl counter logic for left
                if angle > 160:
                    stage = "Down"
                if angle < 30 and stage =='Down':
                    stage="Up"
                    counter +=1

                # Curl counter logic for right
                if angle_r > 160:
                    stage_r = "Down"
                if angle_r < 30 and stage_r =='Down':
                    stage_r="Up"
                    counter_r +=1                      
            
            except:
                pass
            
            cv2.rectangle(image, (440,0), (840,60), (0,0,0), -1)
            cv2.putText(image, 'BICEP CURLS', (460,40), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255,255,255), 1, cv2.LINE_AA)

            # Render curl counter for right hand
            # Setup status box for right hand
            cv2.rectangle(image, (0,0), (70,80), (0,0,0), -1)
            # cv2.rectangle(image, (0,35), (220,80), (245,117,16), -1)
            cv2.rectangle(image, (75,0), (220,80), (0,0,0), -1)
            # Rep data
            cv2.putText(image, 'REPS', (5,25), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1, cv2.LINE_AA)
            cv2.putText(image, str(counter_r), (10,65), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255,255,255), 1, cv2.LINE_AA)
            # Stage data
            cv2.putText(image, 'STAGE', (80,25), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1, cv2.LINE_AA)
            cv2.putText(image, stage_r, (80,65), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255,255,255), 1, cv2.LINE_AA)
            
            
            # Render curl counter for left hand
            # Setup status box for left 
            cv2.rectangle(image, (1280-220,0), (1280-150,80), (0,0,0), -1)
            # cv2.rectangle(image, (0,35), (220,80), (245,117,16), -1)
            cv2.rectangle(image, (1280-145,0), (1280,80), (0,0,0), -1)
            # Rep data
            cv2.putText(image, 'REPS', (1280-220+5,25), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1, cv2.LINE_AA)
            cv2.putText(image, str(counter), (1280-220+10,65), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255,255,255), 1, cv2.LINE_AA)
            # Stage data
            cv2.putText(image, 'STAGE', (1280-220+80,25), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 1, cv2.LINE_AA)
            cv2.putText(image, stage, (1280-220+80,65), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255,255,255), 1, cv2.LINE_AA)
            
            #for the instructor
            cv2.rectangle(image, (730,960-60), (1280,960), (0,0,0), -1)
            if counter > counter_r:
                cv2.putText(image, 'Do Left arm next', (750,960-15), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255,255,255), 2, cv2.LINE_AA)
                readSpeech = "left arm"
                text_speech.runAndWait()
            elif counter_r > counter:
                cv2.putText(image, 'Do Right arm next', (750,960-15), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255,255,255), 2, cv2.LINE_AA)
                readSpeech = "right arm"
                text_speech.runAndWait()
            elif counter == inputGoal and counter_r == inputGoal:
                cv2.putText(image, 'GOOD JOB', (540,960-60), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0), 2, cv2.LINE_AA)
                
            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                    mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                    )               
                
            cv2.imshow('CURL COUNTER', image)

            if int(counter) >= int(inputGoal) and int(counter_r) >= int(inputGoal):
                break

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    cv2.destroyAllWindows()