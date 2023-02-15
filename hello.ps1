# Get-ChildItem -Path "C:\\Windows\\Temp" *.*

# Get-ChildItem -Path "C:\\Windows\\Temp" *.* -Recurse| Remove-Item  -Recurse -Force  -ErrorAction SilentlyContinue


# foreach($erv in $server){
#     if ($erv.PSIsContainer){
#         Write-Host "Folder"
#     }
#     else{
#         Write-Host "Files"
#     }
# }

$names = Get-Content ".\ips.txt"
for($i=0;$i -le 10;$i++)
{

    foreach ($name in $names)
    {
        Test-Connection -Delay 15 -ComputerName $name -Count 1 -ErrorAction SilentlyContinue
    }
}

    # if (Test-Connection -Delay 15 -ComputerName $name -Count 1 -ErrorAction SilentlyContinue)
    # {
    
    #     $Output+= "$name"
        
    #     Write-Host "$Name is found" -ForegroundColor Green
        
    # }
    
    # else
    # {
    
    #     $Output+= "$name"
        
    #     Write-Host "$Name is not found" -ForegroundColor Red
    # }
    # Test-Connection google.com -Count 1 | Select IPV4Address
# while($count -le 2000)
# {
#     echo $count
#     $count+=1
# }
# do {$ping = test-connection google.com -Quiet} until (!$ping)

# while($count -le 10){
#     test-connection google.com
#     $count+=1
# }

# $ports = 22,53,80,445

# $ports | ForEach-Object
# {
#     $port = $_;
#     if (Test-NetConnection -ComputerName 8.8.8.8 -Port $port -InformationLevel Quiet -WarningAction SilentlyContinue)
#         {"Port $port is open" }
#     else
#         {"Port $port is closed"}
# }

# write-host "There are a total of $($args.count) arguments"
# for ( $i = 0; $i -lt $args.count; $i++ ) {
#     write-host "Argument  $i is $($args[$i])"
# }
# $computers="www.google.com","127.0.0.1","www.yahoo.com","www.hotmail.com"
# test-connection $computers -Count 1

# Get-ChildItem -Path "C:\Windows\Temp" . -Recurse
Get-Item -Path "C:\\Users\\user\\Pictures\\local\\NetRmm\*"
# Move-Item -Destination "C:\\Users\\user\\Pictures\\local\\NetRmm1"