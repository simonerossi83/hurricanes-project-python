# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]
########################################################
# 1
# Update Recorded Damages
#######################################################
conversion = {"M": 1000000,
              "B": 1000000000}

def update_damages(damag):
  update_dam = []
  for i in damag:
    if i[-1] == "M":
      i = i[:-1]
      i = float(i)*conversion["M"]
    elif i[-1] == "B":
      i = i[:-1]
      i = float(i)*conversion["B"]
    else:
      i = i
    update_dam.append(i)
  return update_dam

# test function by updating damages

update = update_damages(damages)
############################################################
# 2 
# Create a Table
#######################################################
def create_table(name, month, year, wind, area, damage, death):
  table = {}
  for i in range(len(name)):
    table[name[i]] = {"Name": name[i], "Month": month[i], "Year": year[i], "Max Sustained Wind": wind[i], "Areas Affected": area[i], "Damage": damage[i], "Deaths": death[i]}
  return table


# Create and view the hurricanes dictionary
hurricanes = create_table (names, months, years, max_sustained_winds, areas_affected, update, deaths)
###############################################################
# 3
# Organizing by Year
####################################################
def organize_by_year(hurricanes):
  hurricane_by_year = {}
  for key, values in hurricanes.items():
    current_year = values['Year']
    current_cane = values['Name']
    if current_year not in hurricane_by_year:
      hurricane_by_year[current_year] = [hurricanes[current_cane]]
    else:
      hurricane_by_year[current_year].append([hurricanes[current_cane]])
  return hurricane_by_year


# create a new dictionary of hurricanes with year and key
hurricane_by_year = organize_by_year(hurricanes)
#print(hurricanes["Bahamas"])

############################################################################
# 4
# Counting Damaged Areas
#############################################################
def damaged_areas(hurricanes):
  damaged_areas_count = {}
  for name, value in hurricanes.items():
    area_list = value["Areas Affected"]
    for area in area_list:
      if area not in damaged_areas_count:
        damaged_areas_count[area] = 1
      else:
        damaged_areas_count[area] += 1
  return damaged_areas_count

#print(damaged_areas(hurricanes))

# create dictionary of areas to store the number of hurricanes involved in
damaged_areas = damaged_areas(hurricanes)
######################################################
# 5 
# Calculating Maximum Hurricane Count
######################################################
def most_affected(damaged_areas):
  return max(damaged_areas.items(), key = lambda k : k[1])
# find most frequently affected area and the number of hurricanes involved in

most_affected_area = most_affected(damaged_areas)
########################################################
# 6
# Calculating the Deadliest Hurricane
#######################################################
def find_deadliest(hurricanes):
  return hurricanes[max(hurricanes, key=lambda v: hurricanes[v]['Deaths'])]

# find highest mortality hurricane and the number of deaths
deadliest = find_deadliest(hurricanes)

######################################################
# 7
# Rating Hurricanes by Mortality
##########################################################
mortality_scale = {
0: 0,
1: 100,
2: 500,
3: 1000,
4: 10000}

def switch_mortality(death_no):
  if death_no == mortality_scale.get(0):
    return 0
  elif death_no > mortality_scale.get(0) and death_no < mortality_scale.get(1):
    return 1
  elif death_no >= mortality_scale.get(1) and death_no < mortality_scale.get(2):
    return 2
  elif death_no >= mortality_scale.get(2) and death_no < mortality_scale.get(3):
    return 3
  elif death_no >= mortality_scale.get(3) and death_no < mortality_scale.get(4):
    return 4
  elif death_no >= mortality_scale.get(4):
    return 5

def organize_by_mortality(hurricanes):
  hurricane_by_mortality = {}
  for key, values in hurricanes.items():
    current_death = values['Deaths']
    current_cane = values['Name']
    mortality_rating = switch_mortality(current_death)

    if mortality_rating not in hurricane_by_mortality:
      hurricane_by_mortality[mortality_rating] = [hurricanes[current_cane]]
    else:
      hurricane_by_mortality[mortality_rating].append([hurricanes[current_cane]])
  return hurricane_by_mortality

# categorize hurricanes in new dictionary with mortality severity as key
hurricanes_by_mortality = organize_by_mortality(hurricanes)

########################################
# 8 Calculating Hurricane Maximum Damage
########################################

def find_highest_damage(hurricanes):
  for key, values in hurricanes.items():
    if type(values["Damage"]) == str:
      values["Damage"] = 0
  return hurricanes[max(hurricanes, key=lambda v: hurricanes[v]['Damage'])]


# find highest damage inducing hurricane and its total cost
hurricane_greatest_damage = find_highest_damage(hurricanes)

#####################################
# 9
# Rating Hurricanes by Damage
####################################
damage_scale = {
0: 0,
1: 100000000,
2: 1000000000,
3: 10000000000,
4: 50000000000}

def switch_damage(damage):
  if damage == damage_scale.get(0):
    return 0
  elif damage > damage_scale.get(0) and damage < damage_scale.get(1):
    return 1
  elif damage >= damage_scale.get(1) and damage < damage_scale.get(2):
    return 2
  elif damage >= damage_scale.get(2) and damage < damage_scale.get(3):
    return 3
  elif damage >= damage_scale.get(3) and damage < damage_scale.get(4):
    return 4
  elif damage >= damage_scale.get(4):
    return 5
  
# categorize hurricanes in new dictionary with damage severity as key
def organize_by_damage(hurricanes):
  hurricane_by_damage = {}
  for key, values in hurricanes.items():
    current_damage = values['Damage']
    current_cane = values['Name']
    damage_rating = switch_damage(current_damage)

    if damage_rating not in hurricane_by_damage:
      hurricane_by_damage[damage_rating] = [hurricanes[current_cane]]
    else:
      hurricane_by_damage[damage_rating].append([hurricanes[current_cane]])
  return hurricane_by_damage

hurricanes_by_damage = organize_by_damage(hurricanes)

