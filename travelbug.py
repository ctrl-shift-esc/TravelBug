import webbrowser
from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.keys import Keys

out_price = 0
in_price = 0



print 'Welcome to TravelBug!!'
print '**********************'
src_air = raw_input('Input your starting airport(s) [comma seperated] : ').split(",")
src_air = [x.strip() for x in src_air]
#src_air = src_air.capitalize()
print 'Starting from : ' + str(src_air)

to_date = datetime.datetime.strptime(raw_input('Starting date (dd.mm.yy): '), '%d.%m.%y')
#print 'Starting date: ', to_date.strftime('%d.%m.%y')

dur = int(raw_input('Minimum duration (in days): '))

from_date = to_date + datetime.timedelta(days=dur)
print to_date.strftime('%d.%m.%y'), ' --> ', from_date.strftime('%d.%m.%y')

browser = webdriver.Firefox()

browser.get("https://www.bookryanair.com/SkySales/booking.aspx?culture=de-de&lc=de-de")

print browser.title
browser.implicitly_wait(15)



for s in src_air:
	allSrcOptions = browser.find_element_by_xpath("//select[@name='SearchInput$Orig']").find_elements_by_tag_name("option")
	for srcOption in allSrcOptions:
	    if srcOption.get_attribute("value") == str(s):
	        #print 'Source : ' + srcOption.get_attribute("value")
	        srcOption.click()
	        time.sleep(1)
	        allDestOptions = browser.find_element_by_xpath("//select[@name='SearchInput$Dest']").find_elements_by_tag_name("option")
	        for destOptions in allDestOptions:
	        	if destOptions.get_attribute("value") == "":
	        		continue
	        	print srcOption.get_attribute("value") + ' --> ' + destOptions.get_attribute("value")
	        	destOptions.click()
	        	toDate = browser.find_element_by_xpath("//*[@id=\"search\"]/fieldset/table[2]/tbody/tr[2]/td[1]/input")
	        	toDate.clear()
	        	toDate.send_keys(to_date.strftime('%d.%m.%y'))
	        	fromDate = browser.find_element_by_xpath("//*[@id=\"search\"]/fieldset/table[2]/tbody/tr[2]/td[2]/input")
	        	fromDate.clear()
	        	fromDate.send_keys(from_date.strftime('%d.%m.%y'))
	        	browser.find_element_by_xpath("//*[@id=\"SearchInput_ButtonSubmit\"]").click()

	        	#print fromDate.get_attribute("value")
	        	break


#browser.close()


