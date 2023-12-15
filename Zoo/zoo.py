# zoo.py

camel = r"""
a'!   _,,_ a'!   _,,_     a'!   _,,_
  \\_/    \  \\_/    \      \\_/    \.-,
   \, /-( /'-,\, /-( /'-,    \, /-( /
   //\ //\\   //\ //\\       //\ //\\jrei"""

lion = r"""
   ,/^\'-~-`/^\,
    {(3)       (E)}
  ,(- __\     /__ -),
,{    =*.;   ;.*=    },
{   /   \  |  /   \   ),
` /      / | \      \  }
` /  -~~(.,Y,.)~~-  \  }
{  /     (^"^)     \  }'
`{,  /     ~     \  ,}'
 \`{\_/         \_/}'/
  >_ _`\,,/|\,,/'_ _<
 `(}(}(} `~-~' {){){)'
The lion is roaring!"""

deer = r"""
The deer habitat...
(             )
 `--(_   _)--'
      Y-Y
     /@@ \
    /     \
    `--'.  \             ,
        |   `.__________/)
Pretty good!"""

goose = r"""
The goose habitat...

_
,-"" "".
,' ____ `.
,' ,' `. `._
(`. _..--.._ ,' ,' \ \
(`-.\ .-"" ""' / ( d _b
(`._ `-"" ,._ ( `-( \
<_ ` ( <`< \ `-._\
<`- (__< < :
(__ (_<_< ;
`------------------------------------------
Beautiful!"""

bat = r"""
The bat habitat...
    =/\                 /\=
    / \'._   (\_/)   _.'/ \
   / .''._'--(o.o)--'_.''. \
  /.' _/ |`'=/ " \='`| \_ `.\
 /` .' `\;-,'\___/',-;/` '. '\
/.-' jgs   `\(-V-)/`       `-.\
`            "   "            `
It's doing fine."""

rabbit = r"""
The rabbit habitat...
               ((`\
            ___ \\ '--._
         .'`   `'    o  )
        /    \   '. __.'
       _|    /_  \ \_\_
jgs   {_\______\-'\__\_\
It looks fine!"""


# List of animals
animals = [camel, lion, deer, goose, bat, rabbit]

print("I love animals!")
print("Let's check out the animals...")

while True:
    # Ask user for the number of the habitat
    user_input = input("Please enter the number of the habitat you would like to view: > ")

    if user_input.lower() == 'exit':
        print("See you later!")
        break

    try:
        habitat_number = int(user_input)
        if 1 <= habitat_number <= len(animals):
            print(animals[habitat_number - 1])
            print("It looks fine!\n---")
        else:
            print("Invalid habitat number. Please enter a number between 1 and", len(animals))
    except ValueError:
        print("Invalid input. Please enter a valid number or 'exit'.")
