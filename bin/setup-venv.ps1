$scriptpath = split-path -parent $MyInvocation.MyCommand.Definition
$venvpath = $scriptpath + '\..\venv'

if (test-path $venvpath) {
    remove-item $venvpath -recurse -force
}

C:\Python3\python -m venv $venvpath

$upgradepip = $venvpath + '\Scripts\pip.exe install --upgrade pip'
Invoke-Expression $upgradepip

$installreqs = $venvpath + '\Scripts\pip.exe --no-cache-dir install --upgrade -r .\requirements.txt'
Invoke-Expression $installreqs

echo ""
echo "---------------------------------------------------------------------------------"
echo "Virtual Environment installed... to activate the environment in your shell run:"
echo "---------------------------------------------------------------------------------"
echo ".\venv\Scripts\Activate.ps1"
echo ""


