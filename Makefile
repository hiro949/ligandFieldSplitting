CTBLLIB_URL  = https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbllib-1.3.11.tar.gz
ATLASREP_URL = https://www.math.rwth-aachen.de/~Thomas.Breuer/atlasrep/atlasrep-2.1.11.tar.gz
UTILS_URL    = https://github.com/gap-packages/utils/releases/download/v0.96/utils-0.96.tar.gz

download:
	mkdir -p downloads
	curl -L -o downloads/ctbllib-1.3.11.tar.gz   $(CTBLLIB_URL)
	curl -L -o downloads/atlasrep-2.1.11.tar.gz  $(ATLASREP_URL)
	curl -L -o downloads/utils-0.96.tar.gz        $(UTILS_URL)

build:
	docker compose build

run:
	docker compose run --rm sage sage irrReduce.py $(GROUP)

shell:
	docker compose run --rm sage sage

gap:
	docker compose run --rm sage gap
