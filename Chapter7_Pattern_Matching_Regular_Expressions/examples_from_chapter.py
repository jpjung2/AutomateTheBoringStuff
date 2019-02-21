import re

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman and Robin')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
number = phoneRegex.search("My number is 415-555-4242")
print(number.group())

number = phoneRegex.search("My number is (415)-555-4242")
print(number.group(0))

batRegex = re.compile(r'Bat(wo)*man')
mo_bat = batRegex.search("The adventures of Batman")
print(mo_bat.group())

mo_ba2 = batRegex.search("The Adventures of Batwoman")
print(mo_ba2.group())
mo_bat3 = batRegex.search("The Adventures of Batwowowowoman")
print(mo_bat3.group())

print()

batman = "The Adventures of Batman"
batwoman = "The Adventures of Batwoman"
bwowo = "The Adventures of Batwowowowoman"

plusBat = re.compile(r"Bat(wo)+man")
bw = plusBat.search("The Adventures of Batwoman")
print(bw.group())
bw = plusBat.search(bwowo)
print(bw.group())
bm = plusBat.search(batman)
print(bm)
print()

anan = re.compile(r"(an){2,8}")
banana = anan.search("Bananas")
print(banana.group())

bananana = anan.search("Bananananan")
print(bananana.group())
print()

# Find all method

phoneRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
nums = phoneRegex.findall("Cell: 555-555-5555; Home: 666-666-6666")

for thing in nums:
    print(thing)

phoneRegex = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)")
nums = phoneRegex.findall("Cell: 555-555-5555; Home: 666-666-6666")
for thing in nums:
    print(type(thing) == tuple)

# Character Classes

xmasRegex = re.compile(r"\d+\s\w+")
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lord, 9 ladies, 8 maids, 7 rings'))
print()

# Making You Own Character Classes
vowel = re.compile(r"[aeiouAEIOU]")
print(vowel.findall("The quick brown fox jumped over the lazy dog"))
consonants = re.compile(r"[^aeiouAEIOU\s]")
print(consonants.findall("The quick brown fox jumped over the lazy dog"))
print()
