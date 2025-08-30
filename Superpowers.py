import time


def animate_line(text, delay=0.08):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

lyrics = [

    
    ("\033[36mOoh, you got power\033[0m", 0),
    ("\033[36mSuperpowers\033[0m", 4.7),
    ("\033[36mDo you even know how to wield them?\033[0m", 8),
    ("\033[36mAll God's children\033[0m", 12.5),
    ("\033[36mAre Special\033[0m", 15.7),
    ("\033[36mBut not like you\033[0m", 18.2),
    ("\033[36mNo, not like you\033[0m", 20.8),
    ("", 4.0),

    ("\033[35mYou're just like flower(flower)\033[0m", 24),
    ("\033[35mYou're ever-giving\033[0m", 28.5),
    ("\033[35mThat's a given\033[0m", 33.3),
    ("\033[35mAll God's children\033[0m", 36.2),
    ("\033[35mare special\033[0m", 39.8),
    ("\033[35mBut not like you,'\033[0m", 42.3),
    ("\033[35mno, not like you\033[0m", 45),
    ("\033[35mLift your head to the sky (to the sky, oh sky, sky)\033[0m", 50.5),
    ("\033[35m-\033[0m", 100),
        
    ]

start_time = time.time()
for line, lyric_time in lyrics:
    while time.time() - start_time < lyric_time:
        time.sleep(0.1)
    animate_line(line, delay=0.08)
