formattter = "{} {} {} {}"

print(formattter.format(1, 2, 3, 4))
print(formattter.format("one", "two", "three", "four"))
print(formattter.format(True, False, False, True))
print(formattter.format(formattter, formattter, formattter, formattter))
print(formattter.format(
    "well will you look at that,",
    "everything is quite funny",
    "and i wonder when it will eventually start making sense.",
    "well well here we go again"
))