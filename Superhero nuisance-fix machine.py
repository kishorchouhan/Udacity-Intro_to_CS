# By Sam the Great from forums
# That freaking superhero has been frequenting Udacity
# as his favorite boss battle fight stage. The 'Udacity'
# banner keeps breaking, and money is being wasted on
# repairs. This time, we need you to proceduralize the
# fixing process by building a machine to automatically
# search through debris and return the 'Udacity' banner
# to the company, and be able to similarly fix other goods.
#
# Write a Python procedure fix_machine to take 2 string inputs
# and returns the 2nd input string as the output if all of its
# characters can be found in the 1st input string and "Give me
# something that's not useless next time." if it's impossible.
# Letters that are present in the 1st input string may be used
# as many times as necessary to create the 2nd string (you
# don't need to keep track of repeat usage).

def fix_machine(debris, product):
    a = len(product)
    while a != 0:
        b = debris.find(product[a-1])
        a = a-1
        if b == -1:
            p = "Give me something that's not useless next time."
            return p
            break
        if a == 0:
            return product


### TEST CASES ###
print ("Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == "Give me something that's not useless next time.")
print ("Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity')
print ("Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity')
print ("Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt')
