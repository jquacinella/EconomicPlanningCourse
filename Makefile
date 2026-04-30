# Makefile for the Heterodox Econ Courses monorepo.
#
# Day-to-day editing (live reload):
#   make dev / dev-calc  — Calculation Course at http://localhost:4444
#   make dev-201         — 201 course at http://localhost:4445
#   make dev-crypto      — Crypto Course at http://localhost:4446
#   make dev-notes       — Quartz notes site at http://localhost:8080
#
# Full-site build (one-shot, for checking before push):
#   make build          — build all courses + notes into _site/
#   make preview        — build then serve _site/ at http://localhost:$(PORT) (default 9200)
#   make build-calc     — build only the Calculation Course
#   make build-notes    — build only the Quartz notes site
#   make clean          — remove _site/ and all course _book/ dirs
#
# Prerequisites: quarto, uv, node/npm (with Quartz set up via quartz/setup.sh)

COURSES    := the_calculation_course 201 the_crypto_course
SITE       := _site
PORT       := 9200

.PHONY: build preview dev dev-calc dev-201 dev-crypto dev-notes build-calc build-notes stitch clean help

## dev-calc: Live-reload quarto preview for the Calculation Course (port 4444)
dev-calc:
	@echo "Starting quarto preview for the_calculation_course at http://localhost:4444"
	cd courses/the_calculation_course && uv run quarto preview

## dev-201: Live-reload quarto preview for the 201 course (port 4445)
dev-201:
	@echo "Starting quarto preview for 201 at http://localhost:4445"
	cd courses/201 && uv run quarto preview

## dev-crypto: Live-reload quarto preview for the Crypto Course (port 4446)
dev-crypto:
	@echo "Starting quarto preview for the_crypto_course at http://localhost:4446"
	cd courses/the_crypto_course && uv run quarto preview

## dev: Alias for dev-calc (default course)
dev: dev-calc

## dev-notes: Live-reload Quartz notes site
dev-notes:
	@echo "Starting Quartz notes site with live reload ..."
	@echo "Open http://localhost:8080"
	cd quartz && npx quartz build --serve --port 8080

## build: Build all courses and notes, stitch into _site/
build: build-courses build-notes stitch

## preview: Build everything and serve _site/ at http://localhost:$(PORT)
preview: build
	@echo ""
	@echo "Serving $(SITE)/ at http://localhost:$(PORT)"
	@echo "Press Ctrl-C to stop."
	python3 -m http.server $(PORT) --directory $(SITE)

## build-courses: Render all course books (uses freeze cache — only re-executes changed cells)
build-courses:
	@for course in $(COURSES); do \
		echo "==> Building $$course ..."; \
		(cd courses/$$course && uv run quarto render --to html) || exit 1; \
	done

## build-calc: Build only the Calculation Course
build-calc:
	cd courses/the_calculation_course && uv run quarto render --to html

## build-notes: Build the Quartz notes site into quartz/public/
build-notes:
	@echo "==> Building Quartz notes site ..."
	cd quartz && npx quartz build

## stitch: Assemble _site/ from all build outputs
stitch:
	@echo "==> Stitching outputs into $(SITE)/ ..."
	rm -rf $(SITE)
	mkdir -p $(SITE)
	# Landing page at root
	cp site-root/index.html $(SITE)/index.html
	# Each course book at /courses/<name>/
	@for course in $(COURSES); do \
		if [ -d "courses/$$course/_book" ]; then \
			mkdir -p "$(SITE)/courses/$$course"; \
			cp -r "courses/$$course/_book/." "$(SITE)/courses/$$course/"; \
			echo "  stitched: courses/$$course"; \
		else \
			echo "  skipped (no _book/): courses/$$course"; \
		fi; \
	done
	# Notes site at /notes/
	mkdir -p $(SITE)/notes
	cp -r quartz/public/. $(SITE)/notes/
	echo "  stitched: notes/"
	@echo ""
	@echo "$(SITE)/ is ready. Run 'make preview' to serve it."

## clean: Remove _site/ and all course _book/ directories
clean:
	rm -rf $(SITE)
	@for course in $(COURSES); do \
		rm -rf "courses/$$course/_book"; \
		echo "  cleaned: courses/$$course/_book"; \
	done
	rm -rf quartz/public
	@echo "Clean done."

## help: Show this help
help:
	@grep -E '^## ' Makefile | sed 's/^## //'
