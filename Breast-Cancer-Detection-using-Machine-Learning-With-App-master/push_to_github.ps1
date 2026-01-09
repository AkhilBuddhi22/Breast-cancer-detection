# Script to push code to GitHub
Set-Location "c:\Users\akh56\Downloads\Breast-Cancer-Detection-using-Machine-Learning-With-App-master"

# Abort any pending merge
git merge --abort 2>$null

# Configure git to not open editor
git config core.editor "echo"

# Fetch remote
Write-Host "Fetching from remote..." -ForegroundColor Cyan
git fetch origin

# Force push (since the repository appears to be yours and you want to overwrite)
Write-Host "Pushing to GitHub..." -ForegroundColor Cyan
git push origin main --force

Write-Host "`nDone! Check your repository at: https://github.com/AkhilBuddhi22/Breast-cancer-detection.git" -ForegroundColor Green
