print("salam be femboy khaneye ghamboz khosh amadadid")
first_bar = input("baraye kharid femboy enter ra bezanid\n")

second_bar = input(
    "shoma baraye kharid femboy bayad maraheli ra por konid\n")

###################### dick ######################

input("marhaleye aval:\n")

dick_question = input("kir shoma chand sant ast ?\n>>>")

# dick_question.int()

if int(dick_question) < 30:
    dick_status = True
# else:
#    dick_status = True

###################### income ######################

input("soal badi:\n")

income_question = input("hoghogh shoma dar mah cheghadr ast ?(toman)\n>>>")

if int(income_question) <= 1000000:
    income_status = False
else:
    income_status = True

# def introduce(first_name, last_name)
#    print(f"esm : {first_name} famil : {last_name}")

###################### introduce ######################


def introduce(first_name, last_name):
    print(f"esm : {first_name} famil : {last_name}")


first_name = input("esm shoma chist?\n>>>")
last_name = input("famili shoma chist?\n>>>")

###################### gender ######################

gender_question = input("jensiat shoma chist?(femboy , mard , zan)\n>>>")

# if gender_question == "femboy":
#    while:
#    gender_question == "femboy":
#    print("shoma nemitavanid vaghti femboy hastid femboy digari ra ejare konid.")
#    if gender_question != "femboy":

# second_gender_question

if gender_question == "femboy":
    print("shoma nemitavanid ham no'e khod ra bekharid")
    second_gender_question = input("jensiat shoma chist?\n>>>")

while second_gender_question == "femboy":
    print("shoma hanoz nemitavanid femboy ejare konid")
    thirth_gender_question = input("hala jensiat shoma chist?\n>>>")
    if thirth_gender_question != "femboy":
        break

if thirth_gender_question != "femboy":
    gender_status = True
else:
    gender_status = False

###################### glory to ghamboz ######################

print("va akharin soal")
last_question = input("zende bad koja ?\n>>>")

if last_question.lower() == "ghamboz":
    print("afarin")
else:
    while last_question != "ghamboz":
        print("dobare emtehan kon")
        second_last_question = input("zende bad koja ?\n>>>")
        if second_last_question == "ghamboz":
            break

if second_last_question == "ghamboz":
    honor = True
else:
    honor = False

###################### result ######################

if dick_question and income_status and gender_status and honor:
    print(
        f"aghaye {first_name}{last_name} shoma sharayet ejareye femboy ra darid")
else:
    print(
        f"aghaye {first_name}{last_name} shoma sharayet ejare femboy ra nadarid moteasefam")

print('baraye khoroj "exit" ra benevisid')

nothing = ""

while True:
    nothing = input(">>>")
    print(nothing)
    if nothing.lower() == "exit":
        break
print("khoda negahdar.")
