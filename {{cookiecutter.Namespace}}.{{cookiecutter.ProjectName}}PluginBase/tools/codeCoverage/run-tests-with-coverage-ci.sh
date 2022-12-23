#!/bin/bash -e

dotnet test ../../ --results-directory $(pwd)/../../tmp/coverage/test-results --collect:"XPlat Code Coverage" --no-restore -- DataCollectionRunSettings.DataCollectors.DataCollector.Configuration.Format=json,opencover,cobertura