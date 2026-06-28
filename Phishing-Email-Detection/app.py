import os

print("====================================")
print("   PHISHING EMAIL DETECTION MODEL")
print("====================================")

print("\n1. Train Model")
print("2. Predict Email")

choice = input("\nEnter Choice : ")

if choice == "1":
    os.system("cd src && python train.py")

elif choice == "2":
    os.system("cd src && python predict.py")

else:
    print("Invalid Choice")