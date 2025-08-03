import cv2

def main():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open camera")
        return
    
    print("Press 'q' to quit")
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Could not read frame")
            break
        
        cv2.imshow('Camera Stream', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()