class duck:
    def talk(self):
        print("Qauck Qauck")
class human:
    def talk(self):
        print("hich")
def callTalk(obj):
    obj.talk();
d=duck()
h=human()
callTalk(d)
callTalk(h)