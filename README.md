# simpleChatBot

Developed the simple chat bot using Python and AIML(Artificial Intilegence Markup Language).

#What is AIML?

AIML was developed by Richard Wallace. He made a bot called A.L.I.C.E. (Artificial Linguistics Internet Computer Entity) which won several artificial intelligence awards. Interestingly, one of the Turing tests to look for artificial intelligence is to have a human chat with a bot through a text interface for several minutes and see if they thought it was a human. AIML is a form of XML that defines rules for matching patterns and determining responses.

AIML as 4 Basic Tags:

    <aiml> - defines the beginning and end of a AIML document.

    <category> - defines the unit of knowledge in Alicebot's knowledge base.

    <pattern> - defines the pattern to match what a user may input to an Alicebot.

    <template> - defines the response of an Alicebot to user's input.

other tags reference will be avilable in the reference link : http://www.alicebot.org/documentation/aiml-reference.html

#Simplest Python Program
    python module for the running AIML : #'Pip install aiml'
This is the simplest program we can start with. It creates the aiml object, learns the startup file, and then loads the rest of the aiml files. After that, it is ready to chat, and we enter an infinite loop that will continue to prompt the user for a message. You will need to enter a pattern the bot recognizes. The patterns recognized depend on what AIML files you loaded.

We create the startup file as a separate entity so that we can add more aiml files to the bot later without having to modify any of the programs source code. We can just add more files to learn in the startup xml file.

    import aiml

    # Create the kernel and learn AIML files
    kernel = aiml.Kernel()
    kernel.learn("std-startup.xml")
    kernel.respond("load aiml b")

    # Press CTRL-C to break this loop
    while True:
        print kernel.respond(raw_input("Enter your message >> "))
    
in std_startup.xml file we can include the diffenrent aiml file according our requirement for chatbot replay process.
    for e.g : <learn>hello.aiml</learn>
    now 'hello.aiml' included in <learn> tag it loads the every information present in the aiml to the xml then replay to python.
    
#brain.py  
    python script for loading the aiml files through startup.xml
#startup.xml 
    xml script for loading the AIML files
# * .aiml 
    which consist of source and responce of chatbot.
