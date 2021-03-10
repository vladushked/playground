import pandas as pd
import cv2 as cv

LABELS = [    
    "JUMPING",
    "JUMPING_JACKS",
    "BOXING",
    "WAVING_2HANDS",
    "WAVING_1HAND",
    "CLAPPING_HANDS"] 

DATASET_PATH = "poses/"

X_test_path = DATASET_PATH + "X_train.txt"
X_test_path = DATASET_PATH + "X_test.txt"

y_test_path = DATASET_PATH + "Y_train.txt"
y_test_path = DATASET_PATH + "Y_test.txt"

column_names = [  "j0_x",  "j0_y", "j1_x", "j1_y" , "j2_x", "j2_y", "j3_x", "j3_y", "j4_x", "j4_y", "j5_x", "j5_y", "j6_x", "j6_y", "j7_x", "j7_y", "j8_x", "j8_y", "j9_x", "j9_y", "j10_x", "j10_y", "j11_x", "j11_y", "j12_x", "j12_y", "j13_x", "j13_y", 'j14_x', "j14_y", "j15_x", "j15_y", "j16_x", "j16_y", "j17_x", "j17_y" ]
x_train_data = pd.read_csv(X_train_path, sep=",", names=column_names, header=None, dtype=np.float32)
x_test_data = pd.read_csv(X_test_path, sep=",", names=column_names, header=None, dtype=np.float32)
y_train_data = p|d.read_csv(y_train_path, names=["labels"], dtype=np.int_)
y_test_data = pd.read_csv(y_test_path, names=["labels"], dtype=np.int_)

def chunker(x_seq, y_seq, seq_size):
    for batch_pos in range(0, len(x_seq), seq_size):
        x_batch(x_seq.iloc[pos*seq_size:pos*seq_size + seq_size].values)
        
        yield x_seq.iloc[pos*seq_size:pos*seq_size + seq_size].values, y_seq.iloc[batch_pos:batch_pos + batch_size].values


if __name__ == "__main__":
    out = cv.VideoWriter(name, cv.VideoWriter_fourcc(*'DIVX'), 30, size)
    for i, (x_batch, y_batch) in enumerate(chunker(x_train, y_train, sequence_length, 1)):
        for fname in walk_through_files(path):
            img = cv2.imread(fname)
            img = cv2.resize(img, size)
            out.write(img)
    out.release()