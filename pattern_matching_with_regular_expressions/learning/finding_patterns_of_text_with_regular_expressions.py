import re

phoneNumberRegex1 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumberRegex2 = re.compile(r'\d{3}-\d{3}-\d{4}')

mo1 = phoneNumberRegex1.search('My number is 415-555-4242.')
mo2 = phoneNumberRegex2.search('My number is 415-555-4242')

print(mo1)
print(mo2)
print(mo1.group())
print(mo2.group())
print('Phone number found: ' + mo1.group())
print('Phone number found: ' + mo2.group())

# print(phoneNumberRegex1('My number is'))
# print(phoneNumberRegex2('My number is'))

# --------------------------------------------------------------

phoneNumberRegexGroup = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumberRegexGroup.search('My number is 415-555-4242')
print(mo)
print(mo.group())
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

# --------------------------------------------------------------

phoneNumberRegexParentheses = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumberRegexParentheses.search('My number is (415) 555-4242')
print(mo)
print(mo.group())
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

# --------------------------------------------------------------

phoneNumberRegexPipe = re.compile(r'Batman|Tina Fey')
mo = phoneNumberRegexPipe.search('just Batman')
mo1 = phoneNumberRegexPipe.search('batman and Tina Fey')
mo2 = phoneNumberRegexPipe.search('Batman and Tina Fey')
mo3 = phoneNumberRegexPipe.search('Tina Fey and Batman')
print(mo.group(), '-', mo1.group(), '-', mo2.group(), '-', mo3.group())


batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

# --------------------------------------------------------------

batRegexOptional = re.compile(r'Bat(wo)?man')
mo = batRegexOptional.search('The adventures of Batman')
mo1 = batRegexOptional.search('The adventures of Batwoman')
print(mo.group(), '-', mo1.group())

# --------------------------------------------------------------

batRegexStar = re.compile(r'Bat(wo)*man')
mo = batRegexStar.search('The adventure of Batman')
mo1 = batRegexStar.search('The adventure of Batwoman')
mo2 = batRegexStar.search('The adventure of Batwowoman')
print(mo.group(), '-', mo1.group(), '-', mo2.group())

# --------------------------------------------------------------

batRegexPlus = re.compile(r'Bat(wo)+man')
mo = batRegexPlus.search('The adventure of Batman')
mo1 = batRegexPlus.search('The adventure of Batwoman')
mo2 = batRegexPlus.search('The adventure of Batwowoman')
print(mo == None)
print(mo1.group())
print(mo2.group())

# ---------------------------------------------------------------

haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('HaHaHa')
mo1 = haRegex.search('Ha')
print(mo.group())
print(mo1 == None)

# ---------------------------------------------------------------

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo = greedyHaRegex.search('HaHaHaHaHa')
print(mo.group())
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo1 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

# ----------------------------------------------------------------

phoneNumberRegexCompareSearchAndFindall = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegexCompareSearchAndFindall.search('Cell: 415-555-9999 Work: 212-555-0000')
mo1 = phoneNumberRegexCompareSearchAndFindall.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())
print(mo1)

PhoneNumberRegexfindallGroup = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = PhoneNumberRegexfindallGroup.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)

# -----------------------------------------------------------------

vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegexNegetive = re.compile(r'[^aeiouAEIOU]')
mo = vowelRegex.search('RoboCop eats baby food. BABY FOOD.')
mo1 = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
mo2 = vowelRegexNegetive.search('RoboCop eats baby food. BABY FOOD.')
mo3 = vowelRegexNegetive.findall('RoboCop eats baby food. BABY FOOD.')
print(mo.group())
print(mo1)
print(mo2.group())
print(mo3)

# ------------------------------------------------------------------

carrotsCostDollarsRegex = re.compile(r'^Hello\sfriend\s\d+$')
mo = carrotsCostDollarsRegex.search('Hello friend 12')
mo1 = carrotsCostDollarsRegex.search('HEllo friend 1')
mo2 = carrotsCostDollarsRegex.search('Hello friend')
print(mo.group(), '-', mo1 == None, '-', mo2 == None)

# -------------------------------------------------------------------

atRegexWithDot = re.compile(r'.at')
mo = atRegexWithDot.findall('The cat in the hat sat on the flat mat.')
print(mo)

# -------------------------------------------------------------------

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.findall('First Name: Al Last Name: Sweigart')
mo1 = nameRegex.findall('First Name: Seyyed Mahdi Last Name: Sepahbodi')
print(mo)
print(mo1)

# -------------------------------------------------------------------

greedyDotStarRegex = re.compile(r'<.*?>')
nongreedyDotStarRegex = re.compile(r'<.*>')
mo = greedyDotStarRegex.search('<To serve man> for dinner.>')
mo1 = nongreedyDotStarRegex.search('<To serve man> for dinner.>')
print(mo.group())
print(mo1.group())

# -------------------------------------------------------------------

noNewLineRegex = re.compile('.*')
newLineRegex = re.compile('.*', re.DOTALL)
mo = noNewLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
mo1 = newLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(mo)
print(mo1)

# --------------------------------------------------------------------

caseinsensitiveRegex = re.compile(r'robocop', re.I)
mo = caseinsensitiveRegex.search('RoboCop is part man, part machine, all cop.').group()
mo1 = caseinsensitiveRegex.search('roboCop is part man, part machine, all cop.').group()
print(mo)
print(mo1)

# --------------------------------------------------------------------

namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo)

substitutingStringsRegex = re.compile(r'Agent (\w)\w*')
mo = substitutingStringsRegex.sub(r'\1****', 'Agent Alice told Agent Carol that AgentEve knew Agent Bob was a double agent.')
print(mo)