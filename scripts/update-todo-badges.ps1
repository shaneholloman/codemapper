$todoPath = Join-Path $PSScriptRoot ".." "docs" "todo.md"
$readmePath = Join-Path $PSScriptRoot ".." "README.md"

# Ensure the todo.md file exists
if (-not (Test-Path $todoPath)) {
    Write-Error "Todo file not found at: $todoPath"
    exit 1
}

# Read the todo.md content
$todoContent = Get-Content -Path $todoPath -Raw

# Count completed and incomplete todos
$completedCount = ([regex]"- \[x\]").Matches($todoContent).Count
$incompleteCount = ([regex]"- \[ \]").Matches($todoContent).Count

# Read the README.md content
$readmeContent = Get-Content -Path $readmePath -Raw

# Update the badges using regex
$readmeContent = $readmeContent -replace '(\[!\[TODO\]\(https://img\.shields\.io/badge/✔%20Todo-)\d+(-purple\)\]\(docs/todo\.md\))', "`${1}$incompleteCount`${2}"
$readmeContent = $readmeContent -replace '(\[!\[TODO\]\(https://img\.shields\.io/badge/✔%20Done-)\d+(-purple\)\]\(docs/todo\.md\))', "`${1}$completedCount`${2}"

# Save the updated README.md
$readmeContent | Set-Content -Path $readmePath -NoNewline

Write-Host "Updated badges:"
Write-Host "Todos: $incompleteCount"
Write-Host "Completed: $completedCount"
