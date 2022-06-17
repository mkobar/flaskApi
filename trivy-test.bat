@echo off
REM runs a trivy image test with trivy docker image
REM need to provide a container id as %1

if [%1] == [] goto Missing

REM rmdir rootfs /S /Q
mkdir rootfs 2> trivy.log

docker export %1 | tar -C rootfs -xvf - 1>> trivy.log 2>&1

REM run the test
REM "cd rootfs && docker run -d -it aquasec/trivy rootfs . " 1> trivy-results.txt 2> trivy.err
cmd /c "cd /d rootfs && docker run --rm -it aquasec/trivy -q rootfs ." 1> trivy-results 2> trivy.err

REM remove ctl chars (https://stackoverflow.com/a/35582778)
type trivy-results | sed -r 's/\x1B\[(;?[0-9]{1,3})+[mGK]//g' > trivy-results.txt
cat trivy-results.txt

REM cleanup?
rmdir rootfs /S /Q
goto End

:Missing
echo Usage: %0 containerId

:End

