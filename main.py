import application.db.people as people , application.salary as salary, additional_functions.my_jokes as my_jokes, additional_functions.my_time as my_time


if __name__ == "__main__":
	print(my_jokes.get_jokes())
	print(my_time.time_now())
	print(people.get_employees())
	print(salary.calculate_salar())
   
   