import aiml
import OS
# Create the kernel and learn AIML files
kernel = aiml.Kernel()
#kernel.learn("std-startup.xml")
#'startup.xml file consist of all the information about AIML files
#aiml file consist information about  input and responce.
kernel.learn('startup.xml')
kernel.respond("load aiml b")

# Press CTRL-C to break this loop
while True:
    print kernel.respond(raw_input("Enter your message >> "))
