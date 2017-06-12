tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


print "%r\n%r\n%r\n%r" % (tabby_cat, persian_cat, backslash_cat, fat_cat)

print "%s\n%s\n%s\n%s" % (tabby_cat, persian_cat, backslash_cat, fat_cat)

print "%r" % "I'll do a list:\n\t* Cat food\n\t*Fishes\n\t*Catnip\n\t* Grass"

