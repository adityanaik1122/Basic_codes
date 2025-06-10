import re
quote = "There is only one thing I hate more than lying: skim milk. Which is water that's lying about being milk."

print(re.search("milk",quote).group())

print(re.findall("milk",quote))

print(len(re.findall("milk",quote)))

print(re.split("=-",quote))

print(re.findall("milk",quote))