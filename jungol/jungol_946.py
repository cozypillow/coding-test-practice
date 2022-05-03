countries = {}
num = int(input())
for _ in range(num):
    country, capital = input().split()
    countries[country] = capital
print(countries.get(input(), "Unknown Country"))