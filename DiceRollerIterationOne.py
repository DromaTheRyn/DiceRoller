import random #random function
import PySimpleGUI as sg #frontend

#Variablen, um Würfel zu zählen
diceincrementd4 = int(0)
diceincrementd6 = int(0)
diceincrementd8 = int(0)
diceincrementd10 = int(0)
diceincrementd12 = int(0)
diceincrementd20 = int(0)
diceincrementd100 = int(0)

#Funktionen für Würfel
def d4():
    return random.randint(1,4)
def d6():
    return random.randint(1,6)
def d8():
    return random.randint(1,8)
def d10():
    return random.randint(1,10)
def d12():
    return random.randint(1,12)
def d20():
    return random.randint(1,20)
def d100():
    return random.randint(1,100)

#Funktionen, um Anzahl der Würfel aufzuaddieren, da Python 0*d6 + 2d8... nicht korrekt verarbeiten kann (Aufaddierung von Werten, bei denen Multiplikation mit 0 erfolgt).
#Folgendes Beispiel ruft die Random Funktion nur 1 mal auf, was nur zur Bildung gerader Zahlen führt (increment*d4). Stattdessen soll die Funktion für jedes Inkrement der Variable einzeln aufgerufen und hinzuaddiert werden (für jede Zahl >0, führe Funktion d4 aus und speicher returne den Wert zur Funktion).
#def multiplyd4():
#    if diceincrementd4 <=0:
#        return 0
#    else:
#        return diceincrementd4 * d4()

#Folgendes Beispiel funktioniert NICHT in Python, da nicht auf 0 überprüft wird und die Funktion nicht erneut aufgerufen wird. Bei diceincrementd4 = 4 wären nur [4,8,12,16] mögliche Ergebnisse, da der d4 nur 1 mal geworfen wird und das Ergebnis mit 4 multipliziert wird.
# def damage()
#   return diceincrementd4 * d4() + diceincrementd6 * d6() + [...] + diceincrementd100 * d100() 

#Aus C oder Java bekannte for Schleifen gibt es in Python nicht, wir müssen also 2 weitere Variablen erstellen.
#d4counter wird inkrementiert, bis er dem Integer Wert aus diceincrementd4 entspricht. Bei jeder Inkrementierung wird die Funktion d4() aufgerufen und der Wert in d4sum gespeichert. Wenn d4counter diceincrementd4 entspricht ist die Bedingung erfüllt und d4sum als Integer an die Funktion multiply4d zurückgegeben.
def multiplyd4():
    d4counter = 0
    d4sum = 0
    if diceincrementd4 <=0:
        return 0
    else:
        while True:
            if d4counter < diceincrementd4:
                d4sum += d4()
                d4counter += 1
            else: 
                return d4sum
def multiplyd6():
    d6counter = 0
    d6sum = 0
    if diceincrementd6 <=0:
        return 0
    else:
        while True:
            if d6counter < diceincrementd6:
                d6sum += d6()
                d6counter += 1
            else: 
                return d6sum
def multiplyd8():
    d8counter = 0
    d8sum = 0
    if diceincrementd8 <=0:
        return 0
    else:
        while True:
            if d8counter < diceincrementd8:
                d8sum += d8()
                d8counter += 1
            else: 
                return d8sum
def multiplyd10():
    d10counter = 0
    d10sum = 0
    if diceincrementd10 <=0:
        return 0
    else:
        while True:
            if d10counter < diceincrementd10:
                d10sum += d10()
                d10counter += 1
            else: 
                return d10sum
def multiplyd12():
    d12counter = 0
    d12sum = 0
    if diceincrementd12 <=0:
        return 0
    else:
        while True:
            if d12counter < diceincrementd12:
                d12sum += d12()
                d12counter += 1
            else: 
                return d12sum
def multiplyd20():
    d20counter = 0
    d20sum = 0
    if diceincrementd20 <=0:
        return 0
    else:
        while True:
            if d20counter < diceincrementd20:
                d20sum += d20()
                d20counter += 1
            else: 
                return d20sum    
def multiplyd100():
    d100counter = 0
    d100sum = 0
    if diceincrementd100 <=0:
        return 0
    else:
        while True:
            if d100counter < diceincrementd100:
                d100sum += d100()
                d100counter += 1
            else: 
                return d100sum  

