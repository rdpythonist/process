##############################Example 1##############################
# $name1='Rahul'
# Clear-Variable name


################################Example-2#################################

# Get-Content -Raw demo.json | ConvertFrom-Json
#################################Example-3#########################

Get-Service | Select-Object Name,DisplayName,Status -First 3 | ConvertTo-XML