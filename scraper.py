from bs4 import BeautifulSoup
import requests
import webbrowser
import re




url = 'https://tatoeba.org/eng/audio/index/kab?page=75'

state = requests.get(url)

#print(state)
download = []
name = []
with requests.Session() as req:
    Html_Text = BeautifulSoup(state.text, features="html.parser")
    Audio_column = Html_Text.find_all("div", {"class": "audio"})
    Script_column = Html_Text.find_all("div", {"class": "content"})
    #print(Script_column)
    
    listWithAudioHREF = []
    ScriptOfaudio = []
    ScriptOfaudiotext = []
    for i in range(len(Audio_column)):
        listWithAudioHREF.append(Audio_column[i].find("a",{"href" : True}).attrs.get("href"))
        #print(listWithAudioHREF[i])
    for i in range(len(Script_column)):
        ScriptOfaudio.append(Script_column[i].find("div",{"lang" : True}))
        #ScriptOfaudiotext.append(ScriptOfaudio[i].text)
        print(ScriptOfaudio[i].text)
        ScriptOfaudio[i] = re.sub('[?"]', '', ScriptOfaudio[i].text)
    

    #webbrowser.open(listWithAudioHREF[i], new=2)
    for p in range(len(listWithAudioHREF)):
        download.append(req.get(listWithAudioHREF[p]))
        name.append(' '+ScriptOfaudio[p] + '.mp3')
    #print(name)
    #download = req.get(listWithAudioHREF[1])
    for c in range(len(download)): 
        with open(name[c], 'wb') as f:
            f.write(download[c].content)
