import pandas as pd
import numpy as np
import cv2

LABELS = [
    "JUMPING",
    "JUMPING_JACKS",
    "BOXING",
    "WAVING_2HANDS",
    "WAVING_1HAND",
    "CLAPPING_HANDS"]
POSE_COCO_BODY_PARTS = {
    0: "Nose",
    1: "Neck",
    2: "RShoulder",
    3: "RElbow",
    4: "RWrist",
    5: "LShoulder",
    6: "LElbow",
    7: "LWrist",
    8: "RHip",
    9: "RKnee",
    10: "RAnkle",
    11: "LHip",
    12: "LKnee",
    13: "LAnkle",
    14: "REye",
    15: "LEye",
    16: "REar",
    17: "LEar",
    18: "Bkg",
}
POSE_COCO_PAIRS = (1, 2,   1, 5,   2, 3,   3, 4,   5, 6,   6, 7,   1, 8,   8,
                   9,   9, 10, 1, 11,  11, 12, 12, 13,  1, 0,   0, 14, 14, 16,  0, 15, 15, 17)

sequence_length = 32

column_names = ["j0_x",  "j0_y", "j1_x", "j1_y", "j2_x", "j2_y", "j3_x", "j3_y", "j4_x", "j4_y", "j5_x", "j5_y", "j6_x", "j6_y", "j7_x", "j7_y", "j8_x", "j8_y",
                "j9_x", "j9_y", "j10_x", "j10_y", "j11_x", "j11_y", "j12_x", "j12_y", "j13_x", "j13_y", 'j14_x', "j14_y", "j15_x", "j15_y", "j16_x", "j16_y", "j17_x", "j17_y"]


DATASET_PATH = "poses/"

# X_train_path = DATASET_PATH + "X_train.txt"
# X_test_path = DATASET_PATH + "X_test.txt"

# y_train_path = DATASET_PATH + "Y_train.txt"
# y_test_path = DATASET_PATH + "Y_test.txt"

# x_train = pd.read_csv(X_train_path, sep=",", names=column_names, header=None, dtype=np.float32)
# x_test = pd.read_csv(X_test_path, sep=",", names=column_names, header=None, dtype=np.float32)
# y_train = pd.read_csv(y_train_path, names=["labels"], dtype=np.int_)
# y_test = pd.read_csv(y_test_path, names=["labels"], dtype=np.int_)

x_train_path = "shuffled_x_train_data.csv"
y_train_path = "shuffled_y_train_data.csv"
x_test_path = "shuffled_x_test_data.csv"
y_test_path = "shuffled_y_test_data.csv"

x_train = pd.read_csv(x_train_path, sep="\t", dtype=np.float32)
x_test = pd.read_csv(x_test_path, sep="\t", dtype=np.float32)
y_train = pd.read_csv(y_train_path, sep="\t", dtype=np.int_)
y_test = pd.read_csv(y_test_path, sep="\t", dtype=np.int_)


def chunker(x_seq, y_seq, seq_size):
    for i, index in enumerate(range(0, len(x_seq), seq_size)):
        yield x_seq.iloc[index:index + seq_size].values, y_seq.iloc[i].values


def unnormalize(data):
    for i, column in enumerate(data):
        if i % 2 == 0:
            data[column] = data[column] * 640
        else:
            data[column] = data[column] * 480
    return data


unnormalize(x_test)
unnormalize(x_train)

if __name__ == "__main__":
    out = cv2.VideoWriter(
        "poses_train.mp4", cv2.VideoWriter_fourcc(*'DIVX'), 30, (640, 480))
    for index, (poses, label) in enumerate(chunker(x_train, y_train, sequence_length)):
        if index % 300 == 0:
            print(index)
        # if index > 10:
        #     break
        for pose in poses:
            img = np.zeros((480, 640, 3), np.uint8)
            cv2.putText(img, LABELS[int(label)], (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
            for i in range(0, len(pose), 2):
                point = (int(pose[i]), int(pose[i+1]))
                if (point[0] == 0 and point[1] == 0):
                    continue
                img = cv2.circle(img, point, radius=2,
                                 color=(0, 0, 255), thickness=-1)

            for i in range(0, len(POSE_COCO_PAIRS), 2):
                keypoint_1 = POSE_COCO_PAIRS[i]
                keypoint_2 = POSE_COCO_PAIRS[i+1]
                x = (int(pose[2*keypoint_1]), int(pose[2*keypoint_1+1]))
                y = (int(pose[2*keypoint_2]),
                     int(pose[2*keypoint_2+1]))
                if ((x[0] == 0 and x[1] == 0) or (y[0] == 0 and y[1] == 0)):
                    continue
                cv2.line(img, x, y, (0, 255, 0), thickness=2)
            # cv2.imshow("l", img)
            # cv2.waitKey(0)
            out.write(img)
    out.release()
