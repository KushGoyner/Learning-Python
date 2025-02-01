from os import system

names = ["kush","love","shyam","muskan","amit","tejender"]

for name in names:
    system(f'powershell -Command "Add-Type -AssemblyName System.Speech; '
          f'$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; '
          f'$speak.Speak(\\"shout out to {name}\\")"')
    
