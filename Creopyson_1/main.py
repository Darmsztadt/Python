import creopyson

c = creopyson.Client()
c.connect()
c.creo_set_creo_version(7)


def param_set(param):
    if param == "tekst":
        while True:
            try:
                text = input("Podaj tekst\n")
                if len(text) > 0:
                    c.parameter_set("tekst", text)
                    break
            except:
                print("Tekst niepoprawny")
    else:
        while True:
            try:
                x = int(input("Podaj wartość parametru\n"))
                if x > 0:
                    c.parameter_set(param, x)
                    break
            except:
                print("Niepoprawne dane")


def parameters():
    while True:
        parameter = input(
            "Wybierz parametr z listy do zmiany:\n1.Wysokość kostki\n2.Długość kostki\n3.Szerokość kostki\n4.Wysokość tekstu\n5.Długość tekstu\n6.Szerokość tekstu\n7.Tekst\n8.Zatwierdź i zakończ zmianę parametrów\n")
        while parameter not in ("1", "2", "3", "4", "5", "6", "7", "8"):
            parameter = input("Wybierz poprawny parametr\n")
        parameter_list = ["wys", "dlug", "szer", "wys_t", "dlug_t", "szer_t", "tekst"]
        if parameter == "8":
            break
        param_set(parameter_list[int(parameter)])


def path():
    while True:
        try:
            dir = input("Podaj ściezkę folderu roboczego (zostaw puste by pominąć)\n")
            if dir == "":
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
    material_list = {
        "1": "Alumina",
        "2": "Boron_carbide",
        "3": "Concrete",
        "4": "Glass",
        "5": "Granite",
        "6": "Limestone",
        "7": "Marble",
        "8": "Sandstone",
        "9": "Slate",
        "10": "Zirconia"
    }
    return material_list[material]


while True:
    trigger = input(
        "Wybierz operację:\n1.Zmień parametry\n2.Zmień materiał\n3.Zmień folder roboczy\n4.Zakończ program\n")
    while trigger not in ("1", "2", "3", "4"):
        trigger = input("Wybierz poprawną operację\n")
    if trigger == "2":
        material_input = switch()
        c.file_load_material_file(material_input,
                                  r"C:\Program Files\PTC\Creo 7.0.1.0\Common Files\text\materials-library\Standard-Materials_Granta-Design\Ceramics_and_glasses")
        c.file_set_cur_material(material_input)
        c.file_regenerate()
    elif trigger == "1":
        parameters()
        c.file_regenerate()
    elif trigger == "3":
        path()
        c.file_regenerate()
    elif trigger == "4":
        c.file_regenerate()
        break
