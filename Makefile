# Makefile for the Heterodox Econ Courses monorepo.
#
# Targets:
#   make build          — build all courses + notes into _site/
#   make preview        — build everything then serve _site/ at http://localhost:$(PORT) (default 9200)
#   make build-calc     — build only the Calculation Course
#   make build-notes    — build only the Quartz notes site
#   make clean          — remove _site/ and all course _book/ dirs
#
# Prerequisites: quarto, uv, node/npm (with Quartz set up via quartz/setup.sh)

COURSES := the_calculation_course 201 the_crypto_course
SITE    := _site
PORT    := 9200

.PHONY: build preview build-calc build-notes clean help

## build: Build all courses and notes, stitch into _site/
build: build-courses build-notes stitch

## preview: Build everything and serve _site/ at http://localhost:$(PORT)
preview: build
	@echo ""
	@echo "Serving $(SITE)/ at http://localhost:$(PORT)"
	@echo "Press Ctrl-C to stop."
	python3 -m http.server $(PORT) --directory $(SITE)

## build-courses: Render all course books to courses/<name>/_book/
build-courses:
	@for course in $(COURSES); do \
		echo "==> Building $$course ..."; \
		(cd courses/$$course && uv run quarto render --to html) || exit 1; \
	done

## build-calc: Build only the Calculation Course (faster during active study)
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
