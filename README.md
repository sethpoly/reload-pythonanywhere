# reload-pythonanywhere
I needed a quick and easy way to refresh the data in my pythonanywhere applications. I saw this solution in their docs and I tailored it to my need.

# What It Does
- Uses your account API token to refresh any of your domains hosted on pythonanywhere.com.
- Useful when you're using an external database and you want to update the data every X minutes.

# How To Install
Just clone the repo and create a .env file containing:
- user : username of your pythonanywhere project
- api_token : the generated api token from your project
- domain_name : the domain of your project ex. sethpoly.pythonanywhere.com

Then run it in a bash file and it will reload your application ever X minutes.

# Technology Used
Python