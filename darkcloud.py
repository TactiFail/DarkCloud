#!/usr/bin/python
import sys,os,random,string,readline

def banner():
	os.system('clear')
	print("DarkCloud v1.3.3.7\n")

def input_prompt():
	prompts = [
		os.getcwd(),
		os.getcwd().split('/')[-1],
		''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(random.randint(8,10))),
		'YouAreHere',
		'Somewhere',
	]
	
	return random.choice(prompts) + "> "

def magic_8():
	answers = [
		'It is certain',
		'It is decidedly so',
		'Without a doubt',
		'Yes definitely',
		'You may rely on it',
		'As I see it, yes',
		'Most likely',
		'Outlook good',
		'Yes',
		'Signs point to yes',
		'Reply hazy try again',
		'Ask again later',
		'Better not tell you now',
		'Cannot predict now',
		'Concentrate and ask again',
		'Don\'t count on it',
		'My reply is no',
		'My sources say no',
		'Outlook not so good',
		'Very doubtful',
	]
	return random.choice(answers)

def exit():
	valedictions = [
		'So long',
		'Farewell',
		'Auf wiedersehen',
		'Adieu',
		'GTFO!',
		'How lucky I am to have something that makes saying goodbye so hard',
		'',
	]
	print(random.choice(valedictions) + "\n")
	sys.exit(0)

def unknown(cmd):
	whoknows = [
		'Unrecognized command',
		'I don\'t know what to do with that',
		'\'' + cmd + '\' is not recognized as an internal or external command,\noperable program or batch file',
	]

	return random.choice(whoknows)

# Commands

def ls_dir():
	outputs = [
		"os.system('ls')",
		"os.system('ls | sed -e \\'s/\\t//g\\' | tr -d \\'\\n\\'')",
	]
	eval(random.choice(outputs))

def repl_loop():
	while True:
		cmd = raw_input(input_prompt())

		if random.randint(0,9) == 0:
			print(magic_8() + "\n")
		elif cmd == 'exit' or cmd == 'quit':
			exit()
		elif cmd == 'ls' or cmd == 'dir':
			ls_dir()
		elif cmd == 'clear':
			os.system('clear')
		else:
			print(unknown(cmd) + "\n")

if __name__ == "__main__":
	banner()
	repl_loop()
