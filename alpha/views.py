# from django.shortcuts import render

# # Create your views here.

import random





salutations = ["Hi", "Hey", "Hola", "Bonjour", "Hey you", "Greetings", "Hi earthlings"]

names = ["Cory", "Dima", "Drew", "Etan", "Granger", "Ilias", "Isaac", "Jenn", "Jennifer", "Jessica", "John", "Julia", "Kevin", "Kirsten", "Marco", "Michael", "Nicholas", "Quincy", "Rory", "Sahil", "Sandy", "Shawn", "Steven", "Tahira", "Zach", "Zack", "Peter", "PJ", "Jeff", "Travis"]

professions = ["full-stack web developer", "front-end web developer", "UX Designer", "Rails Ninja", "Director of Smiles", "Mighty Eagle", "Sinatra Samurai", "Swiss Amry Knife", "Social Media Guru"]

alt_passions_intro = ["My passions are", "The things I care most about are", "I dream about", "I'm always working on", "My focuses are", "I wake up ready to learn about", "I am:", "I stand for:"]

passions = ["birding", "ultimate disc", "frisbee golf", "soup", "capture the flag", "whaling", "harpooning", "crochet", "needlepoint", "fast cars", "italian food", "getting slizzered", "gambling", "acquatics", "SQL", "great design", "memes", "instagram", "new media", "tough problems", "snapchat", "my tan", "my laundry", "Isaac's wardrobe", "#hashtags", "lifelong learning", "adventure", "banana pancakes", "breakfast sandwiches", "my belly button", "babies", "improv in every day life", "ad hoc-ing", "whiteboarding", "exposed brick", "wireframing", "skydiving", "riffing", "ideas", "artisinal salt shakers", "the south of France", "efficiency", "lean startups", "agile workflows", "gender equality", "religious freedom", "patriotism", "Magick the Gathering", "Pokemon", "my burgeoning sexuality", "justice", "freedom", "falling asleep in class", "virtua tennis", "LinkedIn"]

emails = ["@hugs.com", "@gmail.com", "@ymail.com", "@ga.co.uk", "@yourhotmom.com", "@playboy.com", "@racksonracksonracks.io"]

def paragraph():
	rand_salutation = random.sample(salutations, 1)
	rand_name = random.sample(names, 1)
	rand_alt_intro = random.sample(alt_passions_intro, 1)
	rand_profession = random.sample(professions, 1)
	passion_sample_1 = random.sample(passions, 1)
	passion_sample_2 = random.sample(passions, 1)
	passion_sample_3 = random.sample(passions, 1)
	rand_email = random.sample(emails, 1)
	full_email = rand_name[0] + rand_email[0]

	bio = "<h1 align='center' style='font-family: helvetica'>Bootcamp Bio Generator</h1><h2 align='center' style='font-family: helvetica'>%s, I'm %s.<br> I'm a %s.<br>%s %s, %s, and %s.<br><br>Let's chat!<br>%s</h2>" % (rand_salutation[0], rand_name[0], rand_profession[0], rand_alt_intro[0], passion_sample_1[0], passion_sample_2[0], passion_sample_3[0], full_email)

	return bio

def welcome():
	welcome = "<h1 align='center' style='font-family:helvetica'>Bootcamp Bio Generator</h1><br><a href='/alpha/bio'><div align='center'><button style='background: #0898bb; font-family: helvetica; font-size:18px; padding: 15px 15px 15px 15px; border-radius: 6px'>Generate Bio &raquo;</button></a></div>"
	return welcome

from django.http import HttpResponse

def index(request):
    return HttpResponse(welcome())

def randnum():
	nums = [1,2,3,4]
	random_number = random.sample(nums, 1)
	return random_number

def bio(request):
		return HttpResponse(paragraph())
