# -*- coding: utf-8 -*-
#skrypt zapisuje sparsowany plik xml na txt korzystajac z http://www.mediawiki.org/wiki/Alternative_parsers, WikiParser C++) w formie 
#key
#adam
#ewa
#piesek
#itd
#do wczytania do bazy jako csv
#powstaje kolekcja:
#{_id : id, klucz: Alergologia }
import re
file=open("plikpoczyszczeniu.txt", "a")

with open("articles_in_plain_text.txt") as infile:
	for line in infile:
		jak=" ".join(line.split()).replace(':', '').replace(';', '').replace('{', '').replace('}', '').replace(',', '').replace('.', '').replace('”', '').replace('„', '').replace('-', '').replace('(', '').replace(')', '')
		file.write(jak.replace(' ', '\n'))