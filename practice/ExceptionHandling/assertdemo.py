try:
    pasw=input("please enter your password: ")
    assert len(pasw)>8, "you have entered wrong lenght"
except AssertionError  as obj:
    print("you have enter wrong lenght of password")
finally:
    print("Program terminated")