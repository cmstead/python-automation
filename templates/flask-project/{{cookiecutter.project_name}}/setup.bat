@echo off

SET batchpath=%~dp0

pushd %batchpath%

pipenv install

IF %ERRORLEVEL% NEQ 0 echo "Virtual environment creation failed. Have you installed pipenv?"

popd