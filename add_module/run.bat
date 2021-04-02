@echo off

SET writeDirectory=%CD%\%1
SET batchpath=%~dp0

pushd %batchpath%

pipenv run cli %writeDirectory%

IF %ERRORLEVEL% NEQ 0 echo "Unable to run add_module, have you run setup?"

popd