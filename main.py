import pprint
from resume_parser import parse_resume

result = parse_resume("Column_resume.pdf")

# Print the pretty-printed JSON string
pprint.pprint(result)