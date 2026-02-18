Get-ChildItem -Path . -Recurse -Directory -Filter "__pycache__" |
    ForEach-Object {
        Write-Host "Deleting $($_.FullName)"
        Remove-Item -Recurse -Force -Path $_.FullName
    }

Write-Host "All __pycache__ folders removed."
