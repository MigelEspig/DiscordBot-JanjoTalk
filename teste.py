from gtts import gTTS

VoiceText = "Paulo merece o sofrimento eterno ponto vírgula parágrafo"
voice = gTTS(text = VoiceText, lang="pt-br")
voice.save("Sounds/TextoFalado.mp3")
print("Audio gerado!!!!")