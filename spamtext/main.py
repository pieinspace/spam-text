import pyautogui as spam
import time

message = input("mau chat apa : ")

count = 0
limit = int(input("mau berapa : "))

print("bakal ngespam dalam waktu:")
for i in range(7, 0, -1): 
    print(f"\r{i}", end="", flush=True) 
    time.sleep(1)

print("\n") 
time.sleep(2) 

while count < int(limit):
    count += 1
    if count > limit:
        break
    spam.typewrite(message)
    spam.press("enter")