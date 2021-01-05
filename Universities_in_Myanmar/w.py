import os

os.chdir('Home_Page')
a_list = os.listdir()
a_list.sort()


with open('/home/arch/TU_mawlamyine_website_datas/Universities_in_Myanmar/index.html', 'w') as file:
	file.write('<html>\n<head></head>\n<body>\n')
	for item in a_list:
		file.write(f"<p><a href='Home_Page/{item}'>"+ item[:-5] + '</a></p>' +'\n')
	file.write('</body>\n</html>')

