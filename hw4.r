library(RSQLite)
db = dbConnect(RSQLite::SQLite(), dbname = "opioid.db")
annual = dbGetQuery(db, "SELECT * FROM annual")
population = dbGetQuery(db, "SELECT * FROM population")
land = dbGetQuery(db, "SELECT * FROM land")
dbDisconnect(db)
library(dplyr) # tidyverse installation failed so moved to dplyr for the purpose of this assignment
annual = annual %>%
  mutate(countyfips = if_else(BUYER_STATE == 'AR' & BUYER_COUNTY == 'MONTGOMERY', '05097', countyfips))
annual = annual %>% 
  filter(BUYER_COUNTY != "NA")
str(annual)
land_area = land %>% 
    select(Areaname, STCOU, LND110210D) %>% 
    rename(countyfips = STCOU)
county_info = population %>%
  left_join(land_area, by = 'countyfips')
str(county_info)