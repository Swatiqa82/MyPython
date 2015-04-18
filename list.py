#List is a collection of different datatypes in a sequence

zoo_animals = ["pangolin", "cassowary", 1,"swati" ];
# One animal is missing!
#print "The third animal at the zoo is the " + zoo_animals[2]
    
if len(zoo_animals) > 1:
	print "The first animal at the zoo is the " + zoo_animals[0]
	print "The second animal at the zoo is the " + zoo_animals[1]
	print  zoo_animals[2]
	print "The fourth animal at the zoo is the " + zoo_animals[3]

"""
    dictionary kids;

    kids.Add(  "ravi", "Beaverton")
    kids.Add("Ajit","Tigard")
    kids.Add("Swati","Santa Clara")

    kids["Swati"] // return Santa clara

    kids.length() //3
    kids["2ndChild"] // returns "Ajit"

    array names=["ajit", "Riya", "Swati", "Richa", "Prisha"];
    array address["tigard","tigard","SC","Tigard","Beaverton"];
    for(i=0; i<len(names); i++){
     if (names[i] == "Prisha")
      print i;
      address[i];
    }
"""

numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
# Your code here!
print numbers[1]+numbers[3]


