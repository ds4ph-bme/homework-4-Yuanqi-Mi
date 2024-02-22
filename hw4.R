# Question 3
annual <- read.csv("county_annual.csv")
population <- read.csv("county_pop_arcos.csv")
land <- read.csv("land_area.csv")

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

dim(land)
dim(land_area)
dim(county_info)
dim(population)
