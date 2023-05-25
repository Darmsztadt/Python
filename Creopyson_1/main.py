import creopyson

c = creopyson.Client()
c.connect()
c.creo_set_creo_version(7)
def parametry():
    while True:
        parameter = input(
            "Wybierz parametr z listy do zmiany:\n1.Wysokość kostki\n2.Długość kostki\n3.Szerokość kostki\n4.Wysokość tekstu\n5.Długość tekstu\n6.Szerokość tekstu\n7.Tekst\n8.Zatwierdź i zakończ zmianę parametrów\n")
        while parameter not in ("1", "2", "3", "4", "5", "6", "7", "8"):
            parameter = input("Wybierz poprawny parametr\n")
        if parameter=="1":
            while True:
                try:
                    wys = int(input("Podaj wysokość kostki\n"))
                    if wys > 0:
                        c.parameter_set("wys", wys)
                        break
                except:
                    print("Niepoprawny typ danych")
        elif parameter=="2":
            while True:
                try:
                    dlug = int(input("Podaj długość kostki\n"))
                    if dlug > 0:
                        c.parameter_set("dlug", dlug)
                        break
                except:
                    print("Niepoprawny typ danych")
        elif parameter == "3":
            while True:
                try:
                    szer = int(input("Podaj szerokość kostki\n"))
                    if szer > 0:
                        c.parameter_set("szer", szer)
                        break
                except:
                    print("Niepoprawny typ danych")
        elif parameter == "4":
            while True:
                try:
                    wys_t = int(input("Podaj wysokość tekstu\n"))
                    if wys_t > 0:
                        c.parameter_set("wys_t", wys_t)
                        break
                except:
                    print("Niepoprawny typ danych")
        elif parameter == "5":
            while True:
                try:
                    dlug_t = int(input("Podaj długość tekstu\n"))
                    if dlug_t > 0:
                        c.parameter_set("dlug_t", dlug_t)
                        break
                except:
                    print("Niepoprawny typ danych")
        elif parameter == "6":
            while True:
                try:
                    szer_t = int(input("Podaj szerokośc tekstu\n"))
                    if szer_t > 0:
                        c.parameter_set("szer_t", szer_t)
                        break
                except:
                    print("Niepoprawny typ danych")
        elif parameter == "7":
            while True:
                try:
                    tekst=input("Podaj tekst\n")
                    if len(tekst)>0:
                        c.parameter_set("tekst",tekst)
                        break
                except:
                    print("Tekst niepoprawny")
        elif parameter == "8":
            break
def path():
    while True:
        try:
            dir = input("Podaj ściezkę folderu roboczego (zostaw puste by pominąć)\n")
            if dir=="":
                break
            c.creo_cd(dir)
            break
        except:
            print("Nieporawna ścieżka")
def switch():
    material = input(
        "Wpisz numer materiału z listy:\n1.Alumina\n2.Boron carbide\n3.Concrete\n4.Glass\n5.Granite\n6.Limestone\n7.Marble\n8.Sandstone\n9.Slate\n10.Zirconia\n")
    while material not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
        material = input("Wybierz poprawny materiał\n")
    if material == "1":
        return "Alumina"
    elif material == "2":
        return "Boron_carbide"
    elif material == "3":
        return "Concrete"
    elif material == "4":
        return "Glass"
    elif material == "5":
        return "Granite"
    elif material == "6":
        return "Limestone"
    elif material == "7":
        return "Marble"
    elif material == "8":
        return "Sandstone"
    elif material == "9":
        return "Slate"
    elif material == "10":
        return "Zirconia"

while True:
    trigger=input("Wybierz operację:\n1.Zmień parametry\n2.Zmień materiał\n3.Zmień folder roboczy\n4.Zakończ program\n")
    while trigger not in("1","2","3","4"):
        trigger=input("Wybierz poprawną operację\n")
    if trigger=="2":
        material_input = switch()
        c.file_load_material_file(material_input,
                                  r"C:\Program Files\PTC\Creo 7.0.1.0\Common Files\text\materials-library\Standard-Materials_Granta-Design\Ceramics_and_glasses")
        c.file_set_cur_material(material_input)
        c.file_regenerate()
    elif trigger=="1":
        parametry()
        c.file_regenerate()
    elif trigger=="3":
        path()
        c.file_regenerate()
    elif trigger=="4":
        c.file_regenerate()
        break

