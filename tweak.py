import os
accuracy = os.system("cat /taskCode/accuracy.txt")
x = 'model.add(Dense(units=32, activation=\"relu\"))'
if accuracy < 97:
    os.system("sed -i '/softmax/ i {}' /taskCode/train.py".format(x))
else:
    print("Accuracy achieved !!!")
    exit()