#Funktionen zusammenzählen, um damage zu bestimmen                          
def damage():
        return multiplyd4() + multiplyd6() + multiplyd8() + multiplyd10() + multiplyd12() + multiplyd20() + multiplyd100()  

#Pures GUI layout, mit Eigenschaften der der Elemente der Benutzeroberfläche
layout = [  
            [sg.Text('Type of Dice:'), sg.Button(enable_events=True, size=(2,1), button_text= '-',key='d4-'), sg.Text(size=(2,1), text='d4'), sg.Button(enable_events=True, size=(2,1), button_text= '+', key='d4+'), sg.Button(enable_events=True, size=(2,1), button_text= '-',key='d6-'), sg.Text(size=(2,1), text='d6'), sg.Button(enable_events=True, size=(2,1), button_text= '+', key='d6+'), sg.Button(enable_events=True, size=(2,1), button_text= '-',key='d8-'), sg.Text(size=(2,1), text='d8'), sg.Button(enable_events=True, size=(2,1), button_text= '+', key='d8+'), sg.Button(enable_events=True, size=(2,1), button_text= '-',key='d10-'), sg.Text(size=(3,1), text='d10'), sg.Button(enable_events=True, size=(2,1), button_text= '+', key='d10+'), sg.Button(enable_events=True, size=(2,1), button_text= '-',key='d12-'), sg.Text(size=(3,1), text='d12'), sg.Button(enable_events=True, size=(2,1), button_text= '+', key='d12+'), sg.Button(enable_events=True, size=(2,1), button_text= '-',key='d20-'), sg.Text(size=(3,1), text='d20'), sg.Button(enable_events=True, size=(2,1), button_text= '+', key='d20+'), sg.Button(enable_events=True, size=(2,1), button_text= '-',key='d100-'), sg.Text(size=(4,1), text='d100'), sg.Button(enable_events=True, size=(2,1), button_text= '+', key='d100+')],
            [sg.Text('Number of Dice:'), sg.Text(size=(1,1), text=''), sg.Text(enable_events=True, size=(2,1), key='diceincrementd4', text=diceincrementd4), sg.Text(size=(2,1), text=''), sg.Text(size=(2,1), text=''), sg.Text(enable_events=True, size=(2,1), key='diceincrementd6', text=diceincrementd6), sg.Text(size=(2,1), text=''), sg.Text(size=(3,1), text=''), sg.Text(enable_events=True, size=(2,1), key='diceincrementd8', text=diceincrementd8), sg.Text(size=(2,1), text=''), sg.Text(size=(3,1), text=''), sg.Text(enable_events=True, size=(3,1), key='diceincrementd10', text=diceincrementd10), sg.Text(size=(2,1), text=''), sg.Text(size=(2,1), text=''), sg.Text(enable_events=True, size=(3,1), key='diceincrementd12', text=diceincrementd12), sg.Text(size=(2,1), text=''), sg.Text(size=(3,1), text=''), sg.Text(enable_events=True, size=(3,1), key='diceincrementd20', text=diceincrementd20), sg.Text(size=(2,1), text=''), sg.Text(size=(3,1), text=''), sg.Text(enable_events=True, size=(4,1), key='diceincrementd100', text=diceincrementd100)], 
            [sg.Text('Damage:'), sg.Text(size=(3,1), key='-OUTPUT-')],
            [sg.Button('Roll'), sg.Button('Clear'), sg.Text(size=(82,1), text=''), sg.Button('Exit')]
        ]
#Rendert das Fenster
window = sg.Window('Dice Roller', layout)

