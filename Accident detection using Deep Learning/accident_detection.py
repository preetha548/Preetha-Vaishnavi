
import cv2
import csv
import os
from datetime import datetime
from ultralytics import YOLO

# ==========================================
# CAR ACCIDENT DETECTION USING DEEP LEARNING
# ==========================================

VIDEO_PATH = "clip_01.mp4"
OUTPUT_VIDEO = "accident_output.mp4"
OUTPUT_CSV = "accident_log.csv"

# Load YOLO11 deep learning model
print("Loading Deep Learning Model...")
model = YOLO("yolo11n.pt")

# Vehicle classes: car, motorcycle, bus, truck
VEHICLE_CLASSES = [2, 3, 5, 7]

# Check input video
if not os.path.exists(VIDEO_PATH):
    print("Video file not found:", VIDEO_PATH)
    raise SystemExit

cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print("Unable to open video!")
    raise SystemExit

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

if fps <= 0:
    fps = 25

# Create output video
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

out = cv2.VideoWriter(
    OUTPUT_VIDEO,
    fourcc,
    fps,
    (width, height)
)

# Accident records
accident_records = []
overlap_count = {}
reported_pairs = set()

frame_number = 0

print("Starting Accident Detection...")
print("Press Q to stop.")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame_number += 1

    # Vehicle detection and tracking
    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml",
        classes=VEHICLE_CLASSES,
        conf=0.35,
        verbose=False
    )

    vehicles = []

    boxes = results[0].boxes

    if boxes is not None:

        for box in boxes:

            x1, y1, x2, y2 = map(
                int, box.xyxy[0].tolist()
            )

            class_id = int(box.cls[0])

            if box.id is None:
                continue

            track_id = int(box.id[0])
            vehicle_name = model.names[class_id]

            vehicles.append({
                "id": track_id,
                "box": (x1, y1, x2, y2)
            })

            # Draw vehicle bounding box
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                vehicle_name + " ID:" + str(track_id),
                (x1, max(y1 - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    # ======================================
    # POSSIBLE COLLISION DETECTION
    # ======================================

    for i in range(len(vehicles)):

        for j in range(i + 1, len(vehicles)):

            v1 = vehicles[i]
            v2 = vehicles[j]

            id1 = v1["id"]
            id2 = v2["id"]

            x1, y1, x2, y2 = v1["box"]
            a1, b1, a2, b2 = v2["box"]

            # Calculate overlapping area
            ix1 = max(x1, a1)
            iy1 = max(y1, b1)
            ix2 = min(x2, a2)
            iy2 = min(y2, b2)

            intersection = (
                max(0, ix2 - ix1) *
                max(0, iy2 - iy1)
            )

            area1 = max(1, (x2 - x1) * (y2 - y1))
            area2 = max(1, (a2 - a1) * (b2 - b1))

            overlap = intersection / min(area1, area2)

            pair = tuple(sorted((id1, id2)))

            if overlap > 0.30:
                overlap_count[pair] = (
                    overlap_count.get(pair, 0) + 1
                )
            else:
                overlap_count[pair] = 0

            # Flag overlap lasting 5 consecutive frames
            if overlap_count[pair] >= 5:

                # Save only one record per vehicle pair
                if pair not in reported_pairs:

                    reported_pairs.add(pair)

                    accident_records.append([
                        len(accident_records) + 1,
                        frame_number,
                        round(frame_number / fps, 2),
                        id1,
                        id2,
                        "Possible Collision",
                        datetime.now().strftime(
                            "%Y-%m-%d %H:%M:%S"
                        )
                    ])

                # Draw warning
                cv2.rectangle(
                    frame,
                    (ix1, iy1),
                    (ix2, iy2),
                    (0, 0, 255),
                    3
                )

                cv2.putText(
                    frame,
                    "POSSIBLE ACCIDENT!",
                    (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    3
                )

    # Display project title
    cv2.putText(
        frame,
        "CAR ACCIDENT DETECTION",
        (20, height - 25),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    # Save processed frame
    out.write(frame)

    # Display video
    cv2.imshow("Accident Detection System", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# ======================================
# SAVE ACCIDENT CSV REPORT
# ======================================

with open(OUTPUT_CSV, "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "S.No",
        "Frame Number",
        "Time in Seconds",
        "Vehicle ID 1",
        "Vehicle ID 2",
        "Detection Result",
        "Date and Time"
    ])

    writer.writerows(accident_records)

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print("\n================================")
print("ACCIDENT DETECTION COMPLETED")
print("================================")
print("Input Video:", VIDEO_PATH)
print("Output Video:", OUTPUT_VIDEO)
print("Accident Report:", OUTPUT_CSV)
print("Possible Collisions:", len(accident_records))
