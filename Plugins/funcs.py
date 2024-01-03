from colorama import init
from pystyle import Colorate, Colors, Center, Col, Add, Anime

from Plugins.logger import Logger
from Plugins.colors import Palette



palette = Palette()



class Funcs:
    
    @staticmethod
    def get_input(text: str, checker = True):
        
        
        
        text = f"{palette.red}{text}{palette.better_grassy_green}"

        v = input(text)
        if not checker(v):
            while not checker(v):
                Logger.Error.error("Try Again")
                v = input(text)
        
        return v
    
    @staticmethod
    def print_logo():
        logo = """
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:   $   ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:  $ :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!        
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
"""


        print(Colorate.Vertical(Colors.DynamicMIX((Col.red, Col.dark_red)), logo))