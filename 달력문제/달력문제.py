		
def leap_year(year):
		if year%400==0 or (year%4==0 and year%100!=0):
				return True
		else:
				return False	

def Julian_startday(y):
		y+=8000
		startday=[]
		for m in range(1,13):
				if m in [1,2]:
						y-=1
						m+=12
						julian=(y*365)+(y//4)-(y//100)+(y//400)-1200820+(m*153+3)//5-92
						julian=julian%7
						julian=(julian+1)%7
						startday.append(julian)
						y+=1
						m-=12
				else:
						julian=(y*365)+(y//4)-(y//100)+(y//400)-1200820+(m*153+3)//5-92
						julian=julian%7
						julian=(julian+1)%7
						startday.append(julian)
		return startday
	
def lastday(month,year):
		if month in [1,3,5,7,8,10,12]:
				last_day=31
		elif month in [4,6,9,11]:
					last_day=30
		elif month==2:
					if leap_year(year):
							last_day=29
					else:
							last_day=28
		return last_day
	

	
def printing(year):
		months=["January","February","March","April","May","June","July",
"August","September","October","November","December"]
		startday=Julian_startday(year)
		line=0
		for i in range(1,13):
				print("{} {}".format(months[i-1],year))
				print("  S  M  T  W  T  F  S")
				for j in range(startday[i-1]):
						print("   ",end="")
				for k in range(1,lastday(i,year)+1):
						print(" ",end="")
						print('{:2d}'.format(k),end='')
						if (startday[i-1]+k)%7==0:
								print("\n",end="")
						if (k==lastday(i,year)):
								if (k+startday[i-1])%7==0:
										print("\n",end="")
				if (lastday(i,year)+startday[i-1])%7!=0:
						print("\n")
										
def main():
		year=int(input())
		printing(year)
		
if __name__ == '__main__':
    main()