#Event Loop
while True:             
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Clear':
        window['-OUTPUT-'].update('')           #Alle Elemente mit der Eigenschaft Output werden auf dem GUI durch ein Leerzeichen ersetzt
        window['diceincrementd4'].update('0')   #Elemente mit Eigenschaft wird auf 0 gesetzt (Anzahl der Würfel)
        window['diceincrementd6'].update('0')
        window['diceincrementd8'].update('0')
        window['diceincrementd10'].update('0')
        window['diceincrementd12'].update('0')
        window['diceincrementd20'].update('0')
        window['diceincrementd100'].update('0')
        diceincrementd4 = 0                     #Variablen werden auf 0 gesetzt (durch clicken des Clear Buttons)
        diceincrementd6 = 0
        diceincrementd8 = 0
        diceincrementd10 = 0
        diceincrementd12 = 0
        diceincrementd20 = 0
        diceincrementd100 = 0
    if event == 'Roll':                         #damage Funktion wird ausgeführt und das GUI geupdated
        window['-OUTPUT-'].update(damage())
    if event == 'd4-':                          #+/- Buttons updaten Variablen und GUI (dass sie unter 0 fallen wird bereits in der Funktion multiplyd4-100 "verhindert")
        diceincrementd4 -= 1                    #diceincrementd4 = diceincrementd4 -1, negative zahken werden verhindert
        if diceincrementd4 <0 :
            diceincrementd4 =0
            window['diceincrementd4'].update('0') 
        else :                  
            window['diceincrementd4'].update(diceincrementd4) #GUI Elemente mit Eigenschaft diceincrementd4 werden geupdated und mit dem Integer der Variable gefüllt
    if event == 'd4+':
        diceincrementd4 += 1
        if diceincrementd4 <0 :
            diceincrementd4 =0
            window['diceincrementd4'].update('0') 
        else :
            window['diceincrementd4'].update(diceincrementd4)
    if event == 'd6-':                          
        diceincrementd6 -= 1
        if diceincrementd6 <0 :
            diceincrementd6 =0
            window['diceincrementd6'].update('0') 
        else :                    
            window['diceincrementd6'].update(diceincrementd6)
    if event == 'd6+':
        diceincrementd6 += 1
        if diceincrementd6 <0 :
            diceincrementd6 =0
            window['diceincrementd6'].update('0') 
        else :
            window['diceincrementd6'].update(diceincrementd6)
    if event == 'd8-':                          
        diceincrementd8 -= 1
        if diceincrementd8 <0 :
            diceincrementd8 =0
            window['diceincrementd8'].update('0') 
        else :                    
            window['diceincrementd8'].update(diceincrementd8)
    if event == 'd8+':
        diceincrementd8 += 1
        if diceincrementd8 <0 :
            diceincrementd8 =0
            window['diceincrementd8'].update('0') 
        else :
            window['diceincrementd8'].update(diceincrementd8)
    if event == 'd10-':                          
        diceincrementd10 -= 1   
        if diceincrementd10 <0 :
            diceincrementd10 =0
            window['diceincrementd10'].update('0') 
        else :                 
            window['diceincrementd10'].update(diceincrementd10)
    if event == 'd10+':
        diceincrementd10 += 1
        if diceincrementd10 <0 :
            diceincrementd10 =0
            window['diceincrementd10'].update('0') 
        else :
            window['diceincrementd10'].update(diceincrementd10)
    if event == 'd12-':                          
        diceincrementd12 -= 1
        if diceincrementd12 <0 :
            diceincrementd12 =0
            window['diceincrementd12'].update('0') 
        else :                    
            window['diceincrementd12'].update(diceincrementd12)
    if event == 'd12+':
        diceincrementd12 += 1
        if diceincrementd12 <0 :
            diceincrementd12 =0
            window['diceincrementd12'].update('0') 
        else :
            window['diceincrementd12'].update(diceincrementd12)
    if event == 'd20-':                          
        diceincrementd20 -= 1 
        if diceincrementd20 <0 :
            diceincrementd20 =0
            window['diceincrementd20'].update('0') 
        else :                   
            window['diceincrementd20'].update(diceincrementd20)
    if event == 'd20+':
        diceincrementd20 += 1
        if diceincrementd20 <0 :
            diceincrementd20 =0
            window['diceincrementd20'].update('0') 
        else :
            window['diceincrementd20'].update(diceincrementd20) 
    if event == 'd100-':                          
        diceincrementd100 -= 1
        if diceincrementd100 <0 :
            diceincrementd100 =0
            window['diceincrementd100'].update('0') 
        else :                    
            window['diceincrementd100'].update(diceincrementd100)
    if event == 'd100+':
        diceincrementd100 += 1
        if diceincrementd100 <0 :
            diceincrementd100 =0
            window['diceincrementd100'].update('0') 
        else :
            window['diceincrementd100'].update(diceincrementd100) 

window.close()


