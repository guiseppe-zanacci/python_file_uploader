# uncomment where server should run
serverType = "Local" # has debug=True
#serverType = "Public" # Has debug=False

# port that the server runs on (5000 is default for flask)
# 80 is default for HTTP, 443 is default for HTTPS. If you want this however, you need nginx or similar
port = 5000

# route that serves upload page
# this can be set to something random for a hack "security solution" (ie "/jlJduJ9400328"),
# for someone to find a random route is unlikely
# must begin with "/"
route = "/"