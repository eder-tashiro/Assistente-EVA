import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit

audio = sr.Recognizer()
maquina = pyttsx3.init()

def listen_command():
    comando = None
    try:
        with sr.Microphone() as source:
            print("Escutando.....")
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language="pt-BR")
            comando = comando.lower()
            if 'eva' in comando:
                comando = comando.replace('eva', '').strip()
                return comando
            elif 'sair' in comando:
                return 'sair'  # Retorna o comando de saída

    except Exception as e:
        print(f"Um erro inesperado ocorreu: {e}")
    
    return comando

def execute_command():
    print("Inicializando assistente Eva...")
    while True:
        comando = listen_command()
        if comando == 'sair':
            maquina.say("Encerrando o assistente Eva.")
            maquina.runAndWait()
            break  # Interrompe o loop e encerra o assistente
        elif comando:
            if 'procure por' in comando or 'pesquise por' in comando:
                procurar = comando.replace('procure por', '').replace('pesquise por', '').strip()
                wikipedia.set_lang('pt')
                resultado = wikipedia.summary(procurar, sentences=2)
                print(resultado)
                maquina.say(resultado)
                maquina.runAndWait()
            elif 'toque' in comando:
                musica = comando.replace('toque', '').strip()
                pywhatkit.playonyt(musica)
                maquina.say(f"Tocando {musica} no YouTube")
                maquina.runAndWait()

print("Inicializando assistente Eva...")
execute_command()
