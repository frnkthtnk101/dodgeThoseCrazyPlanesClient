# dodgeThoseCrazyPlanesClient
## About
This is a game about a ship in space, surviving for  
for its life from the bad guys of space.


## TOC
- Modules
- Installation
- the robustness
- did franco do the extra cred?


## Modules
The following modules are going to be needed to run this program (in python3.7)  
- re
- socket
- pygames
- unittest
- sys
- random

You should have everything with a normal install, but pygames. all you need  
for that is just do a `pip3.7 install pygame`. just make sure your in admin mode  
so you have the correct permission. VScode gets funny with that stuff


## Installation
### Running the Game
1. copy and paste the DODGETHOSECRAZYPLANESCLIENT to your `$HOME` directory
2. copy and paste the DODGETHOSECRAZYPLANESSERVER to your `$HOME` directory
3. run the server in with this command in the _SOURCE_ directory `python3.7 Main.py`
- the server runs at local as default
4. run the client in with this command in the _SOURCE_ directory `python3.7 Main.py`
- its going to ask for a ip and level. press enter medium enter
5. beat the highschore of 1000

### Running the Test
to run the test you need to hard-code the path of the source... recomend running them in
vscode


## the robustness
through testing, I was able to debug allot of issues with the system. Also found out that
there are some chinks in the aromour when it comes to my states. After initiailize, a program 
can easily keep sending bad level request over and eventually break the system OR the client does have to
end or quit the game. other than that, Its pretty solid. You can't get levels without telling the
server you are starting a game. The test just test the basics out. for example, if I send a level request, I get a  level response.


## did franco do the extra cred?
no.