import os
import sys
import config
from models import MobileNetClassifier
from utils import video_processor,preprocessing,visualization

def classify_video(video_path):
    if os.path.exists(video_path):
        print("the pathdoes not exist")
    return

    #extraction of frames
    frames,_=extract_frames(video_path,num_frames=NUM_FRAMES)

    #classify the object

    classifier=MobileNetClassifier()
    preprocessing=preprocess_batch(frames,target_size=config.INPUT_SIZE)
    predictions=classifier.predict(preprocessing)

    print("result summary")
    print_results_summary(predictions,len(frames))

if __name__='__main__':
    if len(sys.argv)<2:
        print("python inference")
        sys.exit(1)
    classify_video(sys.argv[1])