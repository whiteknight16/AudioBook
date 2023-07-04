from PyPDF2 import PdfReader
import pyttsx3
import os


engine = pyttsx3.init()

file_path = input('Enter a file path of PDF: ')
print(file_path)

if os.path.exists(file_path):
    print('The file exists')
    reader = PdfReader(file_path)
    print(f"Total pages {len(reader.pages)}")
    start = int(input("Enter the  starting page:"))
    end = int(input("Enter the page till which you want to read:"))
    if end > len(reader.pages):
        end = reader.pages
    print(f"Reading from {start} till {end}.........")
    print("Converting text to audio.....")
    print("Playing")
    for i in range(start-1, end):
        page = reader.pages[i]
        text = page.extract_text()
        engine.say(text)
        engine.runAndWait()

else:
    print('The specified file does NOT exist')
