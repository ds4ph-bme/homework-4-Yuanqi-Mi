# Question 3
library(DBI)
library(RSQLite)

con <- dbConnect(RSQLite::SQLite(), dbname = here::here("opioid.db"))

population <- dbGetQuery(con, "SELECT * FROM population")
annual <- dbGetQuery(con, "SELECT * FROM annual")
land <- dbGetQuery(con, "SELECT * FROM land")

dbDisconnect(con)

head(annual[annual$countyfips == "NA", ])

head(annual[annual$countyfips == "NA" & annual$BUYER_STATE != "PR", ])

updated <- annual$BUYER_STATE == "AR" & annual$BUYER_COUNTY == "MONTGOMERY"
annual$countyfips[updated] <- 5097
head(annual[annual$BUYER_STATE == "AR" & annual$BUYER_COUNTY == "MONTGOMERY", ])

annual <- annual[annual$BUYER_COUNTY != "NA", ]
head(annual)

land_area <- land[, c("Areaname", "STCOU", "LND110210D")]
names(land_area) <- c("Areaname", "countyfips", "LND110210D")
head(land_area)

county_info <- merge(population, land_area, by = "countyfips", all.x = TRUE)
head(county_info)

print(paste("Length of land:", nrow(land)))
print(paste("Length of land_area:", nrow(land_area)))
print(paste("Length of county_info:", nrow(county_info)))
print(paste("Length of population:", nrow(population)))
