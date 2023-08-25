lint:
	find ./libs -type f -name "*.py" | xargs pylint

clean_up:
	@echo "Removing old files!"
	rm *.html *.xml || true
	rm *.png || true

decrypt_staging:
	export KMS_KEY=projects/onec-stage/locations/global/keyRings/sops-staging-keyring/cryptoKeys/sops-staging-cryptokey
	/usr/local/bin/sops -d --gcp-kms $KMS_KEY ./data/stage.enc.json > ./data/stage.json

decrypt_prod:
	export KMS_KEY=projects/onec-prod/locations/global/keyRings/sops-prod-keyring/cryptoKeys/sops-prod-cryptokey
	/usr/local/bin/sops -d --gcp-kms $KMS_KEY ./data/prod.enc.json > ./data/prod.json

chrome_staging_parallel:
	pabot -i Smoke --logtitle Platform_Chrome_Staging --reporttitle Platform_Chrome_Staging \
	-l platform_staging_chrome_log.html -r platform_staging_chrome_report.html -o platform_staging_chrome_output.xml \
	--variable BROWSER:chrome --variable URL:https://csadmin.staging.onec.co/#/orgs --variable ENVFILE:stage.json \
	--pythonpath ./libs/pages tests/
#	robot -i Smoke --logtitle Platform_Chrome_Staging --reporttitle Platform_Chrome_Staging \
#	-l platform_staging_chrome_log.html -r platform_staging_chrome_report.html -o platform_staging_chrome_output.xml \
#	--variable BROWSER:chrome --variable URL:https://csadmin.staging.onec.co/#/orgs --variable ENVFILE:stage.json \
#	--pythonpath ./libs/pages tests/

chrome_prod_parallel:
	pabot -i Smoke --logtitle Platform_Chrome_Prod --reporttitle Platform_Chrome_Prod \
	-l platform_prod_chrome_log.html -r platform_prod_chrome_report.html -o platform_prod_chrome_output.xml \
	--variable BROWSER:chrome --variable URL:https://csadmin.oneconcern.com/#/orgs --variable ENVFILE:prod.json \
	--pythonpath ./libs/pages tests/
#	robot -i Smoke --logtitle Platform_Chrome_Prod --reporttitle Platform_Chrome_Prod \
#	-l platform_prod_chrome_log.html -r platform_prod_chrome_report.html -o platform_prod_chrome_output.xml \
#	--variable BROWSER:chrome --variable URL:https://csadmin.oneconcern.com/#/orgs --variable ENVFILE:prod.json \
#	--pythonpath ./libs/pages tests/
