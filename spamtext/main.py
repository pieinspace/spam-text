import pyautogui as spam
import time
from pynput import keyboard

print("Note: Click tombol 'Esc' untuk menghentikan proses kapan saja.")
print("\n")
message = input("Mau chat apa: ")

while True:
    try:
        limit = int(input("Mau berapa: "))
        if limit <= 0:
            print("Masukkan angka lebih dari 0!")
            continue
        break
    except ValueError:
        print("Masukkan angka yang bener!")

print("\n")
print("Bakal ngespam dalam waktu:")
for i in range(7, 0, -1):
    print(f"\r{i}", end="", flush=True)
    time.sleep(1)
print("\n")
print("\nMulai mengirim pesan...\n")

count = 0
stop_spam = False

def on_press(key):
    global stop_spam
    if key == keyboard.Key.esc:
        stop_spam = True
        return False 

listener = keyboard.Listener(on_press=on_press)
listener.start()

try:
    while count < limit:
        if stop_spam:
            print("\nProses dihentikan oleh pengguna.")
            break
        spam.typewrite(message)
        spam.press("enter")
        count += 1
        time.sleep(0)
    else:
        print("\nText sudah berhasil terkirim semua!")
except KeyboardInterrupt:
    print("\nProses dihentikan oleh pengguna.")
