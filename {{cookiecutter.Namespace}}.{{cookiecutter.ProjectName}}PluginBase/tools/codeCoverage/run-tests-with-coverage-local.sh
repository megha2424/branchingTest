#!/bin/bash -e

cd tools/codeCoverage
cd ../../

date=$(date '+%Y-%m-%dT%H%M%S')

dotnet tool install --global dotnet-reportgenerator-globaltool

dotnet build
dotnet test --results-directory tmp/coverage/test-results/$date --collect:"XPlat Code Coverage" --no-restore -- DataCollectionRunSettings.DataCollectors.DataCollector.Configuration.Format=json,opencover,cobertura

reportgenerator "-reports:tmp/coverage/test-results/$date/*/coverage.opencover.xml" "-targetdir:tmp/coverage/reports/$date" "-reporttypes:HtmlInline;Cobertura;Badges;Latex;" -verbosity:Info

start tmp/coverage/reports/$date/index.html