# uncomment where server should run
serverType = "Local" # has debug=True
#serverType = "Public" # has debug=False

# port that the server runs on (5000 is default for flask)
# 80 is default for HTTP, 443 is default for HTTPS. If you want this however, you need nginx or similar
port = 5000

# route that serves upload page
# this can be set to something random for a hack "security solution" (ie "/jlJduJ9400328"),
# for someone to find a random route is unlikely
# must begin with "/"
route = "/"

pageTitle = "Flask-File Drag Drop System" # displayed at tab, change as needed
pageHeader = "File drag & Drop System with flask dropzone" # displayed as the header

# set allowed file types by extension. Default is 
# eg ".txt, .html, .zip"
allowed_file_extensions = {
    'default': 'image/*, audio/*, video/*, text/*, application/*',
    'image': 'image/*',
    'audio': 'audio/*',
    'video': 'video/*',
    'text': 'text/*',
    'app': 'application/*'
}










# no touch
class Setup:
    def __init__(self):
        self.title = pageTitle
        self.header = pageHeader