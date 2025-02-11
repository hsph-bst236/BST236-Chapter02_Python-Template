# This is a demo R code for R package dependencies management using renv.

# Initialize renv
install.packages("renv")
renv::init() # like venv

# Install packages
install.packages("dplyr")
install.packages("ggplot2")

# Snapshot/Freeze the Environment
renv::snapshot() # Updates the renv.lock like requirements.txt

# Restore the Environment
renv::restore() # Like pip install -r requirements.txt



