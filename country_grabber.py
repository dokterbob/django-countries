#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Copyright (c) 2010, Alex Kuhl
Copyright (c) 2007, Fredrik Sjöblom (author of original django-countries)
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above
      copyright notice, this list of conditions and the following
      disclaimer in the documentation and/or other materials provided
      with the distribution.
    * Neither the name of the author nor the names of other
      contributors may be used to endorse or promote products derived
      from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

import urllib, sys, json

html = urllib.urlopen( "http://www.iso.org/iso/country_codes/iso_3166_code_lists/english_country_names_and_code_elements.htm" ).read( )

begintag = "<td valign=\"top\">"
btlen = len( begintag )
countries = [ ]

# a dictionary of priority values, 
# if a country is not in dictionary it gets default of 0
# see models.py for more info on sort priority
priority = {
  #"US": 100, # I want US first in my list so I give it a high value
}

# there's an Afghanistan earlier in the html code for the shortcut letters
# so start at the beginning of the table for finding it
begin = html.find( "AFGHANISTAN", html.find( "<table" ) )

while True:
  
  # find the country name
  end = html.find( "</", begin )
  country = html[ begin:end ].strip( )
  
  # find the country code
  begin = html.find( begintag, end ) + btlen
  end = html.find( "</td>", begin )
  iso = html[ begin:end ].strip( ).upper( )
  
  # Some rows are headings with the beginning letter, which are 
  # in strong tags so throw them out.  Also, Vatican is officially 
  # the Holy See but the ISO page has both listed, 
  # with the Vatican entry giving a link back up to Holy See.
  # In either case, not interested so skip that entry.
  if country.find( "<strong>" ) == -1 and country != "VATICAN CITY STATE":
    # some country names have an anchor thrown in with them, strip it out
    anchor = country.find( "<a" ) 
    if anchor > -1:
      country = country[ :anchor ].strip( )
            
    entry = { }
    entry[ 'pk' ] = iso
    entry[ 'model' ] = 'countries.country'
    fields = { }
    fields[ 'name_official' ] = country
    fields[ 'name' ] = country.title( )
    if iso in priority:
      fields[ 'sort_priority' ] = priority[ iso ]
    else:
      fields[ 'sort_priority' ] = 0
    entry[ 'fields' ] = fields
    countries.append( entry )
  try:
    begin = html.index( begintag, end, len( html )-10 ) + btlen 
  except:
    break

# write the json, if no filename is given dump to console
if len( sys.argv ) == 2:
  with open( sys.argv[ 1 ],  mode='w' ) as f:
    json.dump( countries, f, indent=2 )
else:
  print json.dumps( countries, indent=2 )


