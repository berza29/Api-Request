# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests

url = "https://api.nasa.gov/EPIC/api/natural/images"

querystring = {"api_key":"DEMO_KEY"}

payload = ""
headers = {"cookie": "XSRF-TOKEN=eyJpdiI6Ii9NY09oZkJVdU1JWG1kekpkZ2J1TVE9PSIsInZhbHVlIjoiZ3JvRm5lWmpFQ1JhS3RGM3U0bzh6OVdkUmJwNUg5VTdXRWw2cVZMUjA2SEMwTUl5TWtTR0RvMEtqZUxPS0UvbC9SRkl2ZEltOXlrbmU1R2JCaHpiSk1LNFlZeXEvVlBTWHhVOWdwQVRMNDhQTHFLWGYzRERsMEl3aFV5NXNnU3EiLCJtYWMiOiJlN2E3OWExNGFiOTlmYmYwMDBjMDJjYTZlNjQ3NDk5MDllOGNlZWM3ZTY3OTVlNTNmYTMyM2RkMWU3YmUyMTk3IiwidGFnIjoiIn0%253D; laravel_session=eyJpdiI6IkN5a040bWEvZGlkakJTUjBRdDF3YVE9PSIsInZhbHVlIjoiVVJMN0VHc29heHovSVNLbDhZdjBKakszeXZDUXE1eW1sSTlLZC9CaGV1UDE3UzUyWkVlQ01ySkhLSDZkaEx1Yi91UXg0dGY0SVRvcmEwRFVVQVRSTGQ2OTlmaGxIcW5NTTU2bnpOcFhnRk1veVBIdGhkMCs1bjJ0WHFrd2F3OUkiLCJtYWMiOiJmNzE3ZjAwOWZlOWNkZWNjZTQ1YTRlMWYxNTdlMThiMmRkYzE4MjY2ZWY2NDQ5ZWI1MzdjY2I5NDlhMmFiMGE2IiwidGFnIjoiIn0%253D"}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)