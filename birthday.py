import datetime

def print_header():
	print("-----------------------------------")
	print("           Birthday App")
	print("-----------------------------------")
	print("")


def get_birthday():
	bday_year = input("What year were you born [YYYY]?")
	bday_month = input("What month were you born [MM]?")
	bday_day = input("What day were you born [DD]?")

	year = int(bday_year)
	month = int(bday_month)
	day = int(bday_day)

	birthday = datetime.date(year, month, day)

	return birthday

def compute_days(bday, now):
	cy_bday = datetime.date(now.year, month, day)
	print(cy_bday)
	

def print_bday(date):
	pass

def main():
	print_header()
	bday = get_birthday()
	now = datetime.date.today()
	number_of_days = compute_days(bday, now)
	print_bday(number_of_days)

main()