#=========================
Django Countries

This is an application for Django projects providing fixtures and models for a
"complete" list of world countries based on the ISO 3166 standard. This fork 
drops the original project's goal of including US states as well as the 
country information gathered from the UN list (the three-letter abbreviations
and numeric codes).  The UN list may have a slightly different list of 
countries and some country names are definitely altered, but they are similar 
enough to make the considerable merging task not worth it.

#===================
# Installation

To install, copy the 'countries' folder into your django project's directory. 
Add 'countries' to the list of installed apps and run syncdb.

If flag icons are desired, the ISO 3166-1 alpha-2 country code flag package 
can be downloaded at http://www.famfamfam.com/lab/icons/flags/
Add a 'flags' directory to your media root and copy the images there. 
It is recommended to use the png versions because the code in this project 
defaults to looking for png.  
An alternative flag resource is http://www.ip2location.com/flagsoftheworld.aspx

As is, the initial_data fixture loads all countries with sort priorities. 
To make sure you have the most up-to-date list it is probably best to run this
script to replace initial_data.

Ex. ./country_grabber.py countries/fixtures/initial_data.json

If you need to change the display priority of any countries, 
for example if you would like the United States to list first in drop boxes by
default, add entries to the priority dictionary in country_grabber.py. 
These numbers are sorted in descending order, with the country naname ascending
used for those of the same priority. 

Requires Django 1.2+.
country_grabber tested on Python 2.6.5

#===================
# Settings

COUNTRIES_FLAG_PATH
  Alters the location or changes the image file type.  
  The location is relative to your site media root (MEDIA_URL).
  Example: COUNTRIES_FLAG_PATH = 'countries/flags/%s.gif'
  Default: 'flags/%s.png'

#========================
# Countries information

The data that will be put into the database on syncdb/flush is found in 
fixtures/initial_data.json. The json may be edited by hand or overwritten 
using the included country_grabber.py script.  Run without arguments it will 
dump the json to the console, it can also be given one argument, a filename, 
to declare the file to which the json should be written (you probably want to 
pass countries/fixtures/initial_data.json).  The script automatically parses 
the ISO page http://www.iso.org/iso/country_codes/iso_3166_code_lists/english_country_names_and_code_elements.htm


