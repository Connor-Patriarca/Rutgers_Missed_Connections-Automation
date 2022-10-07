import gspread

# Pull entries from Google Sheet
gc = gspread.service_account('test-project-364817-58d0da683a9b.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1GAGsJhb3pH9WLwLs7Kj9F_h0x0lweRL30qURPBguGfw/edit?usp=sharing')
worksheet = sh.sheet1

postNUM = 2
posttimeNUM = 2

post = worksheet.get('A{}'.format(postNUM)).first()
posttime = worksheet.get('B{}'.format(posttimeNUM)).first()

# from GenerateImage import missed_connection
# missed_connection()

print(post,'\n',posttime)